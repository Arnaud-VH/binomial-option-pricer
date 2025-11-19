from binomial_option_pricer import BinomialOptionPricer

pricer = BinomialOptionPricer(
   S0 = 50, K=55, T=2, R=0.05, n_steps = 2, option_type="put", up=1.1, down=0.92
)

option_tree = pricer.price_european()
for row in option_tree:
   print(row)

print(f"The final option price is {option_tree[0][0]:.4f}")