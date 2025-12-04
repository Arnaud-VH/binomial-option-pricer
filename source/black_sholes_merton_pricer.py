from typing import Optional
import numpy as np
from scipy import stats

#Pricer for European options

class BlackSholes:
    """
    Option pricer for only European options, non-dividend paying.
    
    Attributes:
      S0: Initial Stock Price
      K: Strike Price
      T: Time to expiry (in years)
      R: Risk-free interest rate
      vol: Historical volatility of the stock
      option_type: Either a Call option or a Put option

    """
    def __init__(self, S0:float, K:float, T:float, R:float, vol:float, option_type: str):
        self.S0 = S0
        self.K = K
        self.T = T
        self.vol = vol
        self.R =R
        self.option_type = option_type.lower()
    
    def compute_d1(self):
        """
        Compute the d1 parameter
        """
        return (np.log(self.S0/self.K) + (self.R + self.vol**2 / 2) * self.T)/(self.vol * np.sqrt(self.T))
    
    def compute_d2(self):
        """
        Compute the d2 parameter
        """
        d1 = self.compute_d1()
        return d1 - self.vol * np.sqrt(self.T)

    def compute_blackscholes(self):
        """
        Compute the price of the european option according to the BSM
        """

        if self.option_type=="call":
            return self.S0 * stats.norm.cdf(self.compute_d1()) - self.K * np.exp(-self.R * self.T) * stats.norm.cdf(self.compute_d2())
 
        elif self.option_type=="put":
            return self.K * np.exp(-self.R * self.T) * stats.norm.cdf(-self.compute_d2()) - self.S0 * stats.norm.cdf(-self.compute_d1())


