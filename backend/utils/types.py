from typing import TypedDict


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


class ConfidenceScore(TypedDict):
    score: int
    deductions: dict


class DeducedMCP(TypedDict):
    clean_data: MCPData
    confidence_score: ConfidenceScore
    issues: list


class ResearchPack(TypedDict):
    company_summary: str
    company_snapshot: dict
    financial_snapshot: dict
    price_movement: dict
    recent_news: list
    data_confidence: int
    flags: list
