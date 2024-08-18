# audits/no_redirected_pages_on_internal_links.py

import sqlite3
import requests
from malcom import AuditBase
from malcom.metadata.architecture_metadata import ARCHITECTURE_METADATA

class NoRedirectedPagesOnInternalLinksAudit(AuditBase):
    def __init__(self, db_path):
        metadata = ARCHITECTURE_METADATA["no_redirected_pages_on_internal_links"]
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
            # Query to find all internal links (referring pages)
            query = """
            SELECT DISTINCT referring_pages FROM tb_pages
            WHERE referring_pages IS NOT NULL AND referring_pages != ''
            """

            cursor.execute(query)
            referring_pages_records = cursor.fetchall()

            # Flatten the list of URLs
            internal_links = []
            for record in referring_pages_records:
                internal_links.extend(record[0].split(','))

            # Check for redirections in each internal link
            for link in internal_links:
                link = link.strip()
                is_redirected, response = self.check_for_redirection(link)
                if is_redirected:
                    redirected_pages.append((link, response.headers.get('Location')))

            if redirected_pages:
                self.passed = False
                for url, redirection_target in redirected_pages:
                    self.issues.append(
                        f"The page '{url}' results in a redirection to '{redirection_target}'."
                    )
            else:
                self.passed = True

        except sqlite3.Error as e:
            self.passed = False
            self.issues.append(f"Database error occurred: {e}")
        
        finally:
            cursor.close()
            connection.close()
