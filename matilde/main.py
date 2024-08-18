# matilde/main.py

import sys
import os
import sqlite3

# Ensure the parent directory is in the path so that 'audits' can be found
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from audits.internal_links.all_followable_pages_with_internal_links import AllFollowablePagesWithInternalLinksAudit
from audits.internal_links.pages_max_crawl_depth import PagesMaxCrawlDepthAudit
from audits.internal_links.no_follow_pages_without_internal_links import NoFollowPagesWithoutInternalLinksAudit
from audits.internal_links.no_redirected_pages_on_internal_links import NoRedirectedPagesOnInternalLinksAudit
from audits.internal_links.no_unavailable_pages_on_internal_links import NoUnavailablePagesOnInternalLinksAudit

from audits.robots.presence_of_robots_txt import PresenceOfRobotsTxtAudit
from audits.robots.sitemap_in_robots_txt import SitemapInRobotsTxtAudit

from audits.sitemaps.all_followable_pages_in_sitemaps import AllFollowablePagesInSitemapsAudit
from audits.sitemaps.no_follow_pages_not_in_sitemaps import NoFollowPagesNotInSitemapsAudit
from audits.sitemaps.no_redirected_pages_on_sitemaps import NoRedirectedPagesOnSitemapsAudit
from audits.sitemaps.no_unavailable_pages_on_sitemaps import NoUnavailablePagesOnSitemapsAudit

from malcom.metadata.architecture_metadata import ARCHITECTURE_METADATA

def run_audits(website, db_path="db_websites.db"):
    audits = [
        AllFollowablePagesWithInternalLinksAudit(db_path),
        PagesMaxCrawlDepthAudit(db_path),
        NoFollowPagesWithoutInternalLinksAudit(db_path),
        NoRedirectedPagesOnInternalLinksAudit(db_path),
        NoUnavailablePagesOnInternalLinksAudit(db_path),
        PresenceOfRobotsTxtAudit(),
        SitemapInRobotsTxtAudit(),
        AllFollowablePagesInSitemapsAudit(db_path),
        NoFollowPagesNotInSitemapsAudit(db_path),
        NoRedirectedPagesOnSitemapsAudit(db_path),
        NoUnavailablePagesOnSitemapsAudit(db_path),
    ]

    passed_audits = []
    failed_audits = {}

    for audit in audits:
        audit.run(website)
        if audit.get_result():
            passed_audits.append(audit.name)
        else:
            failed_audits[audit.name] = {
                "metadata": {
                    "name": audit.name,
                    "importance": audit.importance,
                    "measurement_criteria": audit.measurement_criteria,
                    "fix_methods": audit.fix_methods,
                    "use_cases": audit.use_cases,
                },
                "issues": audit.get_issues(),
            }

    found_pages = get_all_found_pages(db_path)

    return passed_audits, failed_audits, found_pages

def get_all_found_pages(db_path):
    """Fetch all pages found in the database."""
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT url FROM tb_pages")
        pages = cursor.fetchall()
        found_pages = [page[0] for page in pages]
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
        found_pages = []
    finally:
        cursor.close()
        connection.close()

    return found_pages

if __name__ == "__main__":
    # Example website data
    website_url = "https://example.com"
    
    passed, failed, found_pages = run_audits(website_url)
    
    print("Passed Audits:")
    for audit in passed:
        print(f" - {audit}")
    
    print("\nFailed Audits:")
    for audit, details in failed.items():
        print(f" - {audit}")
        print(f"   Importance: {details['metadata']['importance']}")
        print(f"   Measurement Criteria: {details['metadata']['measurement_criteria']}")
        print(f"   Fix Methods: {details['metadata']['fix_methods']}")
        print(f"   Use Cases: {details['metadata']['use_cases']}")
        print("   Issues:")
        for issue in details['issues']:
            print(f"     - {issue}")
    
    print("\nFound Pages:")
    for page in found_pages:
        print(f" - {page}")
