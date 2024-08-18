# audits/__init__.py

from .internal_links import (
    AllFollowablePagesWithInternalLinksAudit,
    NoFollowPagesWithoutInternalLinksAudit,
    NoRedirectedPagesOnInternalLinksAudit,
    NoUnavailablePagesOnInternalLinksAudit,
    PagesMaxCrawlDepthAudit,    
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
