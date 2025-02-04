### INF601 - Advanced Programming in Python
### Levi Eck
### Mini Project 1
import pprint
import yfinance as yf


mydata ={}

myTickers = ["MSFT", "AAPL", "NVDA", "GME", "AMC"]
myTickers.sort()
for ticker in myTickers:
    result = yf.Ticker(ticker)
    mydata[ticker] = {'ticker': ticker,
                      'dayHigh': result.info['dayHigh']
                        }
    print(f"Ticker: {ticker} \tDaily High: {result.info['dayHigh']}")

pprint.pprint(mydata)



#get historical market data
#hist = msft.history(period='1mo')

#pprint.pprint(hist)
