import pytest
from pathlib import Path
from datetime import datetime

FIXTURES_DIR = Path(__file__).parent.parent / "_fixtures"

# ── Company Price History Fixtures ────────────────────────────────────────


@pytest.fixture
def empty_price_history():
    return {}


@pytest.fixture
def no_close_price_history():
    return {"Open": {"2026-01-01T00:00:00-05:00": 150.0}}


@pytest.fixture
def insufficient_price_history():
    return {
        "Close": {
            "2026-04-01T00:00:00-04:00": 270.0,
            "2026-04-23T00:00:00-04:00": 273.0,
        }
    }


# ── Company Information Fixtures ────────────────────────────────────────


@pytest.fixture
def empty_company_info():
    return {}


@pytest.fixture
def missing_fields_company_info():
    return {
        "address1": "One Apple Park Way",
        "city": "Cupertino",
        # sector, industry, marketCap deliberately absent
    }


# ── Company News Fixtures ────────────────────────────────────────


@pytest.fixture
def empty_news():
    return []


@pytest.fixture
def insufficient_company_news():
    return [
        {
            "datetime": int(datetime.now().timestamp()),
            "headline": "",
            "category": "",
            "id": 1,
            "image": "",
            "related": "",
            "source": "",
            "summary": "",
            "url": "",
        },
        {
            "datetime": int(datetime.now().timestamp()),
            "headline": "",
            "category": "",
            "id": 2,
            "image": "",
            "related": "",
            "source": "",
            "summary": "",
            "url": "",
        },
    ]


@pytest.fixture
def stale_company_news():
    return [
        {
            "datetime": 1609459200,
            "headline": "",
            "category": "",
            "id": 1,
            "image": "",
            "related": "",
            "source": "",
            "summary": "",
            "url": "",
        },
        {
            "datetime": 1609459200,
            "headline": "",
            "category": "",
            "id": 2,
            "image": "",
            "related": "",
            "source": "",
            "summary": "",
            "url": "",
        },
        {
            "datetime": 1609459200,
            "headline": "",
            "category": "",
            "id": 3,
            "image": "",
            "related": "",
            "source": "",
            "summary": "",
            "url": "",
        },
    ]


# ── Company Financial Fixtures ────────────────────────────────────────


@pytest.fixture
def empty_financials():
    return {}
