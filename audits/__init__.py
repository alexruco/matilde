# audits/__init__.py

from audits.internal_links import (
    AllFollowablePagesWithInternalLinksAudit,
    NoFollowPagesWithoutInternalLinksAudit,
    NoRedirectedPagesOnInternalLinksAudit,
    NoUnavailablePagesOnInternalLinksAudit,
    PagesMaxCrawlDepthAudit,    
)

from audits.robots import (
    PresenceOfRobotsTxtAudit,
    SitemapInRobotsTxtAudit,
)

from audits.sitemaps import (
    AllFollowablePagesInSitemapsAudit,
    NoFollowPagesNotInSitemapsAudit,
    NoRedirectedPagesOnSitemapsAudit,
    NoUnavailablePagesOnSitemapsAudit,
)

__all__ = [
    # Internal Links Audits
    "AllFollowablePagesWithInternalLinksAudit",
    "NoFollowPagesWithoutInternalLinksAudit",
    "NoRedirectedPagesOnInternalLinksAudit",
    "NoUnavailablePagesOnInternalLinksAudit",
    "PagesMaxCrawlDepthAudit",
    
    # Robots Audits
    "PresenceOfRobotsTxtAudit",
    "SitemapInRobotsTxtAudit",
    
    # Sitemaps Audits
    "AllFollowablePagesInSitemapsAudit",
    "NoFollowPagesNotInSitemapsAudit",
    "NoRedirectedPagesOnSitemapsAudit",
    "NoUnavailablePagesOnSitemapsAudit",
]
