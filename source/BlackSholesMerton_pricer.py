from typing import Optional
import numpy as np
import scipy
from scipy import stats

#Pricer for European options

class BlackSholes:
    def __init__(self, S0:float, K:float, T:float, R:float, vol:float, option_type: str):
        self.S0 = S0
        self.K = K
        self.T = T
        self.vol = vol
        self.R =R
        self.option_type = option_type.lower()
    
    def compute_d1(self):
        return (np.log(self.S0/self.K) + (self.R + self.vol**2 / 2) * self.T)/(self.vol * np.sqrt(self.T))
    
    def compute_d2(self):
        return (np.log(self.S0/self.K) + (self.R - self.vol**2 / 2) * self.T) / (self.vol * np.sqrt(self.T))

    def compute_blackscholes(self):

        if self.option_type=="call":
            return self.S0 * stats.norm.cdf(self.compute_d1()) - self.K * np.exp(-self.R * self.T) * stats.norm.cdf(self.compute_d2())
 
        elif self.option_type=="put":
            return self.S0 * np.exp(-self.R * self.T) * stats.norm.cdf(-self.compute_d2()) - self.S0 * stats.norm.cdf(-self.compute_d1())


