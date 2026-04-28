from .types import DeducedMCP, ResearchPack, News


def build_research_pack(data: DeducedMCP) -> ResearchPack:
    company_summary = get_company_summary(data["clean_data"]["company_information"])
    company_snapshot = get_company_snapshot(data["clean_data"]["company_information"])
    financial_snapshot = get_financial_snapshot(data["clean_data"]["financials"])
    price_movement = get_price_movement(data["clean_data"]["price_history"])
    recent_news = get_recent_news(data["clean_data"]["news"])

    return {
        "company_summary": company_summary,
        "company_snapshot": company_snapshot,
        "financial_snapshot": financial_snapshot,
        "price_movement": price_movement,
        "recent_news": recent_news,
        "data_confidence": data["confidence_score"]["score"],
        "flags": data["issues"],
    }


def get_company_summary(company_info: dict) -> str:
    return company_info.get("longBusinessSummary", "")


def get_company_snapshot(company_info: dict) -> dict:
    keys = [
        "symbol",
        "shortName",
        "recommendationKey",
        "recommendationMean",
        "numberOfAnalystOpinions",
        "currentPrice",
        "fiftyTwoWeekLow",
        "fiftyTwoWeekHigh",
        "trailingPE",
        "forwardPE",
        "profitMargins",
        "revenueGrowth",
        "earningsGrowth",
        "beta",
        "sector",
        "industry",
        "marketCap",
    ]
    return {k: company_info.get(k) for k in keys}


def get_financial_snapshot(company_financials: dict) -> dict:
    keys = [
        "Total Revenue",
        "Gross Profit",
        "Operating Income",
        "Net Income",
        "EBITDA",
        "Diluted EPS",
        "Research And Development",
        "Operating Expense",
    ]

    snapshot = {}
    sorted_years = sorted(company_financials.items(), reverse=True)

    for date, metrics in sorted_years:
        year_data = {key: metrics.get(key) for key in keys}
        values = list(year_data.values())
        has_data = False

        for value in values:
            if value is not None:
                has_data = True
                break

        if has_data:
            snapshot[date] = year_data

    return snapshot


def get_price_movement(company_price_movement: dict) -> dict:
    close_prices = company_price_movement["Close"]
    sorted_data = sorted(close_prices, reverse=True)
    current_price = close_prices[sorted_data[0]]
    price_30d_ago = close_prices[sorted_data[30]] if len(sorted_data) > 30 else None
    price_90d_ago = close_prices[sorted_data[90]] if len(sorted_data) > 90 else None
    change_30d_pct = (
        ((current_price - price_30d_ago) / price_30d_ago) * 100
        if price_30d_ago
        else None
    )
    change_90d_pct = (
        ((current_price - price_90d_ago) / price_90d_ago) * 100
        if price_90d_ago
        else None
    )
    year_high = max(close_prices.values())
    year_low = min(close_prices.values())

    return {
        "current_price": current_price,
        "price_30d_ago": price_30d_ago,
        "price_90d_ago": price_90d_ago,
        "change_30d_pct": change_30d_pct,
        "change_90d_pct": change_90d_pct,
        "year_high": year_high,
        "year_low": year_low,
    }


def get_recent_news(company_news: list[News]) -> list:
    sorted_news = sorted(
        company_news, key=lambda article: article["datetime"], reverse=True
    )
    return sorted_news[:15]
