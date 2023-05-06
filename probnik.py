import datetime
from datetime import datetime as dt

import pytz
import streamlit as st
import yfinance as yf
import pandas

tz = pytz.timezone("Europe/Moscow")
now = str(datetime.datetime.now()).split()
now_date = list(map(int, now[0].split('-')))
print(now_date)
start = tz.localize(dt(2022, 5, 1))
end = tz.localize(dt.today())

tickers = "AFKS.ME,GAZP.ME".split(",")
df = yf.download(tickers,start, end, auto_adjust=True)['Close']

st.table(df.head())