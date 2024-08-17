# audits/followable_pages_with_internal_links.py

from malcom import AuditBase
from malcom.metadata.architecture_metadata import ARCHITECTURE_METADATA

class FollowablePagesWithInternalLinksAudit(AuditBase):
    def __init__(self):
        metadata = ARCHITECTURE_METADATA["followable_pages_with_internal_links"]
        super().__init__(
            name=metadata["name"],
            importance=metadata["importance"],
            measurement_criteria=metadata["measurement_criteria"],
            fix_methods=metadata["fix_methods"],
            use_cases=metadata["use_cases"]
        )

    def run(self, website):
        # Replace this with actual logic later
        pages_without_internal_links = ["page1.html", "page2.html"]  # Placeholder list of pages without internal links
        issues = ["some issue", "some other issue"]
        
        if pages_without_internal_links:
            self.passed = False
            self.issues.append("The following pages do not have any internal followable links: " + ", ".join(pages_without_internal_links))
        else:
            self.passed = True
