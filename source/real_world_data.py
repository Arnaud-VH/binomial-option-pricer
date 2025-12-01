import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib as plt

class RealWorldData:
    ##We get the datas needed from yahoo finance and drop the column we dont need
    def __init__(self):
        pass
    
    def get_current_price(self, ticker_input):

        ticker = yf.Ticker(str(ticker_input))
        df = ticker.history('max')
        df = df.drop(['Dividends', 'Stock Splits'], axis=1)
        S0 = df['Close'].iloc[-1]

        return S0

    def get_df(self, ticker_input):

        ticker = yf.Ticker(str(ticker_input))
        df = ticker.history('max')
        df = df.drop(['Dividends', 'Stock Splits'], axis=1)

        return df
    
    #We want with this get the current risk free rate in the market:
    def get_rf(self, ticker_rf):

        ticker_rf = yf.Ticker(str(ticker_rf))
        df_rf = ticker_rf.history(period = '1d')
        R = df_rf['Close'].iloc[-1] / 100
        return R

    #Hystorical volatility of the stock, since we would get daily volatility we need to multiply by the average number of trading days
    def get_volatility(self, ticker_input):

        ticker = yf.Ticker(str(ticker_input))
        df = ticker.history('max')
        df = df.drop(['Dividends', 'Stock Splits'], axis=1)
        price_return = df['Close'].pct_change()
        vol = price_return.std() * np.sqrt(252) 

        return vol

