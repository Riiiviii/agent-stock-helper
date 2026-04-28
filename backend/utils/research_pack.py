from .types import DeducedMCP, ResearchPack


def build_research_pack(data: DeducedMCP) -> ResearchPack:
    company_summary: str = get_company_summary(
        data["clean_data"]["company_information"]
    )

    return {
        "company_summary": company_summary,
        "company_snapshot": {},
        "financial_snapshot": {},
        "price_movement": {},
        "recent_news": [],
        "data_confidence": data["confidence_score"]["score"],
        "flags": data["issues"],
    }


def get_company_summary(company_info: dict) -> str:
    return company_info.get("longBusinessSummary", "")


def generate_company_snapshot(company_info: dict) -> dict:
    return {}


def generate_price_movement(company_price_movement: dict) -> dict:
    return {}


def refine_recent_news(company_news: list) -> list:
    return []
