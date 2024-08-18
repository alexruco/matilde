# matilde/main.py

import sys
import os

# Ensure the parent directory is in the path so that 'audits' can be found
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bertha import recrawl_website

#Internal Links audits imports
from audits.internal_links.all_followable_pages_with_internal_links import  AllFollowablePagesWithInternalLinksAudit
from audits.internal_links.no_follow_pages_without_internal_links import NoFollowPagesWithoutInternalLinksAudit
from audits.internal_links.no_redirected_pages_on_internal_links import NoRedirectedPagesOnInternalLinksAudit
from audits.internal_links.no_unavailable_pages_on_internal_links import NoUnavailablePagesOnInternalLinksAudit
from audits.internal_links.pages_max_crawl_depth import PagesMaxCrawlDepthAudit

#Sitempas audits imports
from audits.sitemaps.all_followable_pages_in_sitemaps import AllFollowablePagesInSitemapsAudit
from audits.sitemaps.no_follow_pages_not_in_sitemaps import NoFollowPagesNotInSitemapsAudit
from audits.sitemaps.no_redirected_pages_on_sitemaps import NoRedirectedPagesOnSitemapsAudit
from audits.sitemaps.no_unavailable_pages_on_sitemaps import NoUnavailablePagesOnSitemapsAudit

#Robots.txt audits imports
from audits.robots.presence_of_robots_txt import PresenceOfRobotsTxtAudit
from audits.robots.sitemap_in_robots_txt import SitemapInRobotsTxtAudit




def run_audits(website):
    
    pages_data = recrawl_website(website)
    
    audits = [
        
        AllFollowablePagesWithInternalLinksAudit("db_websites.db"),
        NoFollowPagesWithoutInternalLinksAudit("db_websites.db"),
        NoRedirectedPagesOnInternalLinksAudit("db_websites.db"),
        NoUnavailablePagesOnInternalLinksAudit("db_websites.db"),
        PagesMaxCrawlDepthAudit("db_websites.db"),
        
        #Sitemaps Audits
        AllFollowablePagesInSitemapsAudit("db_websites.db"),
        NoFollowPagesNotInSitemapsAudit("db_websites.db"),
        NoRedirectedPagesOnSitemapsAudit("db_websites.db"),
        NoFollowPagesNotInSitemapsAudit("db_websites.db"),
        NoUnavailablePagesOnSitemapsAudit("db_websites.db"),

        #Robots Audits
        PresenceOfRobotsTxtAudit(),        
        SitemapInRobotsTxtAudit(),
        
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
