# audits/all_followable_pages_in_sitemap.py

from malcom import AuditBase
from malcom.metadata.architecture_metadata import ARCHITECTURE_METADATA

class AllFollowablePagesInSitemapAudit(AuditBase):
    def __init__(self):
        metadata = ARCHITECTURE_METADATA["all_followable_pages_in_sitemap"]
        super().__init__(
            name=metadata["name"],
            importance=metadata["importance"],
            measurement_criteria=metadata["measurement_criteria"],
            fix_methods=metadata["fix_methods"],
            use_cases=metadata["use_cases"]
        )

    def run(self, website):
        # Placeholder logic
        all_followable_pages_in_sitemap = ["page1.html", "page2.html"]  # Example followable pages not in sitemap
        issues = ["some issue", "some other issue"]
        
        if all_followable_pages_in_sitemap:
            self.passed = False
            self.issues.append("The following followable pages are not listed in any sitemap: " + ", ".join(all_followable_pages_in_sitemap))
        else:
            self.passed = True
