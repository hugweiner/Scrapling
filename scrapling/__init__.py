"""Scrapling - A powerful, flexible web scraping library.

Scrapling provides an easy-to-use interface for web scraping with support
for both static and dynamic content, smart element selection, and
automatic adaptation to website changes.

Personal fork notes:
- Using this for learning purposes and personal scraping projects.
- See upstream: https://github.com/D4Vinci/Scrapling
- Added convenience alias: `Page` as shorthand for `Adaptor`.
- Added convenience alias: `AsyncPage` as shorthand for `AsyncFetcher`.
- Added convenience alias: `PWFetcher` as shorthand for `PlayWrightFetcher`.
- Added convenience alias: `Stealthy` as shorthand for `StealthyFetcher`.
"""

__version__ = "0.2.9"
__author__ = "D4Vinci"
__license__ = "MIT"

from scrapling.core.fetchers import (
    Fetcher,
    AsyncFetcher,
    PlayWrightFetcher,
    StealthyFetcher,
)
from scrapling.core.page import Adaptor, WebPage
from scrapling.core.custom_types import (
    AttributesHandler,
    NavigationWarning,
    SimilarElementsHandler,
    TextHandler,
)

# Personal convenience aliases - I keep mixing up the class names
Page = Adaptor
AsyncPage = AsyncFetcher
PWFetcher = PlayWrightFetcher  # PlayWrightFetcher is a mouthful
Stealthy = StealthyFetcher    # StealthyFetcher is also a mouthful

__all__ = [
    # Core fetchers
    "Fetcher",
    "AsyncFetcher",
    "PlayWrightFetcher",
    "StealthyFetcher",
    # Page/Adaptor classes
    "Adaptor",
    "Page",  # convenience alias for Adaptor
    "WebPage",
    # Fetcher aliases
    "AsyncPage",  # convenience alias for AsyncFetcher
    "PWFetcher",  # convenience alias for PlayWrightFetcher
    "Stealthy",   # convenience alias for StealthyFetcher
    # Custom types
    "AttributesHandler",
    "NavigationWarning",
    "SimilarElementsHandler",
    "TextHandler",
    # Metadata
    "__version__",
    "__author__",
    "__license__",
]
