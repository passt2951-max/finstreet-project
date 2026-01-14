# This script is to get the history data from the fyers api

import requests
import pandas as pd

app_id = None
symbol = "" # Sonata's Symbol
resolution = "30"
range_from = "2025-11-01" 
range_to = "2025-12-31"

try:
    with open("tokens.txt", "r") as file:
        line = file.readlines()[0]
        access_token = line.split(":")[1].strip()
except:
    print("Error in opening the tokens file")

history_api_url = "https://api-t1.fyers.in/data/history"

headers = {
    "Authorization": f"{app_id}:{access_token}"
}

params = {
    "symbol": symbol,
    "resolution": resolution,
    "date_format": 1,
    "range_from": range_from,
    "range_to": range_to,
    "cont_flag": 0
}

res = requests.post(url=history_api_url, params=params, headers=headers)
res = res.json()

if res['s'] != 200:
    print("Error in fetching data")
    print(f"message: {res['message']}")
    quit()

candles = res['candles']
df = pd.DataFrame(candles)
df.columns = ['epoch', 'open', 'high', 'low', 'close', 'volume']

df.to_csv(f"{symbol.upper()}.csv")