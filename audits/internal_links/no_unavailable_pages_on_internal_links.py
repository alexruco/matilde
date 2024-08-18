# audits/no_unavailable_pages_on_internal_links.py

import sqlite3
from malcom import AuditBase
from malcom.metadata.architecture_metadata import ARCHITECTURE_METADATA

class NoUnavailablePagesOnInternalLinksAudit(AuditBase):
    def __init__(self, db_path):
        metadata = ARCHITECTURE_METADATA["no_unavailable_pages_on_internal_links"]
        super().__init__(
            name=metadata["name"],
            importance=metadata["importance"],
            measurement_criteria=metadata["measurement_criteria"],
            fix_methods=metadata["fix_methods"],
            use_cases=metadata["use_cases"]
        )
        self.db_path = db_path

    def run(self, website):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        unavailable_pages = []

        try:
            # Query to find all internal links with an unsuccessful fetch status
            query = """
            SELECT url, referring_pages FROM tb_pages
            WHERE successful_page_fetch = 0 AND referring_pages IS NOT NULL AND referring_pages != ''
            """

            cursor.execute(query)
            pages_with_issues = cursor.fetchall()

            for url, referring_pages in pages_with_issues:
                referring_pages_list = referring_pages.split(',')
                unavailable_pages.append((url, referring_pages_list))

            if unavailable_pages:
                self.passed = False
                for url, referring_pages_list in unavailable_pages:
                    self.issues.append(
                        f"The page '{url}' is unavailable but is linked from: {', '.join(referring_pages_list)}"
                    )
            else:
                self.passed = True

        except sqlite3.Error as e:
            self.passed = False
            self.issues.append(f"Database error occurred: {e}")
        
        finally:
            cursor.close()
            connection.close()
