import json
import pytest
from pathlib import Path
from datetime import datetime

FIXTURES_DIR = Path(__file__).parent / "fixtures"

#######################################################################################
#                      COMPANY PRICE HISTORY FIXTURE DECLARATIONS                     #
#######################################################################################


@pytest.fixture
def valid_company_price_history():
    with open(FIXTURES_DIR / "price_history.json") as f:
        return json.load(f)


@pytest.fixture
def empty_price_history():
    return {}


#######################################################################################
#                          COMPANY INFO FIXTURE DECLARATIONS                          #
#######################################################################################


@pytest.fixture
def valid_company_info():
    with open(FIXTURES_DIR / "company_info.json") as f:
        return json.load(f)


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


#######################################################################################
#                          COMPANY NEWS FIXTURE DECLARATIONS                          #
#######################################################################################


@pytest.fixture
def valid_company_news():
    with open(FIXTURES_DIR / "company_news.json") as f:
        return json.load(f)


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


#######################################################################################
#                       COMPANY FINANCIALS FIXTURE DECLARATIONS                       #
#######################################################################################


@pytest.fixture
def valid_company_financials():
    with open(FIXTURES_DIR / "company_financials.json") as f:
        return json.load(f)


@pytest.fixture
def empty_financials():
    return {}


#######################################################################################
#                          COMBINED MCP DATA FIXTURE                                  #
#######################################################################################


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
