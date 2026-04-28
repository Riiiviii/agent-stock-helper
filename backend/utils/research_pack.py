from .types import DeducedMCP, ResearchPack


def build_research_pack(data: DeducedMCP) -> ResearchPack:

    return {
        "company_summary": "",
        "company_snapshot": {},
        "financial_snapshot": {},
        "price_movement": {},
        "recent_news": [],
        "data_confidence": data["confidence_score"]["score"],
        "flags": data["issues"],
    }


def generate_company_summary(company_info: dict) -> str:
    return ""


def generate_company_snapshot(company_info: dict) -> dict:
    return {}


def generate_price_movement(company_price_movement: dict) -> dict:
    return {}


def refine_recent_news(company_news: list) -> list:
    return []
