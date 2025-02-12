### INF601 - Advanced Programming in Python
### Levi Eck
### Mini Project 1

#Package Imports
import yfinance as yf
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import os


os.makedirs("charts", exist_ok=True)

today = datetime.now()
ten_days_ago = today - timedelta(days=15)

#Collect closing price of 5 stock tickers for the last 10 trading days
#Store in a list that coverts to an array in NumPy
myTickers = ["MSFT", "NTDOY", "NVDA", "TXT", "F"]

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
        #Plot the graphs
        plt.plot(myarray)
        plt.xlabel('Days Ago')
        plt.ylabel('Closing Price')
        plt.axis((9, 0, min_price, max_price))
        plt.title(f"{ticker} Last 10 Closing Prices")
        #Save in a folder called charts as PNG files
        plt.savefig(f"charts/{ticker}.png")