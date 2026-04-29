from utils.types import ResearchPack, SentimentOutput
from agents.mcp import MCPServerStdio, MCPServerStdioParams
from typing import Final
from pathlib import Path
from agents import Agent, Runner, trace
from dotenv import load_dotenv
import sys
import json

load_dotenv(override=True)

MODEL: Final = "gpt-4o-mini"
INSTRUCTION: Final[str] = (
    Path(__file__).parent / "prompts" / "sentiment_agent.txt"
).read_text()

server_params = MCPServerStdioParams(
    command=sys.executable,
    args=[str(Path(__file__).resolve().parents[1] / "mcp-servers" / "finnhub-mcp.py")],
)


async def run_sentiment_agent(research_pack: ResearchPack) -> SentimentOutput:
    async with MCPServerStdio(
        params=server_params, client_session_timeout_seconds=60
    ) as server:
        data = json.dumps(research_pack)

        sentiment_agent = Agent(
            name="sentiment-analysis-agent",
            instructions=INSTRUCTION,
            model=MODEL,
            mcp_servers=[server],
        )

        with trace("Sentiment Agent"):
            try:
                result = await Runner.run(sentiment_agent, data)
                parsed = json.loads(result.final_output)
                required_keys = {
                    "general_sentiment",
                    "summary",
                    "notable_events",
                    "strength",
                }
                missing = required_keys - set(parsed.keys())
                if missing:
                    raise ValueError(f"Missing sentiment fields: {sorted(missing)}")
                return parsed

            except Exception as e:
                raise RuntimeError(f"Sentiment agent failed: {str(e)}") from e
