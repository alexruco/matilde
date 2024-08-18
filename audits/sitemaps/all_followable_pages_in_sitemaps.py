# audits/all_followable_pages_in_sitemap.py

import sqlite3
from malcom import AuditBase
from malcom.metadata.architecture_metadata import ARCHITECTURE_METADATA

class AllFollowablePagesInSitemapsAudit(AuditBase):
    def __init__(self, db_path):
        metadata = ARCHITECTURE_METADATA["all_followable_pages_in_sitemap"]
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
            # Query to find followable pages (robots_follow = True) with empty sitemaps
            query = """
            SELECT url FROM tb_pages
            WHERE robots_follow = 1 AND (sitemaps IS NULL OR sitemaps = '')
            """

            cursor.execute(query)
            pages_without_sitemaps = cursor.fetchall()

            if pages_without_sitemaps:
                self.passed = False
                urls = [row[0] for row in pages_without_sitemaps]
                self.issues.append(f"The following followable pages are not listed in any sitemap: {', '.join(urls)}")
            else:
                self.passed = True

        except sqlite3.Error as e:
            self.passed = False
            self.issues.append(f"Database error occurred: {e}")
        
        finally:
            cursor.close()
            connection.close()
