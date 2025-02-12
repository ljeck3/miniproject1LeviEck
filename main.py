### INF601 - Advanced Programming in Python
### Levi Eck
### Mini Project 1
import pprint
import yfinance as yf
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt


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
        plt.plot(myarray)
        plt.xlabel('Data Points')
        plt.ylabel('Closing Price')
        plt.title(f"{ticker} Last 10 Closing Prices")
        plt.show()





#get historical market data
#hist = msft.history(period='1mo')

#pprint.pprint(hist)
