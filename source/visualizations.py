import numpy as np
import matplotlib.pyplot as plt
from black_sholes_merton_pricer import BlackSholes
from real_world_data import RealWorldData

R = 0.05
S0 = 200
vol = 0.1
T=1
K = 180

S0_range = np.linspace(S0*0.6,S0*1.4, num= 100)

pricer_bs_call = BlackSholes(S0 = S0, K=K, T=T, R = R, option_type="call", vol=vol)
pricer_bs_put = BlackSholes(S0 = S0, K=K, T=T, R = R, option_type="put", vol=vol)


price_series_put = []
price_series_call = []

for S in S0_range:
    pricer_bs_call.S0 = S
    pricer_bs_put.S0 = S

    price_call = pricer_bs_call.compute_blackscholes()
    price_put = pricer_bs_put.compute_blackscholes()

    price_series_call.append(price_call)
    price_series_put.append(price_put)

plt.plot(S0_range, price_series_call, label='BSM Price Call')
plt.plot(S0_range, price_series_put, label='BSM Price Put')
plt.ylabel('BSM Price')
plt.xlabel('Stock Price S0')
plt.legend()
plt.show()