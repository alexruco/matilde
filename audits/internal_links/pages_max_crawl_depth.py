# audits/followable_pages_max_crawl_depth.py

import sqlite3
from malcom import AuditBase
from malcom.metadata.architecture_metadata import ARCHITECTURE_METADATA

class PagesMaxCrawlDepthAudit(AuditBase):
    def __init__(self, db_path):
        metadata = ARCHITECTURE_METADATA["followable_pages_max_crawl_depth"]
        super().__init__(
            name=metadata["name"],
            importance=metadata["importance"],
            measurement_criteria=metadata["measurement_criteria"],
            fix_methods=metadata["fix_methods"],
            use_cases=metadata["use_cases"]
        )
        self.db_path = db_path
        self.max_depth = 3

    def calculate_crawl_depth(self, cursor, url, depth=0, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        # If we already visited this URL, return a high depth to prevent infinite loops
        if url in visited:
            return float('inf'), path

        visited.add(url)
        path.append(url)

        # Base case: if depth exceeds max_depth, return immediately
        if depth > self.max_depth:
            return depth, path

        # Query to find the pages that link to this URL (referring pages)
        cursor.execute("SELECT referring_pages FROM tb_pages WHERE url = ?", (url,))
        row = cursor.fetchone()

        if not row or not row[0]:
            return depth, path

        referring_pages = row[0].split(',')

        # Recursively calculate the minimum depth among all referring pages
        min_depth = float('inf')
        min_path = list(path)
        for referring_page in referring_pages:
            referring_page = referring_page.strip()
            current_depth, current_path = self.calculate_crawl_depth(cursor, referring_page, depth + 1, visited, list(path))
            if current_depth < min_depth:
                min_depth = current_depth
                min_path = current_path

        return min_depth, min_path

    def run(self, website):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        try:
            # Query to find all followable pages
            cursor.execute("SELECT url FROM tb_pages WHERE robots_follow = 1")
            followable_pages = cursor.fetchall()

            pages_with_high_crawl_depth = []

            for (url,) in followable_pages:
                crawl_depth, path = self.calculate_crawl_depth(cursor, url)
                if crawl_depth > self.max_depth:
                    pages_with_high_crawl_depth.append((url, path))

            if pages_with_high_crawl_depth:
                self.passed = False
                for url, path in pages_with_high_crawl_depth:
                    self.issues.append(
                        f"Page '{url}' has a crawl depth greater than {self.max_depth}. Referring path: " +
                        " -> ".join(path)
                    )
            else:
                self.passed = True

        except sqlite3.Error as e:
            self.passed = False
            self.issues.append(f"Database error occurred: {e}")
        
        finally:
            cursor.close()
            connection.close()
