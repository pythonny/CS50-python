# As of Saturday, April 5, 2025 at 3:00 PM GMT+2, we are aware of the CoinCap v2 API deprecation that may affect students’ ability to complete this problem. We have now updated the problem to use the CoinCap v3 API instead.
# If you have already started working on this problem, you must update your code to use the CoinCap v3 API instead of the CoinCap v2 API. Importantly, you will need to sign up for a CoinCap account and obtain an API key. You can do this by visiting CoinCap.
# Once you have your API key, you can use it in your code to access the CoinCap v3 API.

# Bitcoin logo
# Bitcoin is a form of digital currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.

# Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

# In a file called bitcoin.py, implement a program that:

# Expects the user to specify as a command-line argument the number of Bitcoins,
# , that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
# Queries the API for the CoinCap Bitcoin Price Index at rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey. You should replace YourApiKey with the actual API key you obtained from your CoinCap account dashboard, which returns a JSON object,
#  among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code lik
import requests
import sys

# see if the amount of command-line arguments is correct, [0] = name file, [1]  is the amount of bitcoins they want to buy
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

# we check if sys.arg[1] is a float number ( the amount of bitcoins they want to buy)
try:
    bitcoins = float(sys.argv[1])

# Since we expect a float, we use sys.exit to exit the problem with an error code.
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=ff4514f52dd4548059e576e72144265cb2e3f2a450a6d6babcb24cf8d3c73527")
    # Raise for will raise an HTTPError if the request returned an unsuccesfull status code. The code will stop if the data cannot be pulled
    # if we don't use raise_for_status() we have the risk that the program continues using wrong or incomplete data
    response.raise_for_status()
    #json = Javascrapt Object Notation. A way to collect and send data that both humans and computers can read
    data = response.json()
    # First print data as a test You'll see that the json response has a "Data" followed by many keys, one of which is"priceUSD"
    # So to get that we first refer to response.json() which is saved in the definition Data 2 lines above, then we go to the keyword "data" and then we go to the keyword "priceUsd"
    price = float(data["data"]["priceUsd"])
    # we round on 4 decimals
    final_price = round(bitcoins * price, 4)
    # :, adds , after 3 numbers. So 1000$ becomes 1,000
    print(f"${final_price:,}")


except requests.RequestException:
    print("Invalid URL")
