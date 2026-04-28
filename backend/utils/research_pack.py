from .types import DeducedMCP, ResearchPack


def build_research_pack(data: DeducedMCP) -> ResearchPack:
    company_summary: str = get_company_summary(
        data["clean_data"]["company_information"]
    )

    company_snapshot: dict = get_company_snapshot(
        data["clean_data"]["company_information"]
    )

    return {
        "company_summary": company_summary,
        "company_snapshot": company_snapshot,
        "financial_snapshot": {},
        "price_movement": {},
        "recent_news": [],
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


def generate_financial_snapshot(company_financials: dict) -> dict:
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


def generate_price_movement(company_price_movement: dict) -> dict:
    return {}


def refine_recent_news(company_news: list) -> list:
    return []
