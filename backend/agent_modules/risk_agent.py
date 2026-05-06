from pydantic import ValidationError

from utils.types import ResearchPack, RiskOutput
from typing import Final
from pathlib import Path
from agents import Agent, Runner, trace
from dotenv import load_dotenv

load_dotenv(override=True)


class RiskAgent:
    MODEL: Final = "gpt-4o-mini"
    INSTRUCTION: Final[str] = (
        Path(__file__).parent / "prompts" / "risk_agent.txt"
    ).read_text()

    async def run(self, research_pack: ResearchPack) -> RiskOutput:
        data = f"Analyse this ticker for risk. ResearchPack:\n\n{research_pack.model_dump_json()}"

        agent = Agent(
            name="risk-analysis-agent",
            instructions=self.INSTRUCTION,
            model=self.MODEL,
        )

        with trace("Risk Agent"):
            result = await Runner.run(agent, data)
            return self._parse_result(result.final_output)

    def _parse_result(self, output: str) -> RiskOutput:
        try:
            return RiskOutput.model_validate_json(output)
        except ValidationError as e:
            raise RuntimeError(
                f"Fundamentals agent output failed validation: {e}"
            ) from e
