import yfinance as yf
import numpy as np

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
        df = ticker.history('1d')
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
        df = ticker.history('10y')
        df = df.drop(['Dividends', 'Stock Splits'], axis=1)
        df = df.reset_index()
        df['80MA'] = df['Close'].rolling(window=80).mean()
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
        df = ticker.history('1y')
        df = df.drop(['Dividends', 'Stock Splits'], axis=1)

        #we need to check this
        
        #price_return = df['Close'].pct_change()
        #vol = price_return.std() * np.sqrt(252)

        log_returns = np.log(df['Close'] / df['Close'].shift(1))
        vol = log_returns.std() * np.sqrt(252) 

        return vol
    
    def get_atm_strike(self, ticker_input):
      stock = yf.Ticker(ticker_input)
      current_price = stock.history(period='1d')['Close'].iloc[-1]
      strike = round(current_price)
      return strike
    
    def get_itm_strike(self, ticker_input, percent_itm=10):
      current_price = self.get_current_price(ticker_input)
      #Call ITM when price below
      itm_call = round(current_price * (1-percent_itm/100))
      #Put ITM when price above        
      itm_put = round(current_price * (1 + percent_itm/100))
      return itm_call, itm_put

    def get_otm_strike(self, ticker_input, percent_otm=10):
      current_price = self.get_current_price(ticker_input)
      #Opposite as for in the money
      otm_call = round(current_price * (1 + percent_otm/100))
      otm_put = round(current_price * (1-percent_otm/100))
      return otm_call, otm_put