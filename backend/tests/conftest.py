import pytest
import json
from pathlib import Path
from datetime import datetime, timezone


FIXTURES_DIR = Path(__file__).parent / "_fixtures"


# ── Shared JSON fixtures ────────────────────────────────────────


@pytest.fixture
def valid_company_info():
    with open(FIXTURES_DIR / "company_info.json") as f:
        return json.load(f)


@pytest.fixture
def valid_company_price_history():
    with open(FIXTURES_DIR / "price_history.json") as f:
        return json.load(f)


@pytest.fixture
def valid_company_news():
    with open(FIXTURES_DIR / "company_news.json") as f:
        news = json.load(f)
    now_ts = int(datetime.now(timezone.utc).timestamp())
    for i, article in enumerate(news):
        article["datetime"] = now_ts - (i * 3600)
    return news


@pytest.fixture
def valid_company_financials():
    with open(FIXTURES_DIR / "company_financials.json") as f:
        return json.load(f)


# ── Combined MCP fixture ────────────────────────────────────────


@pytest.fixture
def valid_mcp_data(
    valid_company_info,
    valid_company_financials,
    valid_company_news,
    valid_company_price_history,
):
    return {
        "company_information": valid_company_info,
        "news": valid_company_news,
        "financials": valid_company_financials,
        "price_history": valid_company_price_history,
    }
