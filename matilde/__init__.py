# audits/__init__.py

from .internal_links import (
    AllFollowablePagesWithInternalLinksAudit,
    PagesMaxCrawlDepthAudit,
    NoFollowPagesWithoutInternalLinksAudit,
    NoRedirectedPagesOnInternalLinksAudit,
    NoUnavailablePagesOnInternalLinksAudit,
)

from .robots import (
    PresenceOfRobotsTxtAudit,
    SitemapInRobotsTxtAudit,
)

from .sitemaps import (
    AllFollowablePagesInSitemapsAudit,
    NoFollowPagesNotInSitemapsAudit,
    NoRedirectedPagesOnSitemapsAudit,
    NoUnavailablePagesOnSitemapsAudit,
)

from .utils import(
    cleanup_database,
    get_all_found_pages
)
__all__ = [
    
    #utils
    "cleanup_database",
    "get_all_found_pages",
    
    # Internal Links Audits
    "AllFollowablePagesWithInternalLinksAudit",
    "PagesMaxCrawlDepthAudit",
    "NoFollowPagesWithoutInternalLinksAudit",
    "NoRedirectedPagesOnInternalLinksAudit",
    "NoUnavailablePagesOnInternalLinksAudit",
    
    # Robots Audits
    "PresenceOfRobotsTxtAudit",
    "SitemapInRobotsTxtAudit",
    
    # Sitemaps Audits
    "AllFollowablePagesInSitemapsAudit",
    "NoFollowPagesNotInSitemapsAudit",
    "NoRedirectedPagesOnSitemapsAudit",
    "NoUnavailablePagesOnSitemapsAudit",
]
