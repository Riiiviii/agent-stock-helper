from mcp.server.fastmcp import FastMCP
import yfinance as yf

server_name: str = "yfinance-mcp"
mcp = FastMCP(server_name)


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

        return financials.to_dict()
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

        return history.to_dict()
    except Exception as e:
        return {"error": f"Failed to fetch company history for {ticker}: {str(e)}"}


if __name__ == "__main__":
    print(f"MCP Server Status: {server_name} initialized")
    mcp.run()
