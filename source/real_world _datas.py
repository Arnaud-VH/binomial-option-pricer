import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib as plt

#We get the datas needed from yahoo finance and drop the column we dont need
ticker = yf.Ticker('JNJ')
df = ticker.history('max')
df = df.drop(['Dividends', 'Stock Splits'], axis=1)

S0 = df['Close'].iloc[-1]
print(S0)