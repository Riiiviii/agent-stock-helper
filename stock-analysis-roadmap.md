# Stock Analysis Agent — Build Roadmap

## Phase 1 — Foundations + MCP Setup

### Goal

Get real data flowing end-to-end via MCP tools with zero agents.

### Tasks

**1. Set up backend**

- FastAPI project
- Basic route: `GET /analyze?ticker=AAPL`

**2. Build MCP servers (do this before touching agents)**

Wrap both data sources as MCP servers. This is the right time — retrofitting later is painful.

- `yfinance-mcp` — exposes tools: `get_company_information`, `get_company_financials`, `get_price_history`, `get_analyst_recommendations`, `get_insider_transactions`
- `finnhub-mcp` — exposes tools: `get_company_news`

Your agents will call these tools via the OpenAI SDK MCP integration, not call the APIs directly.

**3. Verify raw data through MCP tools**

```json
{
  "company_info": {...},
  "financials": {...},
  "price_data": {...},
  "news": [...]
}
```

**4. Sanity check**

- Try 3–5 tickers
- Confirm news returns results and timestamps are recent
- Confirm financials aren't empty for large-cap stocks
- Note any tickers that behave badly — you'll need edge case handling later

### Exit Criteria

- `GET /analyze?ticker=AAPL` returns usable raw data
- Data is flowing through MCP tools, not direct API calls
- You can articulate why each MCP tool exists

> If this isn't solid, everything else collapses.

### Status: ✅ Complete

---

## Phase 2 — Data Integrity Layer

### Goal

Turn messy data into trusted structured input using deterministic rules — no LLM.

### Tasks

**1. Define schema**

```json
{
  "clean_data": {...},
  "confidence_score": {
    "score": 0-100,
    "deductions": {
      "missing_financials": 0,
      "news_count_below_3": 0,
      "news_older_than_14_days": 0,
      "price_history_under_90_days": 0,
      "missing_company_fields": 0
    }
  },
  "issues": []
}
```

**2. Implement deterministic scoring**

Confidence score is rule-based, not LLM-generated. Start at 100 and deduct:

```json
{
  "missing_financials": -20,
  "news_count_below_3": -10,
  "news_older_than_14_days": -8,
  "price_history_under_90_days": -15,
  "missing_company_fields": -15
}
```

Every deduction rule is defined upfront and auditable. The score never blocks the pipeline — it flows through as a signal that the Judge Agent uses to calibrate confidence in its output.

**3. Write tests**

All deduction rules must have passing unit tests before moving on.

> Don't rely on LLM judgment for data validation. Rules are faster, cheaper, and auditable.

### Exit Criteria

- Clean structured data
- Confidence score with clear deduction breakdown
- Issues list that catches real problems
- 14 passing unit tests

### Status: ✅ Complete

---

## Phase 3 — Research Pack

### Goal

Create a stable contract between pipeline stages.

### Task

Transform validated data into a single object passed to all downstream agents:

```json
{
  "company_summary": "...",
  "financial_snapshot": {...},
  "price_movement": {...},
  "recent_news": [...],
  "data_confidence": 0-100,
  "flags": []
}
```

> This is not optional. Without it your agents become inconsistent and hard to debug.

### Exit Criteria

- Single clean object that every downstream agent receives
- No agent fetches its own data after this point

### Status: ✅ Complete

---

## Phase 4 — Panel Agents

### Goal

Parallel, specialised reasoning from four distinct lenses.

Build ONE agent at a time. Do not parallelize development.

### 4.1 Fundamentals Agent

- Revenue trends
- Profitability
- Valuation signals (P/E, margins)

**Data source:** financial_snapshot from research pack + `get_analyst_recommendations` via MCP

### 4.2 Sentiment Agent

