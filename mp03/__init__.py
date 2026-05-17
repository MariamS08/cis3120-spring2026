"""MP03 supporting module — seeded data for the industry-comparison project.

This package provides the seeded ticker lists and search-phrase lists that
serve as starting points for Mini-Project MP03. Teams import these lists,
extend them, and document the rationale for any changes in the methodology
section of their submission.

Reference: docs/MP03_Assignment.docx, Section 3.
"""

from mp03.seeds import (
    FINANCIAL_SERVICES_TICKERS,
    FINANCIAL_SERVICES_PHRASES,
    TRAVEL_HOSPITALITY_TICKERS,
    TRAVEL_HOSPITALITY_PHRASES,
)

__all__ = [
    "FINANCIAL_SERVICES_TICKERS",
    "FINANCIAL_SERVICES_PHRASES",
    "TRAVEL_HOSPITALITY_TICKERS",
    "TRAVEL_HOSPITALITY_PHRASES",
]
