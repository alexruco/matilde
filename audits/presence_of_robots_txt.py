# audits/presence_of_robots_txt.py

from malcom import AuditBase
from malcom.metadata.architecture_metadata import ARCHITECTURE_METADATA

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
        print(f"Running {self.name} on the website: {website}")
        if "robots.txt" in website:  # Simplified example check
            self.passed = True
        else:
            self.passed = False
            self.issues.append("robots.txt file is missing.")