- News tone and volume
- Short-term narrative (what's the market talking about)
- Any major recent events

**Data source:** recent_news from research pack

### 4.3 Risk/Macro Agent

- External risks (interest rates, regulation, macro environment)
- Industry-specific exposure
- Any red flags in the data

**Data source:** financial_snapshot + recent_news + flags

### 4.4 Competitive Agent

> **Note:** yfinance and Finnhub don't provide competitive data directly. This agent reasons from what it knows — it uses the company summary and financial snapshot to identify likely competitors and positioning, and uses the Finnhub news tool (via MCP) to pull any recent news mentioning competitors by name. Be honest about this limitation in your README.

- Likely competitive landscape based on sector/industry
- Relative positioning signals from news
- Obvious threats or advantages

**Data source:** company_summary + financial_snapshot + targeted Finnhub news queries via MCP

### Critical Rule

Each agent must:

- Have a distinct focus that doesn't overlap with others
- Produce structured output (not free-form prose)
- Reference only its designated data sources

If two agents sound the same → your prompts are wrong. Tighten the schemas.

### Exit Criteria

For one ticker, you get 4 clearly different perspectives with non-overlapping insights.

### Status: ⏳ Pending

---

## Phase 5 — Judge Agent

### Goal

Synthesise multiple perspectives into one coherent, structured thesis.

### Tasks

**1. Define strict output schema**

```json
{
  "company": "...",
  "thesis_strength": 0-100,
  "confidence": 0-100,
  "time_horizon": "short/medium/long",
  "key_tailwinds": [],
  "key_risks": [],
  "conflicting_signals": [],
  "data_gaps": [],
  "final_summary": "..."
}
```

**2. Force reasoning quality**

- Must explicitly reference each panel agent's output
- Must surface disagreements between agents
- Must acknowledge uncertainty — a confident output with low data quality is a bug, not a feature
- `thesis_strength` should be lower when agents disagree significantly
- Run at `temperature=0` for consistency

> The judge cannot say "buy" or "sell." It produces a structured reasoning output. That's a feature, not a limitation.

### Exit Criteria

- Output is structured, readable, and non-generic
- Conflicting signals are explicitly called out
- You can explain every field to an interviewer

### Status: ⏳ Pending

---

## Phase 6 — Orchestration

### Goal

Wire everything together into a reliable, observable pipeline.

### Flow

```
fetch (MCP) → validate → research pack → panel agents (parallel) → judge
```

### Tasks

- Parallel panel execution with `asyncio`
- Structured error handling at each stage (don't let one agent failure kill the run)
- Structured logging at every stage with a `run_id`:

```json
{
  "run_id": "...",
  "ticker": "AAPL",
  "stage": "fundamentals_agent",
  "output": {...},
  "timestamp": "..."
}
```

- Timeout handling on MCP tool calls

### Exit Criteria

- One API call runs the full pipeline reliably
- Individual stage failures are caught and logged, not silently swallowed

### Status: ⏳ Pending

---

## Phase 7 — Auth + Persistence

### Goal

Make the tool usable across sessions with per-user history.

### Auth

Use **Clerk** or **Supabase Auth**. Do not build auth from scratch — it doesn't demonstrate AI engineering skills and will take a week you don't have. Drop it in and move on.

### Database

**Neon (Postgres)** with **SQLAlchemy** + **asyncpg**.

### Store

- User ID (from auth)
- Ticker
- Timestamp
- Final judge output (JSON)
- Optionally: intermediate panel outputs for debugging

### Exit Criteria

- Users can log in
- Past analyses are tied to their account
- History is retrievable via a `/history` endpoint

### Status: ⏳ Pending

---

## Phase 8 — Minimal Frontend

### Goal

View results. Nothing more.

### Features

- Ticker input
- Trigger analysis
- Display: summary, risks, tailwinds, confidence score, conflicting signals
- Analysis history per user

> No design obsession. Have AI generate the UI. Your time is in the backend.

### Exit Criteria

- A non-technical person could use this without explanation
- History is visible and navigable

### Status: ⏳ Pending

---

## Phase 9 — Deployment

### Goal

Get a public URL. A project that only runs locally is significantly weaker as a portfolio piece.

### Tasks

- Deploy FastAPI backend to **Railway** or **Render**
- Deploy frontend to **Vercel**
- Connect Neon — your connection string works as-is in both platforms
- Set environment variables
- Smoke test the full pipeline on the deployed version

### Exit Criteria

- Public URL that anyone can visit
- Full pipeline runs end-to-end on the deployed version
- URL goes in your README and portfolio

### Status: ⏳ Pending

---

## Phase 10 — Evaluation Layer ⭐ High Value

### Goal

Prove your system produces meaningfully better output than a naive approach.

### Tasks

**1. Define a baseline**

Single prompt to a plain LLM:

> "Analyse [TICKER] as an investment. What are the key risks and opportunities?"

**2. Run structured comparison**

Pick 5 tickers. For each, run both your system and the baseline. Score both on this rubric:

| Dimension                   | Score 0-3                                           | Notes |
| --------------------------- | --------------------------------------------------- | ----- |
| Specificity                 | Does it reference actual figures, not generalities? |       |
| Risk awareness              | Does it surface non-obvious risks?                  |       |
| Consistency                 | Would it give the same answer twice?                |       |
| Uncertainty acknowledgement | Does it flag what it doesn't know?                  |       |
| Structure                   | Is the output actionable and readable?              |       |

**3. Add a consistency test**

Run your system twice on the same ticker. Compare `thesis_strength` scores, `key_risks` lists, and `final_summary`. Document any meaningful divergence — this signals you understand LLM non-determinism.

**4. Document results honestly in the README**

### Exit Criteria

- You can say with evidence: "My system produces more structured and risk-aware outputs than a single-prompt baseline"
- Results are documented in the README

### Status: ⏳ Pending

---

## Phase 11 — Polish

- Tighten prompts based on real outputs you've seen
- Improve schemas where agents are still producing vague outputs
- Edge case handling: tickers with no news, very small companies, delisted stocks
- README: architecture diagram, tech stack, eval results, public URL

### Status: ⏳ Pending

---

## Biggest Risks

**1. Agent outputs become generic**
Fix: tighten schemas, force each agent to reference specific figures from the research pack

**2. Competitive agent is too vague**
Fix: scope it explicitly to news-based evidence + known sector positioning. Don't promise what the data can't support.

**3. You stall on frontend**
Fix: have AI generate the entire UI. Your value is in the backend.

**4. Auth becomes a rabbit hole**
Fix: Clerk or Supabase Auth only. One afternoon maximum.

**5. You skip deployment**
Fix: it's not optional. A private repo with no public URL is not a portfolio piece.

---

## Final Check

If you finish this, you will have:

- A real deployed system with a public URL
- Demonstrated MCP integration with justified architecture
- Multi-agent orchestration with a non-trivial panel + judge pattern
- Structured evaluation methodology you can defend
- Per-user persistence with auth

If you half-build it, it becomes another AI project with no depth.
