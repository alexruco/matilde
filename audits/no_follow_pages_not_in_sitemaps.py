# audits/no_follow_pages_not_in_sitemaps.py

import sqlite3
from malcom import AuditBase
from malcom.metadata.architecture_metadata import ARCHITECTURE_METADATA

class NoFollowPagesNotInSitemapsAudit(AuditBase):
    def __init__(self, db_path):
        metadata = ARCHITECTURE_METADATA["no_follow_pages_not_in_sitemaps"]
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
            # Query to find no-follow pages (robots_follow = False) that have sitemaps listed
            query = """
            SELECT url FROM tb_pages
            WHERE robots_follow = 0 AND (sitemaps IS NOT NULL AND sitemaps != '')
            """

            cursor.execute(query)
            pages_in_sitemaps = cursor.fetchall()

            if pages_in_sitemaps:
                self.passed = False
                urls = [row[0] for row in pages_in_sitemaps]
                self.issues.append(f"The following no-followable pages are incorrectly listed in sitemaps: {', '.join(urls)}")
            else:
                self.passed = True

        except sqlite3.Error as e:
            self.passed = False
            self.issues.append(f"Database error occurred: {e}")
        
        finally:
            cursor.close()
            connection.close()
