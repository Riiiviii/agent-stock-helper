from utils.types import ResearchPack, SentimentOutput
from agents.mcp import MCPServerStdio, MCPServerStdioParams
from typing import Final
from pathlib import Path
from agents import Agent, Runner, trace
from dotenv import load_dotenv
import sys
import json

load_dotenv(override=True)

REQUIRED_KEYS: Final[set[str]] = {
    "general_sentiment",
    "summary",
    "notable_events",
    "strength",
}


class SentimentAgent:
    MODEL: Final = "gpt-4o-mini"
    INSTRUCTION: Final[str] = (
        Path(__file__).parent / "prompts" / "sentiment_agent.txt"
    ).read_text()

    def __init__(self) -> None:
        self._server_params = MCPServerStdioParams(
            command=sys.executable,
            args=[
                str(
                    Path(__file__).resolve().parents[1]
                    / "mcp-servers"
                    / "finnhub-mcp.py"
                )
            ],
        )

    async def run(self, research_pack: ResearchPack) -> SentimentOutput:
        async with MCPServerStdio(
            params=self._server_params, client_session_timeout_seconds=60
        ) as server:
            data = json.dumps(research_pack)

            sentiment_agent = Agent(
                name="sentiment-analysis-agent",
                instructions=self.INSTRUCTION,
                model=self.MODEL,
                mcp_servers=[server],
            )

            with trace("Sentiment Agent"):
                result = await Runner.run(sentiment_agent, data)
                return self._parse_result(result.final_output)

    def _parse_result(self, output: str) -> SentimentOutput:
        try:
            parsed = json.loads(output)
        except json.JSONDecodeError as e:
            raise RuntimeError(
                f"Sentiment agent returned invalid JSON: {str(e)}"
            ) from e

        missing = REQUIRED_KEYS - set(parsed.keys())
        if missing:
            raise ValueError(f"Missing sentiment fields: {sorted(missing)}")

        return parsed
