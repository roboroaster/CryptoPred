import pandas_datareader as web 
import datetime as dt 
import mplfinance as mpf

start  = dt.datetime(2021,1,1)
end = dt.datetime.now()

data = web.DataReader('BTC-USD','yahoo',start,end)

mpf.plot(data,type='candle',volume=True,style='yahoo')