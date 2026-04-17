import yfinance as yf


async def run_analysis(ticker: str):
    raw_ticker_info = fetch_records(ticker)

    return {
        "info": raw_ticker_info,
    }


def fetch_records(ticker: str):
    user_ticker = yf.Ticker(ticker)
    ticker_info = user_ticker.info
    return ticker_info
