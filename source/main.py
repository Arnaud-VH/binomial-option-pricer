from binomial_option_pricer import BinomialOptionPricer
from BlackSholesMerton_pricer import BlackSholes
from real_world_data import RealWorldData

ticker_input = "JNJ"
ticker_rf = "^IRX"

data = RealWorldData()
R = data.get_rf(ticker_rf)
S0 = data.get_current_price(ticker_input)
vol = data.get_volatility(ticker_input)

pricer_bt = BinomialOptionPricer(
   S0 = S0, K=200, T=2, R = R, n_steps = 100, option_type="call", up=1.1, down=0.92
)
pricer_bs = BlackSholes(
   S0 = S0, K=200, T=2, R = R, option_type="call", vol=vol
)

price_bs = pricer_bs.compute_blackscholes()
option_tree = pricer_bt.price_european()

print(f"The final option price is {option_tree[0][0]:.4f}")
print(f"The final option price is {price_bs:.4f}")