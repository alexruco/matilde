# matilde/main.py

import sys
import os

# Ensure the parent directory is in the path so that 'audits' can be found
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from audits.robots.presence_of_robots_txt import PresenceOfRobotsTxtAudit
from audits.robots.sitemap_in_robots_txt import SitemapInRobotsTxtAudit
from audits.internal_links.all_followable_pages_with_internal_links import  FollowablePagesWithInternalLinksAudit
from audits.sitemaps.all_followable_pages_in_sitemaps import AllFollowablePagesInSitemapAudit
from audits.internal_links.pages_max_crawl_depth import FollowablePagesMaxCrawlDepthAudit
from audits.sitemaps.no_follow_pages_not_in_sitemaps import NoFollowPagesNotInSitemapsAudit
from audits.internal_links.pages_max_crawl_depth import FollowablePagesMaxCrawlDepthAudit
from audits.internal_links.no_follow_pages_without_internal_links import NoFollowPagesWithoutInternalLinksAudit
from audits.sitemaps.no_unavailable_pages_on_sitemaps import NoUnavailablePagesOnSitemapsAudit
from audits.internal_links.no_unavailable_pages_on_internal_links import NoUnavailablePagesOnInternalLinksAudit
from bertha import recrawl_website



def run_audits(website):
    
    pages_data = recrawl_website(website)
    
    audits = [
        
        AllFollowablePagesInSitemapAudit("db_websites.db"),
        
        FollowablePagesMaxCrawlDepthAudit("db_websites.db"),
        
        FollowablePagesWithInternalLinksAudit("db_websites.db"),
        
        NoFollowPagesNotInSitemapsAudit("db_websites.db"),

        NoFollowPagesWithoutInternalLinksAudit("db_websites.db"),

        NoFollowPagesNotInSitemapsAudit("db_websites.db"),
        
        PresenceOfRobotsTxtAudit(),
        
        SitemapInRobotsTxtAudit(),
        
        NoUnavailablePagesOnSitemapsAudit("db_websites.db"),
        
        NoUnavailablePagesOnInternalLinksAudit("db_websites.db"),
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
    website_url = "https://orca.ricarela.com"  # This URL will be used by the dourado package
    
    results = run_audits(website_url)

    
    for audit_name, result in results.items():
        print(f"Audit: {audit_name}")
        print(f"Passed: {result['passed']}")
        if not result['passed']:
            print("Issues:")
            for issue in result['issues']:
                print(f" - {issue}")
