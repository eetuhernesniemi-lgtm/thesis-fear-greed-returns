import yfinance as yf
import pandas as pd

start = "2018-02-01"
end = "2025-05-02"

print("Getting S&P 500 company list...")
tickers_df = pd.read_csv("sp500_list.csv")
tickers = tickers_df["Symbol"].tolist()
tickers = [t.replace(".", "-") for t in tickers]
print(f"Found {len(tickers)} companies")

print("Downloading all stocks... this will take a few minutes!")
all_returns = []

for i, ticker in enumerate(tickers):
    try:
        data = yf.download(ticker, start=start, end=end, progress=False)
        if len(data) > 20:
            monthly = data["Close"].resample("MS").last()
            returns = monthly.pct_change() * 100
            returns.name = ticker
            all_returns.append(returns)
    except:
        pass
    if (i+1) % 50 == 0:
        print(f"  {i+1}/{len(tickers)} done...")

print("Saving...")
returns_df = pd.concat(all_returns, axis=1)
returns_df.to_csv("sp500_monthly_returns.csv")
print(f"Done! Saved {returns_df.shape[1]} companies.")