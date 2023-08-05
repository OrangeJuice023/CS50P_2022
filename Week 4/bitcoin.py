 # https://api.coindesk.com/v1/bpi/currentprice.json

# import library
import sys
import requests


# get value from command-line
if len(sys.argv) != 2:
    print("Command-line is not a number")
    sys.exit(1)
else:
    try:
        get_value = float(sys.argv[1])
    except:
        print("Missing command-line argument")
        sys.exit(1)


# get the current price of Bitcoin, convert it as a float, then print the value in the command-line
try:

    get_api = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    api = get_api
    raw = api.json()
    us = raw["bpi"]
    float_p = us["USD"]
    full_dat = float_p["rate_float"]
    operate = full_dat * get_value
    print(f"${operate:,.4f}")

except requests.RequestException:
    print("RequestException")
    sys.exit(1)
