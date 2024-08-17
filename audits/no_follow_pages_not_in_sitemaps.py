# audits/no_follow_pages_not_in_sitemaps.py

from malcom import AuditBase
from malcom.metadata.architecture_metadata import ARCHITECTURE_METADATA

class NoFollowPagesNotInSitemapsAudit(AuditBase):
    def __init__(self):
        metadata = ARCHITECTURE_METADATA["no_follow_pages_not_in_sitemaps"]
        super().__init__(
            name=metadata["name"],
            importance=metadata["importance"],
            measurement_criteria=metadata["measurement_criteria"],
            fix_methods=metadata["fix_methods"],
            use_cases=metadata["use_cases"]
        )

    def run(self, website):
        # Placeholder logic
        no_follow_pages_in_sitemaps = ["page3.html", "page4.html"]  # Example no-followable pages included in sitemaps
        issues = ["some issue", "some other issue"]

        if no_follow_pages_in_sitemaps:
            self.passed = False
            self.issues.append("The following no-followable pages are listed in sitemaps: " + ", ".join(no_follow_pages_in_sitemaps))
        else:
            self.passed = True
