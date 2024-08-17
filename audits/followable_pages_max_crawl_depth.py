# audits/followable_pages_max_crawl_depth.py

from malcom import AuditBase
from malcom.metadata.architecture_metadata import ARCHITECTURE_METADATA

class FollowablePagesMaxCrawlDepthAudit(AuditBase):
    def __init__(self):
        metadata = ARCHITECTURE_METADATA["followable_pages_max_crawl_depth"]
        super().__init__(
            name=metadata["name"],
            importance=metadata["importance"],
            measurement_criteria=metadata["measurement_criteria"],
            fix_methods=metadata["fix_methods"],
            use_cases=metadata["use_cases"]
        )

    def run(self, website):
        # Placeholder logic
        pages_with_high_crawl_depth = ["page1.html", "page2.html"]  # Example pages with crawl depth > 3
        issues = ["some issue", "some other issue"]

        if pages_with_high_crawl_depth:
            self.passed = False
            self.issues.append("The following pages have a crawl depth greater than 3: " + ", ".join(pages_with_high_crawl_depth))
        else:
            self.passed = True
