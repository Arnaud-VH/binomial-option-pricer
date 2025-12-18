from black_sholes_merton_pricer import BlackSholes
from binomial_option_pricer import BinomialOptionPricer
import matplotlib.pyplot as plt

class ConvergenceAnalyser:
   """
   Need to also add the DocString. 
   """
   @staticmethod
   def check_convergence(S0, K, T, R, sigma, option_type, max_steps=200, step_increment=5):
      pricer_bs = BlackSholes(S0, K, T, R, sigma, option_type)
      bs_price = pricer_bs.compute_blackscholes()

      steps = list(range(1, max_steps, step_increment))
      binomial_prices = []
      for n in steps:
         pricer = BinomialOptionPricer(S0, K, T, R, n, option_type, sigma)
         price = pricer.price_european()[0][0]
         binomial_prices.append(price)
      
      plt.figure(figsize=(14,6))
      plt.plot(steps, binomial_prices, label=f"Binomial Price: ${binomial_prices[len(binomial_prices)-1]:.2f}")
      plt.axhline(y=bs_price, color = 'r', label =f"Black Scholes Price: ${bs_price:.2f}")
      plt.xlabel("Number of steps in binomial tree")
      plt.ylabel("Option Price")
      plt.title("Convergence of Binomial model to Black Scholes")
      plt.legend()
      plt.show(block=False)