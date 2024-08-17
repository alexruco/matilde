# audits/no_follow_pages_without_internal_links.py

from malcom import AuditBase
from malcom.metadata.architecture_metadata import ARCHITECTURE_METADATA

class NoFollowPagesWithoutInternalLinksAudit(AuditBase):
    def __init__(self):
        metadata = ARCHITECTURE_METADATA["no_follow_pages_without_internal_links"]
        super().__init__(
            name=metadata["name"],
            importance=metadata["importance"],
            measurement_criteria=metadata["measurement_criteria"],
            fix_methods=metadata["fix_methods"],
            use_cases=metadata["use_cases"]
        )

    def run(self, website):
        # Placeholder logic
        no_follow_pages_with_internal_links = ["page5.html", "page6.html"]  # Example no-followable pages with internal links
        issues = ["some issue", "some other issue"]

        if no_follow_pages_with_internal_links:
            self.passed = False
            self.issues.append("The following no-followable pages have internal followable links: " + ", ".join(no_follow_pages_with_internal_links))
        else:
            self.passed = True
