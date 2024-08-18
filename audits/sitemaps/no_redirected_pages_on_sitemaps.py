# audits/no_redirected_pages_on_sitemaps.py

import sqlite3
import requests
from malcom import AuditBase
from malcom.metadata.architecture_metadata import ARCHITECTURE_METADATA

class NoRedirectedPagesOnSitemapsAudit(AuditBase):
    def __init__(self, db_path):
        metadata = ARCHITECTURE_METADATA["no_redirected_pages_on_sitemaps"]
        super().__init__(
            name=metadata["name"],
            importance=metadata["importance"],
            measurement_criteria=metadata["measurement_criteria"],
            fix_methods=metadata["fix_methods"],
            use_cases=metadata["use_cases"]
        )
        self.db_path = db_path

    def check_for_redirection(self, url):
        """
        Checks if the given URL results in a redirection.
        """
        try:
            response = requests.get(url, allow_redirects=False)
            return response.status_code in [301, 302, 303, 307, 308], response
        except requests.RequestException as e:
            print(f"Error checking {url}: {e}")
            return False, None

    def run(self, website):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        redirected_pages = []

        try:
            # Query to find all pages listed in sitemaps
            query = """
            SELECT url, sitemaps FROM tb_pages
            WHERE sitemaps IS NOT NULL AND sitemaps != ''
            """

            cursor.execute(query)
            pages_with_sitemaps = cursor.fetchall()

            # Check for redirections in each sitemap URL
            for url, sitemaps in pages_with_sitemaps:
                is_redirected, response = self.check_for_redirection(url)
                if is_redirected:
                    redirected_pages.append((url, response.headers.get('Location'), sitemaps))

            if redirected_pages:
                self.passed = False
                for url, redirection_target, sitemaps in redirected_pages:
                    self.issues.append(
                        f"The page '{url}' listed in sitemaps '{sitemaps}' results in a redirection to '{redirection_target}'."
                    )
            else:
                self.passed = True

        except sqlite3.Error as e:
            self.passed = False
            self.issues.append(f"Database error occurred: {e}")
        
        finally:
            cursor.close()
            connection.close()
