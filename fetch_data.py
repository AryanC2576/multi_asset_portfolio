import yfinance as yf
import pandas as pd

def fetch_crypto_prices(tickers, start="2022-01-01"):
    df = yf.download(tickers, start=start)["Close"]
    return df.dropna()
