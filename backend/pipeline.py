import yfinance as yf
import finnhub
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv(override=True)
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")


async def run_analysis(ticker: str):
    raw_ticker_info = fetch_records(ticker)
    raw_ticker_news = fetch_news(ticker)

    return {
        "info": raw_ticker_info,
        "news": raw_ticker_news,
    }


def fetch_records(ticker: str):
    user_ticker = yf.Ticker(ticker)
    ticker_info = user_ticker.info
    return ticker_info


def fetch_news(ticker: str):
    client = finnhub.Client(api_key=FINNHUB_API_KEY)
    today = datetime.today().strftime("%Y-%m-%d")
    month_ago = (datetime.today() - timedelta(days=30)).strftime("%Y-%m-%d")
    news = client.company_news(ticker, _from=month_ago, to=today)
    return news
