### INF601 - Advanced Programming in Python
### Levi Eck
### Mini Project 1
import yfinance as yf
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)

today = datetime.now()
ten_days_ago = today - timedelta(days=15)


myTickers = ["MSFT", "NTDOY", "NVDA", "GME", "AMC"]

myTickers.sort()
for ticker in myTickers:
    result = yf.Ticker(ticker)
    hist = result.history(start=ten_days_ago, end=today)
    last10days = []
    for date in hist['Close'][:11]:
        last10days.append(date)


        myarray = np.array(last10days)
        max_price = myarray.max() + (myarray.max()*.05)
        min_price = myarray.min() - (myarray.max()*.05)
        plt.plot(myarray)
        plt.xlabel('Days Ago')
        plt.ylabel('Closing Price')
        plt.axis((9, 0, min_price, max_price))
        plt.title(f"{ticker} Last 10 Closing Prices")
        plt.savefig(f"charts/{ticker}.png")

