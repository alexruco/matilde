# audits/presence_of_robots_txt.py

from malcom import AuditBase
from malcom.metadata.architecture_metadata import ARCHITECTURE_METADATA
from dourado import robots_exists

class PresenceOfRobotsTxtAudit(AuditBase):
    def __init__(self):
        metadata = ARCHITECTURE_METADATA["presence_of_robots_txt"]
        super().__init__(
            name=metadata["name"],
            importance=metadata["importance"],
            measurement_criteria=metadata["measurement_criteria"],
            fix_methods=metadata["fix_methods"],
            use_cases=metadata["use_cases"]
        )

    def run(self, website):        
        if robots_exists(website):  # Using dourado to check for robots.txt presence
            self.passed = True
        else:
            self.passed = False
            self.issues.append("robots.txt file is missing.")
