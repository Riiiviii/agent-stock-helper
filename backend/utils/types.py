from enum import Enum
from typing import TypedDict

# ── Confidence Score Typing ────────────────────────────────────────


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


class CompanyInformation(TypedDict, total=False):
    long_business_summary: str
    symbol: str
    short_name: str
    recommendation_key: str
    recommendation_mean: float
    number_of_analyst_opinions: int
    current_price: float
    fifty_two_week_low: float
    fifty_two_week_high: float
    trailing_pe: float
    forward_pe: float
    profit_margins: float
    revenue_growth: float
    earnings_growth: float
    beta: float
    sector: str
    industry: str
    market_cap: int


Financials = dict[str, dict[str, float | None]]

PriceHistory = dict[str, dict[str, float | None]]


class AnalystRecommendation(TypedDict):
    period: str
    strong_buy: int
    buy: int
    hold: int
    sell: int
    strong_sell: int


class MCPData(TypedDict):
    company_information: CompanyInformation
    news: list[News]
    financials: Financials
    price_history: PriceHistory
    analyst_recommendations: list[AnalystRecommendation]


class DeductionDetail(TypedDict):
    missing_financials: int
    news_count_below_3: int
    news_older_than_14_days: int
    price_history_under_90_days: int
    missing_company_fields: int


class ConfidenceScore(TypedDict):
    score: int
    deductions: DeductionDetail


class Issue(TypedDict):
    reason: str
    description: str


# ── Research Pack Typing ────────────────────────────────────────


class DeducedMCP(TypedDict):
    clean_data: MCPData
    confidence_score: ConfidenceScore
    issues: list[Issue]


class CompanySnapshot(TypedDict):
    symbol: str | None
    short_name: str | None
    recommendation_key: str | None
    recommendation_mean: float | None
    number_of_analyst_opinions: int | None
    current_price: float | None
    fifty_two_week_low: float | None
    fifty_two_week_high: float | None
    trailing_pe: float | None
    forward_pe: float | None
    profit_margins: float | None
    revenue_growth: float | None
    earnings_growth: float | None
    target_mean_price: float | None
    target_high_price: float | None
    target_low_price: float | None
    beta: float | None
    sector: str | None
    industry: str | None
    market_cap: int | None


FinancialYearData = TypedDict(
    "FinancialYearData",
    {
        "Total Revenue": float | None,
        "Gross Profit": float | None,
        "Operating Income": float | None,
        "Net Income": float | None,
        "EBITDA": float | None,
        "Diluted EPS": float | None,
        "Research And Development": float | None,
        "Operating Expense": float | None,
    },
)

FinancialSnapshot = dict[str, FinancialYearData]


class PriceMovement(TypedDict):
    current_price: float | None
    price_30d_ago: float | None
    price_90d_ago: float | None
    change_30d_pct: float | None
    change_90d_pct: float | None
    year_high: float | None
    year_low: float | None


class ResearchPack(TypedDict):
    company_summary: str
    company_snapshot: CompanySnapshot
    financial_snapshot: FinancialSnapshot
    price_movement: PriceMovement
    recent_news: list[News]
    analyst_recommendations: list[AnalystRecommendation]
    data_confidence: int
    flags: list[Issue]


# ── Fundamental Agent Typing ────────────────────────────────────────


class ValuationSignals(TypedDict, total=False):
    trailing_pe: float | None
    forward_pe: float | None
    profit_margins: float | None
    earnings_growth: float | None
    revenue_growth: float | None
    market_cap: int | None


class AnalystConsensus(TypedDict, total=False):
    recommendation: str | None
    mean_score: float | None
    num_analyst: int | None
    price_target_mean: float | None
    price_target_high: float | None
    price_target_low: float | None


class FundamentalsOutput(TypedDict, total=False):
    revenue_trends: str
    profitability: str
    valuation_signals: ValuationSignals
    analyst_consensus: AnalystConsensus
    summary: str
    strength: int


# ── Sentiment Agent Typing ────────────────────────────────────────


class SentimentLabel(str, Enum):
    positive = "positive"
    neutral = "neutral"
    negative = "negative"
    mixed = "mixed"


class SentimentOutput(TypedDict):
    general_sentiment: SentimentLabel
    summary: str
    notable_events: list[News]
    strength: int
