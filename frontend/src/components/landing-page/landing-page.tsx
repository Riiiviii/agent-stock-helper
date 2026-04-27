import AgentsSummary from "./agents-summary";
import Hero from "./hero";
import ReportSummary from "./report-summary";
import WorkingSummary from "./working-summary";

export default function LandingPage() {
  return (
    <main>
      <Hero />
      <WorkingSummary />
      <AgentsSummary />
      <ReportSummary />
    </main>
  );
}
