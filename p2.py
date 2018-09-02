import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2016,12,31)

#yahoo API doesn't work any more, change it to robinhood or quandl
#https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-quandl
#df = web.DataReader('TSLA', 'robinhood', start, end)
df = web.DataReader('WIKI/TSLA', 'quandl', start, end)
print(df.head())
df.to_csv('TSLA.csv')

df = pd.read_csv('TSLA.csv', parse_dates = True, index_col=0)

##print(df.head())
print(df[['AdjLow','AdjHigh']].head())
####
df['AdjClose'].plot()
plt.show()













