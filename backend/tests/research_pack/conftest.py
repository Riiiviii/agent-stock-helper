import pytest


# ── Research Pack Data Fixtures ────────────────────────────────────────


@pytest.fixture
def valid_deduced_mcp(valid_mcp_data):
    from utils.confidence_calculator import calculate_confidence_score

    return calculate_confidence_score(valid_mcp_data)


# ── Research Pack Company Info Fixtures ────────────────────────────────────────


@pytest.fixture
def empty_company_info():
    return {}


# ── Research Pack Company Snapshot Fixtures ────────────────────────────────────────


@pytest.fixture
def invalid_company_info():
    return {
        "symbol": None,
        "shortName": None,
        "recommendationKey": None,
        "recommendationMean": None,
        "numberOfAnalystOpinions": None,
        "currentPrice": None,
        "fiftyTwoWeekLow": None,
        "fiftyTwoWeekHigh": None,
        "trailingPE": None,
        "forwardPE": None,
        "profitMargins": None,
        "revenueGrowth": None,
        "earningsGrowth": None,
        "beta": None,
        "sector": None,
        "industry": None,
        "marketCap": None,
    }


# ── Research Pack Financial Snapshot Fixtures ────────────────────────────────────────


@pytest.fixture
def empty_company_financials():
    return {}
