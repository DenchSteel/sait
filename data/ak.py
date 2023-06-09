import datetime
from datetime import datetime as dt
import os

import pytz
import streamlit as st
import yfinance as yf

tz = pytz.timezone("Europe/Moscow")
now = str(datetime.datetime.now()).split()
now_date = list(map(int, now[0].split('-')))
print(now_date)
start = tz.localize(dt(2020, 1, 3))
end = tz.localize(dt.today())


tickers = "AFKS.ME,GAZP.ME,IRAO.ME,NLMK.ME,MTSS.ME,MGNT.ME,ROSN.ME,SBER.ME,CHMF.ME,AFLT.ME,YNDX.ME,ALRS.ME".split(",")
df = yf.download(tickers,start, end, auto_adjust=True)['Close']

st.table(df.head())
