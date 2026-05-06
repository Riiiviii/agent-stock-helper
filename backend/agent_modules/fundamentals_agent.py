from pydantic import ValidationError

from utils.types import ResearchPack, FundamentalsOutput
from typing import Final
from pathlib import Path
from agents import Agent, Runner, trace
from dotenv import load_dotenv

load_dotenv(override=True)


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
            return FundamentalsOutput.model_validate_json(output)
        except ValidationError as e:
            raise RuntimeError(
                f"Fundamentals agent output failed validation: {e}"
            ) from e
