from utils.types import ResearchPack, FundamentalsOutput
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
    Path(__file__).parent / "prompts" / "fundamentals_agent.txt"
).read_text()

server_params = MCPServerStdioParams(
    command=sys.executable,
    args=[str(Path(__file__).resolve().parents[1] / "mcp-servers" / "yfinance-mcp.py")],
)


async def run_fundamentals_agent(research_pack: ResearchPack) -> FundamentalsOutput:
    async with MCPServerStdio(
        params=server_params, client_session_timeout_seconds=60
    ) as server:
        data = json.dumps(research_pack)

        fundamentals_agent = Agent(
            name="fundamentals-analysis-agent",
            instructions=INSTRUCTION,
            model=MODEL,
            mcp_servers=[server],
        )

        with trace("Fundamental Agent"):
            result = await Runner.run(fundamentals_agent, data)

            try:
                parsed = json.loads(result.final_output)
            except json.JSONDecodeError as e:
                raise RuntimeError(
                    f"Fundamentals agent returned invalid JSON: {str(e)}"
                ) from e

            required_keys = {
                "revenue_trends",
                "profitability",
                "valuation_signals",
                "analyst_consensus",
                "summary",
                "strength",
            }
            missing = required_keys - set(parsed.keys())
            if missing:
                raise ValueError(f"Missing fundamentals fields: {sorted(missing)}")

            return parsed
