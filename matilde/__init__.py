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

__all__ = [
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
