# audits/sitemap_in_robots_txt.py

from malcom import AuditBase
from malcom.metadata.architecture_metadata import ARCHITECTURE_METADATA
from dourado import sitemap_indicated_on_robots, website_sitemaps

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
        # Check if any sitemap is indicated in robots.txt
        sitemap_indicated = sitemap_indicated_on_robots(website_url=website)
        if sitemap_indicated:
            self.passed = True
        else:
            # If no sitemap is found in robots.txt, check for any sitemaps found on the website
            self.passed = False
            sitemaps_found = website_sitemaps(website_url=website)
            if sitemaps_found:
                sitemaps_list = ', '.join(sitemaps_found)
                self.issues.append(f"No sitemap listed in robots.txt, but found these sitemaps on the website: {sitemaps_list}.")
            else:
                self.issues.append("No sitemap listed in robots.txt and no sitemaps found on the website.")
