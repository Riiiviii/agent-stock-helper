from fastapi import FastAPI
from pipeline import run_analysis

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "ok"}


@app.get("/analyze")
async def analyze(ticker: str):
    data = await run_analysis(ticker)
    return data
