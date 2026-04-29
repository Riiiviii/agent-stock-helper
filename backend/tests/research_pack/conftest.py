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
        "targetMeanPrice": None,
        "targetHighPrice": None,
        "targetLowPrice": None,
        "beta": None,
        "sector": None,
        "industry": None,
        "marketCap": None,
    }


# ── Research Pack Financial Snapshot Fixtures ────────────────────────────────────────


@pytest.fixture
def empty_company_financials():
    return {}


# ── Research Pack Price History Fixtures ────────────────────────────────────────


@pytest.fixture
def empty_company_price_history():
    return {}


@pytest.fixture
def insufficient_price_history():
    return {
        "Close": {
            "2026-04-01T00:00:00-04:00": 270.0,
            "2026-04-23T00:00:00-04:00": 273.0,
        }
    }


# ── Research Pack News Fixtures ────────────────────────────────────────


@pytest.fixture
def less_than_15_news():
    return [
        {
            "category": "company",
            "datetime": 1777395120,
            "headline": "Apple's CEOs, Intel & AI, and Another SaaSpocalype",
            "id": 139918601,
            "image": "https://s.yimg.com/rz/stage/p/yahoo_finance_en-US_h_p_finance_2.png",
            "related": "AAPL",
            "source": "Yahoo",
            "summary": "Intel has such high demand from the AI market that it's selling chips it once thought were worthless.",
            "url": "https://finnhub.io/api/news?id=bd6df7daebf3de12e8d192c917b484e2ad71c64144ef903c58146f3c1001c622",
        }
    ]
