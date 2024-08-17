# matilde/audits/__init__.py

"""
This package contains all the individual audits for the Matilde website architecture audit tool.
Each module in this package implements a specific audit by extending the AuditBase class from Malcom.
"""

from audits.presence_of_robots_txt import PresenceOfRobotsTxtAudit
'''from .sitemap_in_robots_txt import SitemapInRobotsTxtAudit
from .all_followable_pages_in_sitemap import AllFollowablePagesInSitemapAudit
from .followable_pages_with_internal_links import FollowablePagesWithInternalLinksAudit
from .no_follow_pages_without_internal_links import NoFollowPagesWithoutInternalLinksAudit
from .no_follow_pages_not_in_sitemaps import NoFollowPagesNotInSitemapsAudit
from .followable_pages_max_crawl_depth import FollowablePagesMaxCrawlDepthAudit
'''
__all__ = [
    "PresenceOfRobotsTxtAudit",
    '''
    "SitemapInRobotsTxtAudit",
    "AllFollowablePagesInSitemapAudit",
    "FollowablePagesWithInternalLinksAudit",
    "NoFollowPagesWithoutInternalLinksAudit",
    "NoFollowPagesNotInSitemapsAudit",
    "FollowablePagesMaxCrawlDepthAudit"
    '''
]
