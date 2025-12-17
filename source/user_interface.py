from real_world_data import RealWorldData
import yfinance as yf
class UserInterface:

   @staticmethod
   def get_user_inputs():
      print("=" * 50)
      print("Welcome to our Binomial Option Pricing Application.")
      print("=" * 50)

      ticker = UserInterface._get_ticker()
      option_type = UserInterface._get_option_type()
      strike = UserInterface._get_strike(ticker, option_type)

      data = RealWorldData()
      S0 = data.get_current_price(ticker)
      vol = data.get_volatility(ticker)
      R = data.get_rf("^IRX")

      inputs_dict = {
         "ticker": ticker,
         "S0": S0,
         "K": strike, 
         "T": 1,
         "R": R,
         "sigma": vol,
         "n_steps": 10,
         "option_type": option_type
      }

      return inputs_dict


   @staticmethod
   def _get_ticker():
      print("\n Please enter the stock ticker symbol (e.g. NVDA, TSLA, JNJ): ")
      while True:
         ticker_input = input("> ").upper().strip()
         if not UserInterface._validate_ticker(ticker_input):
            print("This ticker does not exist. Please enter a valid Ticker.")
         else:
            return ticker_input
      

   @staticmethod
   def _validate_ticker(ticker):
      #Method to check if ticker exists found on Stack Overflow
      info = yf.Ticker(ticker).history(period = "7d", interval = "1d")
      return len(info) > 0


   @staticmethod
   def _get_option_type():
      print("\nChoose option type:")
      print("1. Call option")
      print("2. Put option\n")

      while True:
         choice = input("Enter 1 or 2: ").strip()
         if choice == "1":
            return 'call'
         elif choice == "2":
            return 'put'
         print("Invalid choice! Please enter 1 or 2.")
   
   @staticmethod
   def _get_strike(ticker, option_type):
      print("\nSelect the moneyness of the option (strike price relative to current price):")
      print("1. ATM - At The Money (Strike close to current price)")
      print("2. ITM - In The Money (Favourable strike)")
      print("3. OTM - Out The Money (Unfavourable strike)\n")

      data = RealWorldData()

      while True:
         choice = input("Enter your choice as 1-3:\n").strip()

         if choice == "1":
            strike = data.get_atm_strike(ticker)
            return strike
         elif choice == "2":
            itm_call, itm_put = data.get_itm_strike(ticker, percent_itm=10)
            strike = 0
            if option_type == "call":
               strike = itm_call
            else:
               strike = itm_put
            return strike
         elif choice == "3":
            otm_call, otm_put = data.get_otm_strike(ticker, percent_otm=10)
            if option_type == "call":
               strike = otm_call
            else:
               strike = otm_put
            return strike
         
         print("Invalid choice! Please enter a number between 1 and 3.\n")

      