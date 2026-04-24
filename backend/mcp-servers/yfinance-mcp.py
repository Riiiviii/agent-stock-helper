import math
import yfinance as yf
from mcp.server.fastmcp import FastMCP

server_name: str = "yfinance-mcp"
mcp = FastMCP(server_name)


def _clean_nan(value):
    if isinstance(value, float) and math.isnan(value):
        return None
    return value


@mcp.tool()
def get_company_information(ticker: str):
    """This tool provides the current business information for a given stock ticker.

    Args:
        ticker: the stock ticker
    """
    try:
        user_ticker = yf.Ticker(ticker)
        information = user_ticker.info

        if not information or len(information) < 5:
            return {"error": f"No data found for ticker: {ticker}"}

        return information
    except Exception as e:
        return {"error": f"Failed to fetch company info for {ticker}: {str(e)}"}


@mcp.tool()
def get_company_financials(ticker: str):
    """This tool provides the current business financials for a given stock ticker.

    Args:
        ticker: the stock ticker
    """
    try:
        user_ticker = yf.Ticker(ticker)
        financials = user_ticker.financials

        if financials.empty:
            return {"error": f"No data found for ticker: {ticker}"}

        raw = financials.to_dict()
        cleaned = {}
        for column, values in raw.items():
            cleaned[column] = {}
            for date, value in values.items():
                cleaned[column][date] = _clean_nan(value)
        return cleaned
    except Exception as e:
        return {"error": f"Failed to fetch company financials for {ticker}: {str(e)}"}


@mcp.tool()
def get_price_history(ticker: str):
    """This tool provides the current business price history for a given stock ticker.

    Args:
        ticker: the stock ticker
    """
    try:
        user_ticker = yf.Ticker(ticker)
        history = user_ticker.history(period="1y")

        if history.empty:
            return {"error": f"No data found for ticker: {ticker}"}

        raw = history.to_dict()
        cleaned = {}
        for column, values in raw.items():
            cleaned[column] = {}
            for date, value in values.items():
                cleaned[column][date] = _clean_nan(value)
        return cleaned
    except Exception as e:
        return {"error": f"Failed to fetch company history for {ticker}: {str(e)}"}


if __name__ == "__main__":
    print(f"MCP Server Status: {server_name} initialized")
    mcp.run()
