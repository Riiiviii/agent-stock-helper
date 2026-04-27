import Hero from "./hero";
import AgentSummary from "./report-summary";
import WorkingSummary from "./working-summary";

export default function LandingPage() {
  return (
    <div>
      <Hero />
      <WorkingSummary />
      <AgentSummary />
    </div>
  );
}
