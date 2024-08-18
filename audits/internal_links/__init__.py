from .all_followable_pages_with_internal_links import AllFollowablePagesWithInternalLinksAudit
from .no_follow_pages_without_internal_links import NoFollowPagesWithoutInternalLinksAudit
from .no_redirected_pages_on_internal_links import NoRedirectedPagesOnInternalLinksAudit
from .no_unavailable_pages_on_internal_links import NoUnavailablePagesOnInternalLinksAudit
from .pages_max_crawl_depth import PagesMaxCrawlDepthAudit


__all__ = [
    "AllFollowablePagesWithInternalLinksAudit",
    "NoFollowPagesWithoutInternalLinksAudit",
    "NoRedirectedPagesOnInternalLinksAudit",
    "NoUnavailablePagesOnInternalLinksAudit",
    "PagesMaxCrawlDepthAudit",
]
