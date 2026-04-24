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


class News(TypedDict):
    category: str
    datetime: int
    headline: str
    id: int
    image: str
    related: str
    source: str
    summary: str
    url: str


def calculate_confidence_score(mcp_data: MCPData) -> dict:
    missing_financials_deduction = calculate_financial_deduction(mcp_data["financials"])

    (news_count_deduction, news_time_deduction) = calculate_news_deductions(
        mcp_data["news"]
    )
    price_history_deduction = calculate_price_history_deduction(
        mcp_data["price_history"]
    )

    score = (
        100
        + missing_financials_deduction
        + news_count_deduction
        + news_time_deduction
        + price_history_deduction
        + company_fields_deduction
    )
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
    """Returns MISSING_FINANCIALS_DEDUCTION if finances is empty, 0 otherwise."""
    if not finances:
        return MISSING_FINANCIALS_DEDUCTION
    return 0


def calculate_news_deductions(news: list[News]) -> tuple[int, int]:
    """
    Returns count and recency deductions for news data.

    Returns a tuple of (news_count_deduction, news_recency_deduction).
    Both deductions apply if news is empty. Uses Unix timestamps from
    Finnhub.
    """
    if not news:
        return (NEWS_COUNT_DEDUCTION, NEWS_RECENCY_DEDUCTION)

    news_count_deduction = NEWS_COUNT_DEDUCTION if len(news) < 3 else 0

    most_recent = max(datetime.fromtimestamp(article["datetime"]) for article in news)
    cutoff = datetime.today() - timedelta(days=14)
    news_time_deduction = NEWS_RECENCY_DEDUCTION if most_recent < cutoff else 0

    return (news_count_deduction, news_time_deduction)


def calculate_price_history_deduction(price_history: dict) -> int:
    """
    Returns PRICE_HISTORY_DEDUCTION if price history spans fewer than 90 days.

    Uses the Close key from the yfinance history dict. Dates are ISO strings,
    not Unix timestamps.
    """
    if not price_history:
        return PRICE_HISTORY_DEDUCTION

    close_dates = list(price_history.get("Close", {}).keys())

    if not close_dates:
        return PRICE_HISTORY_DEDUCTION

    earliest = datetime.fromisoformat(close_dates[0])
    latest = datetime.fromisoformat(close_dates[-1])
    days_of_data = (latest - earliest).days

    return PRICE_HISTORY_DEDUCTION if days_of_data < 90 else 0


def calculate_information_deductions(info: dict) -> int:
    """Returns MISSING_COMPANY_FIELDS_DEDUCTION if sector, industry, or marketCap are absent."""
    pass
