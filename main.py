### INF601 - Advanced Programming in Python
### Levi Eck
### Mini Project 1
import pprint
import yfinance as yf

msft = yf.Ticker("MSFT")

# get all stock info
#pprint.pprint(msft.info)

#get historical market data
hist = msft.history(period='1mo')

pprint.pprint(hist)
