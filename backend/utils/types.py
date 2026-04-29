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
    longBusinessSummary: str
    symbol: str
    shortName: str
    recommendationKey: str
    recommendationMean: float
    numberOfAnalystOpinions: int
    currentPrice: float
    fiftyTwoWeekLow: float
    fiftyTwoWeekHigh: float
    trailingPE: float
    forwardPE: float
    profitMargins: float
    revenueGrowth: float
    earningsGrowth: float
    beta: float
    sector: str
    industry: str
    marketCap: int


Financials = dict[str, dict[str, float | None]]

PriceHistory = dict[str, dict[str, float | None]]


class MCPData(TypedDict):
    company_information: CompanyInformation
    news: list[News]
    financials: Financials
    price_history: PriceHistory


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
    shortName: str | None
    recommendationKey: str | None
    recommendationMean: float | None
    numberOfAnalystOpinions: int | None
    currentPrice: float | None
    fiftyTwoWeekLow: float | None
    fiftyTwoWeekHigh: float | None
    trailingPE: float | None
    forwardPE: float | None
    profitMargins: float | None
    revenueGrowth: float | None
    earningsGrowth: float | None
    targetMeanPrice: float | None
    targetHighPrice: float | None
    targetLowPrice: float | None
    beta: float | None
    sector: str | None
    industry: str | None
    marketCap: int | None


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
