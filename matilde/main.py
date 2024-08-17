# matilde/main.py

import sys
import os

# Ensure the parent directory is in the path so that 'audits' can be found
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from audits.presence_of_robots_txt import PresenceOfRobotsTxtAudit
from audits.sitemap_in_robots_txt import SitemapInRobotsTxtAudit
from audits.followable_pages_with_internal_links import  FollowablePagesWithInternalLinksAudit
from audits.all_followable_pages_in_sitemap import AllFollowablePagesInSitemapAudit
from audits.followable_pages_max_crawl_depth import FollowablePagesMaxCrawlDepthAudit
from audits.no_follow_pages_not_in_sitemaps import NoFollowPagesNotInSitemapsAudit
from audits.no_follow_pages_without_internal_links import NoFollowPagesWithoutInternalLinksAudit

from bertha import recrawl_website



def run_audits(website):
    audits = [
        PresenceOfRobotsTxtAudit(),
        SitemapInRobotsTxtAudit(),
        #FollowablePagesWithInternalLinksAudit(),
        #AllFollowablePagesInSitemapAudit(),
        #FollowablePagesMaxCrawlDepthAudit(),
        #NoFollowPagesNotInSitemapsAudit(),
        #NoFollowPagesWithoutInternalLinksAudit()
    ]

    results = {}
    for audit in audits:
        audit.run(website)
        results[audit.name] = {
            "passed": audit.get_result(),
            "issues": audit.get_issues(),
        }
    
    return results

if __name__ == "__main__":
    # Example website data
    website_url = "mysitefaster.com"  # This URL will be used by the dourado package
    
    results = run_audits(website_url)
    
    website_data = recrawl_website(website_url)
    
    print(website_data)
    for audit_name, result in results.items():
        print(f"Audit: {audit_name}")
        print(f"Passed: {result['passed']}")
        if not result['passed']:
            print("Issues:")
            for issue in result['issues']:
                print(f" - {issue}")
