import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib as plt

class RealWorldData:
    """
    We get the data needed from yahoo finance
    """
    def __init__(self):
        pass
    
    def get_current_price(self, ticker_input):
        """
        Get the current price of the stock:

        Parameters:
            ticker_input: Ticker of the stock
        """
        ticker = yf.Ticker(str(ticker_input))
        df = ticker.history('max')
        df = df.drop(['Dividends', 'Stock Splits'], axis=1)
        S0 = df['Close'].iloc[-1]

        return S0

    def get_df(self, ticker_input):
        """
        Get the pandas dataframe of the stock:

        Parameters:
            ticker_input: Ticker of the stock
        """
        ticker = yf.Ticker(str(ticker_input))
        df = ticker.history('max')
        df = df.drop(['Dividends', 'Stock Splits'], axis=1)

        return df
    
    #We want with this get the current risk free rate in the market:
    def get_rf(self, ticker_rf):
        """
        Get the current risk free rate in the market:

        Parameters:
            ticker_rf: Ticker of the risk free bond (yearly rate)
        """
        ticker_rf = yf.Ticker(str(ticker_rf))
        df_rf = ticker_rf.history(period = '1d')
        R = df_rf['Close'].iloc[-1] / 100
        return R

    #Historical volatility of the stock, since we would get daily volatility we need to multiply by the average number of trading days
    def get_volatility(self, ticker_input):
        """
        get the historycal volatility of the stock:

        Parameters:
            ticker_input: Ticker of the stock
        """

        ticker = yf.Ticker(str(ticker_input))
        df = ticker.history('max')
        df = df.drop(['Dividends', 'Stock Splits'], axis=1)
        price_return = df['Close'].pct_change()
        vol = price_return.std() * np.sqrt(252) 

        return vol

