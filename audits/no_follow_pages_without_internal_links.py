# audits/no_follow_pages_without_internal_links.py

import sqlite3
import requests
from bs4 import BeautifulSoup
from malcom import AuditBase
from malcom.metadata.architecture_metadata import ARCHITECTURE_METADATA

class NoFollowPagesWithoutInternalLinksAudit(AuditBase):
    def __init__(self, db_path):
        metadata = ARCHITECTURE_METADATA["no_follow_pages_without_internal_links"]
        super().__init__(
            name=metadata["name"],
            importance=metadata["importance"],
            measurement_criteria=metadata["measurement_criteria"],
            fix_methods=metadata["fix_methods"],
            use_cases=metadata["use_cases"]
        )
        self.db_path = db_path

    def check_followable_links(self, referring_page, target_url):
        """
        Check if the referring page has followable links to the target URL.
        """
        try:
            response = requests.get(referring_page)
            if response.status_code != 200:
                return False, None

            soup = BeautifulSoup(response.content, 'html.parser')
            followable_links = []

            # Find all <a> tags pointing to the target_url
            for link in soup.find_all('a', href=True):
                if link['href'].strip('/') == target_url.strip('/'):
                    # Check if the link is followable (i.e., not rel="nofollow")
                    if 'nofollow' not in link.get('rel', []):
                        followable_links.append(referring_page)

            return len(followable_links) > 0, followable_links
        except Exception as e:
            print(f"Error fetching or parsing {referring_page}: {e}")
            return False, None

    def run(self, website):
        # Connect to the SQLite database
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        try:
            # Query to find no-follow pages (robots_follow = False) that have internal links
            query = """
            SELECT url, referring_pages FROM tb_pages
            WHERE robots_follow = 0 AND (referring_pages IS NOT NULL AND referring_pages != '')
            """

            cursor.execute(query)
            pages_with_internal_links = cursor.fetchall()

            if pages_with_internal_links:
                self.passed = False
                for url, referring_pages in pages_with_internal_links:
                    referring_pages_list = referring_pages.split(',')

                    followable_referrers = []
                    for referring_page in referring_pages_list:
                        has_followable_link, followable_links = self.check_followable_links(referring_page.strip(), url)
                        if has_followable_link:
                            followable_referrers.extend(followable_links)

                    if followable_referrers:
                        self.issues.append(
                            f"Page '{url}' is no-follow but has followable links from: {', '.join(followable_referrers)}"
                        )

                if not self.issues:
                    self.passed = True
            else:
                self.passed = True

        except sqlite3.Error as e:
            self.passed = False
            self.issues.append(f"Database error occurred: {e}")
        
        finally:
            cursor.close()
            connection.close()
