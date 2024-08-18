# audits/followable_pages_with_internal_links.py

import sqlite3
from malcom import AuditBase
from malcom.metadata.architecture_metadata import ARCHITECTURE_METADATA

class AllFollowablePagesWithInternalLinksAudit(AuditBase):
    def __init__(self, db_path):
        metadata = ARCHITECTURE_METADATA["followable_pages_with_internal_links"]
        super().__init__(
            name=metadata["name"],
            importance=metadata["importance"],
            measurement_criteria=metadata["measurement_criteria"],
            fix_methods=metadata["fix_methods"],
            use_cases=metadata["use_cases"]
        )
        self.db_path = db_path

    def run(self, website):
        # Connect to the SQLite database
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        try:
            # Query to find followable pages (robots_follow = True) with no internal links (referring_pages is NULL or empty)
            query = """
            SELECT url FROM tb_pages
            WHERE robots_follow = 1 AND (referring_pages IS NULL OR referring_pages = '')
            """

            cursor.execute(query)
            pages_without_internal_links = cursor.fetchall()

            if pages_without_internal_links:
                self.passed = False
                urls = [row[0] for row in pages_without_internal_links]
                self.issues.append(f"The following followable pages do not have any internal followable links: {', '.join(urls)}")
            else:
                self.passed = True

        except sqlite3.Error as e:
            self.passed = False
            self.issues.append(f"Database error occurred: {e}")
        
        finally:
            cursor.close()
            connection.close()
