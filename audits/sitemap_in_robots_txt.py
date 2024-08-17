# audits/sitemap_in_robots_txt.py

from malcom import AuditBase
from malcom.metadata.architecture_metadata import ARCHITECTURE_METADATA
from dourado import sitemap_indicated_on_robots

class SitemapInRobotsTxtAudit(AuditBase):
    def __init__(self):
        metadata = ARCHITECTURE_METADATA["sitemap_in_robots_txt"]
        super().__init__(
            name=metadata["name"],
            importance=metadata["importance"],
            measurement_criteria=metadata["measurement_criteria"],
            fix_methods=metadata["fix_methods"],
            use_cases=metadata["use_cases"]
        )

    def run(self, website):        
        sitemap_indicated = sitemap_indicated_on_robots(website_url=website)
        if sitemap_indicated:  # Check for 'sitemap' in robots.txt
            self.passed = True
        else:
            self.passed = False
            self.issues.append("No sitemap listed in robots.txt.")
