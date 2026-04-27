import { ArrowRight } from "lucide-react";

interface AgentDescription {
  name: string;
  description: string;
}

interface ReportFeature {
  label: string;
  description: string;
}

const agents: AgentDescription[] = [
  {
    name: "Fundamentals Agent",
    description:
      "Analyses revenue trends, profitability margins, and valuation signals — P/E ratios, EBITDA, and analyst recommendations.",
  },
  {
    name: "Sentiment Agent",
    description:
      "Reads recent headlines to gauge news tone, volume, and the short-term narrative the market is forming around the company.",
  },
  {
    name: "Risk / Macro Agent",
    description:
      "Surfaces external threats — macro headwinds, regulatory exposure, industry-specific risks, and red flags in the data.",
  },
  {
    name: "Competitive Agent",
    description:
      "Maps likely competitive positioning using sector data and targeted news queries to identify rival signals and market threats.",
  },
];

const reportFeatures: ReportFeature[] = [
  {
    label: "Thesis strength",
    description:
      "A 0–100 score reflecting how strongly the four agents agree. Low scores surface genuine uncertainty — not a bug, a feature.",
  },
  {
    label: "Data confidence",
    description:
      "Calculated before any AI runs. Flags missing financials, stale news, or thin price history so you always know what the analysis is working with.",
  },
  {
    label: "Conflicting signals",
    description:
      "Where agents disagree is explicitly named. If Fundamentals says strong and Risk says fragile, you see both — not a smoothed average.",
  },
  {
    label: "Key tailwinds",
    description:
      "Specific catalysts drawn from the fundamental, sentiment, and competitive lenses — grounded in real data, not boilerplate.",
  },
  {
    label: "Key risks",
    description:
      "Non-obvious risks from the Risk/Macro and Competitive agents, anchored to recent news and financial figures.",
  },
  {
    label: "Time horizon",
    description:
      "Short, medium, or long-term framing from the Judge Agent, calibrated to the strength and recency of the evidence.",
  },
];

export default function AgentSummary() {
  return (
    <>
      <section className="py-24 bg-(--cream)">
        <div className="mx-auto max-w-4xl px-6">
          <div className="mb-14 text-center">
            <h2 className="font-mono text-xs tracking-widest text-(--green) uppercase mb-3">
              Under the hood
            </h2>
            <h3 className="font-serif font-bold text-4xl text-(--ink) mb-5">
              Not one AI. A panel of specialists.
            </h3>
            <p className="text-sm text-(--ink2) leading-relaxed max-w-xl mx-auto">
              Vestly runs four specialist agents in parallel, each with a
              distinct focus, then passes all four outputs to a Judge Agent that
              synthesises them into one structured thesis. Every analysis is
              grounded in live data from{" "}
              <strong className="text-(--ink)">yfinance</strong> and{" "}
              <strong className="text-(--ink)">Finnhub</strong>.
            </p>
          </div>

          <div className="flex items-stretch gap-0">
            {/* Left: agents */}
            <div className="flex-1 flex flex-col">
              {agents.map((agent) => (
                <div key={agent.name} className="py-5 border-t border-border">
                  <h4 className="font-semibold text-sm text-(--ink) mb-1.5">
                    {agent.name}
                  </h4>
                  <p className="text-sm text-(--ink2) leading-relaxed">
                    {agent.description}
                  </p>
                </div>
              ))}
              <div className="border-t border-border" />
            </div>

            {/* Bracket + arrow connector */}
            <div className="flex items-center mx-3">
              <div className="self-stretch w-4 border-r border-t border-b border-border rounded-r-lg" />
              <ArrowRight className="w-4 h-4 text-(--ink3) shrink-0" strokeWidth={1.5} />
            </div>

            {/* Right: Judge Agent */}
            <div className="w-56 bg-(--green) rounded-xl p-6 flex flex-col justify-center shrink-0">
              <p className="font-mono text-xs tracking-widest text-(--green-hero) uppercase mb-2">
                Synthesis
              </p>
              <h4 className="font-serif font-bold text-2xl text-white mb-3">
                Judge Agent
              </h4>
              <p className="text-sm text-white/70 leading-relaxed">
                Reads all four outputs, surfaces disagreements, and produces a
                structured thesis with a strength score, time horizon, and key
                risks.
              </p>
            </div>
          </div>
        </div>
      </section>

      <section className="py-20 bg-white">
        <div className="mx-auto max-w-3xl px-6">
          <div className="text-center mb-16">
            <h2 className="font-mono text-xs tracking-widest text-(--green) uppercase mb-4">
              Every report includes
            </h2>
            <h3 className="font-serif font-bold text-4xl text-(--ink) leading-tight">
              Structured reasoning,
              <br /> not a guess.
            </h3>
          </div>

          <div>
            {reportFeatures.map((feature) => (
              <div
                key={feature.label}
                className="flex gap-12 py-6 border-t border-border"
              >
                <h4 className="font-semibold text-sm text-(--ink) w-44 shrink-0">
                  {feature.label}
                </h4>
                <p className="text-sm text-(--ink2) leading-relaxed">
                  {feature.description}
                </p>
              </div>
            ))}
            <div className="border-t border-border" />
          </div>
        </div>
      </section>
    </>
  );
}
