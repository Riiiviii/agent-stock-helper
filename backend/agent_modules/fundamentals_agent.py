from utils.types import ResearchPack, FundamentalsOutput
from typing import Final
from pathlib import Path
from agents import Agent, Runner, trace
from dotenv import load_dotenv
import json

load_dotenv(override=True)

REQUIRED_KEYS: Final[set[str]] = {
    "revenue_trends",
    "profitability",
    "valuation_signals",
    "analyst_consensus",
    "summary",
    "strength",
}


class FundamentalsAgent:
    MODEL: Final = "gpt-4o-mini"
    INSTRUCTION: Final[str] = (
        Path(__file__).parent / "prompts" / "fundamentals_agent.txt"
    ).read_text()

    async def run(self, research_pack: ResearchPack) -> FundamentalsOutput:

        data = research_pack.model_dump_json()

        agent = Agent(
            name="fundamentals-analysis-agent",
            instructions=self.INSTRUCTION,
            model=self.MODEL,
        )

        with trace("Fundamental Agent"):
            result = await Runner.run(agent, data)
            return self._parse_result(result.final_output)

    def _parse_result(self, output: str) -> FundamentalsOutput:
        try:
            parsed = json.loads(output)
        except json.JSONDecodeError as e:
            raise RuntimeError(
                f"Fundamentals agent returned invalid JSON: {str(e)}"
            ) from e

        missing = REQUIRED_KEYS - set(parsed.keys())
        if missing:
            raise ValueError(f"Missing fundamentals fields: {sorted(missing)}")

        return parsed
