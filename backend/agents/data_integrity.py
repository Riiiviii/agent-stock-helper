from typing import TypedDict
from datetime import datetime, timedelta
from typing import Final

NEWS_COUNT_DEDUCTION: Final = -10
NEWS_RECENCY_DEDUCTION: Final = -8
MISSING_FINANCIALS_DEDUCTION: Final = -20
PRICE_HISTORY_DEDUCTION: Final = -15
MISSING_COMPANY_FIELDS_DEDUCTION: Final = -15


class MCPData(TypedDict):
    company_information: dict
    news: list
    financials: dict
    price_history: dict


def calculate_confidence_score(mcp_data: MCPData) -> dict:
    return {
        "clean_data": {
            "company_information": mcp_data["company_information"],
            "news": mcp_data["news"],
            "financials": mcp_data["financials"],
            "price_history": mcp_data["price_history"],
        },
        "confidence_score": {
            "score": score,
            "deductions": {
                "missing_financials": missing_financials_deduction,
                "news_count_below_3": news_count_deduction,
                "news_older_than_14_days": news_time_deduction,
                "price_history_under_90_days": price_history_deduction,
                "missing_company_fields": company_fields_deduction,
            },
        },
        "issues": [],
    }


def calculate_financial_deduction(finances: dict) -> int:
    pass


def calculate_news_deductions(news: list[News]) -> tuple[int, int]:
    pass


def calculate_price_history_deductions(history: dict) -> int:
    pass


def calculate_information_deductions(info: dict) -> int:
    pass
