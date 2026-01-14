# This script is to generate auth code, refresh token and access token

import requests 
from hashlib import sha256

# fyers api details
client_id = None
secret_id = None
app_id_hash = sha256(f"{client_id}:{secret_id}".encode()).digest()

redirect_url = "https://www.google.com"
response_type = "code"
state = None
grant_type = "authorization_code"

get_auth_url = "https://api-t1.fyers.in/api/v3/generate-authcode"

params_for_auth = {
    "client_id": client_id,
    "redirect_uri": redirect_url,
    "request_type": response_type,
    "state": state
}

res = requests.get(url=get_auth_url, params=params_for_auth)
res = res.json()

if res['s'] != 200:
    print("Error in generating auth code")
    print(f"message: {res['message']}")
    quit()

auth_code = res['auth_code']
print(f"Authentication Code: {auth_code}")

verify_auth_url = "https://api-t1.fyers.in/api/v3/validate-authcode"

headers = {
    "Content-Type": "application/json"
}

data = {
    "grant_type": grant_type,
    "appIdHash": app_id_hash,
    "code": auth_code
}

res = requests.get(url=verify_auth_url, data=data, headers=headers)
res = res.json()

if res['s'] != 200:
    print("Error in validating auth code")
    print(f"message: {res['message']}")
    quit()

access_token = res['access_token']
refresh_token = res['refresh_token']

print(f"access_token: {access_token}")
print(f"refresh_token: {refresh_token}")

with open("tokens.txt", "w") as file:
    print(f"access_token: {access_token}", file=file)
    print(f"refresh_token: {refresh_token}", file=file)
