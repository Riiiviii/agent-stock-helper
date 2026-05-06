from typing import Literal
from pydantic import BaseModel, Field, ConfigDict

MODEL_CONFIG: ConfigDict = {"extra": "forbid"}

Severity = Literal["low", "medium", "high"]
EvidenceSource = Literal[
    "financial_snapshot",
    "company_snapshot",
    "recent_news",
    "flags",
    "price_movement",
    "company_summary",
]

# ── Confidence Score Typing ────────────────────────────────────────


class News(BaseModel):
    model_config = MODEL_CONFIG

    category: str
    datetime: int
    headline: str
    id: int
    image: str
    related: str
    source: str
    summary: str
    url: str


class CompanyInformation(BaseModel):
    model_config = ConfigDict(extra="ignore")

    long_business_summary: str | None = None
    symbol: str | None = None
    short_name: str | None = None
    recommendation_key: str | None = None
    recommendation_mean: float | None = None
    number_of_analyst_opinions: int | None = None
    current_price: float | None = None
    fifty_two_week_low: float | None = None
    fifty_two_week_high: float | None = None
    trailing_pe: float | None = None
    forward_pe: float | None = None
    profit_margins: float | None = None
    revenue_growth: float | None = None
    earnings_growth: float | None = None
    target_mean_price: float | None = None
    target_high_price: float | None = None
    target_low_price: float | None = None
    beta: float | None = None
    sector: str | None = None
    industry: str | None = None
    market_cap: int | None = None


class FinancialYearData(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    total_revenue: float | None = Field(None, alias="Total Revenue")
    gross_profit: float | None = Field(None, alias="Gross Profit")
    operating_income: float | None = Field(None, alias="Operating Income")
    net_income: float | None = Field(None, alias="Net Income")
    ebitda: float | None = Field(None, alias="EBITDA")
    diluted_eps: float | None = Field(None, alias="Diluted EPS")
    research_and_development: float | None = Field(
        None, alias="Research And Development"
    )
    operating_expense: float | None = Field(None, alias="Operating Expense")


class AnalystRecommendation(BaseModel):
    model_config = MODEL_CONFIG

    period: str
    strong_buy: int
    buy: int
    hold: int
    sell: int
    strong_sell: int


PriceHistory = dict[str, dict[str, float | None]]
Financials = dict[str, FinancialYearData]


class MCPData(BaseModel):
    model_config = MODEL_CONFIG

    company_information: CompanyInformation
    news: list[News]
    financials: Financials
    price_history: PriceHistory
    analyst_recommendations: list[AnalystRecommendation]


class DeductionDetail(BaseModel):
    model_config = MODEL_CONFIG

    missing_financials: int
    news_count_below_3: int
    news_older_than_14_days: int
    price_history_under_90_days: int
    missing_company_fields: int


class ConfidenceScore(BaseModel):
    model_config = MODEL_CONFIG

    score: int
    deductions: DeductionDetail


class Issue(BaseModel):
    model_config = MODEL_CONFIG

    reason: str
    description: str


# ── Research Pack Typing ────────────────────────────────────────


class DeducedMCP(BaseModel):
    model_config = MODEL_CONFIG

    clean_data: MCPData
    confidence_score: ConfidenceScore
    issues: list[Issue]


class CompanySnapshot(BaseModel):
    model_config = MODEL_CONFIG

    symbol: str | None = None
    short_name: str | None = None
    recommendation_key: str | None = None
    recommendation_mean: float | None = None
    number_of_analyst_opinions: int | None = None
    current_price: float | None = None
    fifty_two_week_low: float | None = None
    fifty_two_week_high: float | None = None
    trailing_pe: float | None = None
    forward_pe: float | None = None
    profit_margins: float | None = None
    revenue_growth: float | None = None
    earnings_growth: float | None = None
    target_mean_price: float | None = None
    target_high_price: float | None = None
    target_low_price: float | None = None
    beta: float | None = None
    sector: str | None = None
    industry: str | None = None
    market_cap: int | None = None


class PriceMovement(BaseModel):
    model_config = MODEL_CONFIG

    current_price: float | None = None
    price_30d_ago: float | None = None
    price_90d_ago: float | None = None
    change_30d_pct: float | None = None
    change_90d_pct: float | None = None
    year_high: float | None = None
    year_low: float | None = None


FinancialSnapshot = dict[str, FinancialYearData]


class ResearchPack(BaseModel):
    model_config = MODEL_CONFIG

    company_summary: str
    company_snapshot: CompanySnapshot
    financial_snapshot: FinancialSnapshot
    price_movement: PriceMovement
    recent_news: list[News]
    analyst_recommendations: list[AnalystRecommendation]
    data_confidence: int
    flags: list[Issue]


# ── Fundamental Agent Typing ────────────────────────────────────────


class ValuationSignals(BaseModel):
    model_config = MODEL_CONFIG

    trailing_pe: float | None = None
    forward_pe: float | None = None
    profit_margins: float | None = None
    earnings_growth: float | None = None
    revenue_growth: float | None = None
    market_cap: int | None = None


class AnalystConsensus(BaseModel):
    model_config = MODEL_CONFIG

    recommendation: str | None = None
    mean_score: float | None = None
    num_analyst: int | None = None
    price_target_mean: float | None = None
    price_target_high: float | None = None
    price_target_low: float | None = None


class FundamentalsOutput(BaseModel):
    model_config = MODEL_CONFIG

    revenue_trends: str = Field(min_length=1)
    profitability: str = Field(min_length=1)
    valuation_signals: ValuationSignals
    analyst_consensus: AnalystConsensus
    summary: str = Field(min_length=1)
    strength: int = Field(ge=0, le=100)


# ── Sentiment Agent Typing ────────────────────────────────────────


class SentimentOutput(BaseModel):
    model_config = MODEL_CONFIG

    general_sentiment: Literal["positive", "neutral", "negative", "mixed"]
    summary: str = Field(min_length=1)
    notable_events: list[News]
    strength: int = Field(ge=0, le=100)


# ── Risk Agent Typing ────────────────────────────────────────


class DownsideScenario(BaseModel):
    model_config = MODEL_CONFIG

    scenario: str = Field(min_length=1)
    trigger: str = Field(min_length=1)
    evidence: str = Field(min_length=1)
    evidence_source: EvidenceSource
    severity: Severity


class ConcentrationRisk(BaseModel):
    model_config = MODEL_CONFIG

    risk: str = Field(min_length=1)
    evidence: str = Field(min_length=1)
    evidence_source: EvidenceSource
    severity: Severity


class BalanceSheetConcern(BaseModel):
    model_config = MODEL_CONFIG

    concern: str = Field(min_length=1)
    metric: str = Field(min_length=1)
    metric_value: float | None = None
    stress_implication: str = Field(min_length=1)
    severity: Severity


class RiskOutput(BaseModel):
    model_config = MODEL_CONFIG

    downside_scenarios: list[DownsideScenario]
    concentration_risks: list[ConcentrationRisk]
    balance_sheet_concerns: list[BalanceSheetConcern]
    data_layer_red_flags: list[str]
    thesis_breakers: list[str]
    data_limitations: list[str]
    summary: str = Field(min_length=1)
    strength: int = Field(ge=0, le=100)
