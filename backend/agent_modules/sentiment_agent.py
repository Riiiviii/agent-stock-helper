from pydantic import ValidationError

from utils.types import ResearchPack, SentimentOutput
from typing import Final
from pathlib import Path
from agents import Agent, Runner, trace
from dotenv import load_dotenv
import json

load_dotenv(override=True)


class SentimentAgent:
    MODEL: Final = "gpt-4o-mini"
    INSTRUCTION: Final[str] = (
        Path(__file__).parent / "prompts" / "sentiment_agent.txt"
    ).read_text()

    async def run(self, research_pack: ResearchPack) -> SentimentOutput:
        data = research_pack.model_dump_json()

        sentiment_agent = Agent(
            name="sentiment-analysis-agent",
            instructions=self.INSTRUCTION,
            model=self.MODEL,
        )

        with trace("Sentiment Agent"):
            result = await Runner.run(sentiment_agent, data)
            return self._parse_result(result.final_output)

    def _parse_result(self, output: str) -> SentimentOutput:
        try:
            return SentimentOutput.model_validate_json(output)
        except ValidationError as e:
            raise RuntimeError(
                f"Fundamentals agent output failed validation: {e}"
            ) from e
