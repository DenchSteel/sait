import pandas as pd
import yfinance as yf

tickers_list = ['AFKS.ME']

# Import pandas
data = pd.DataFrame(columns=tickers_list)

# Fetch the data

for ticker in tickers_list:
    data[ticker] = yf.download(ticker,'2016-01-01')['Adj Close']

for tkr in tickers_list:
	dat = yf.Ticker(tkr)
	tz = dat._fetch_ticker_tz(debug_mode=True, proxy=None, timeout=30)
	valid = yf.utils.is_valid_timezone(tz)
	print(f"{tkr}: tz='{tz}', valid={valid}")





