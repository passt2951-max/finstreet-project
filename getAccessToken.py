#This to generate access token from refresh token

import requests
from hashlib import sha256

# fyers api details
client_id = None
secret_id = None
app_id_hash = sha256(f"{client_id}:{secret_id}".encode()).digest()

grant_type = "refresh_token"
pin = None

try:
    with open("tokens.txt", 'r') as file:
        lines = file.readlines()
        refresh_token = lines[1].split(':')[1].strip()
except:
    print("Error in reading file")

verify_auth_url = "https://api-t1.fyers.in/api/v3/validate-authcode"

headers = {
    "Content-Type": "application/json"
}

data = {
    "grant_type": grant_type,
    "appIdHash": app_id_hash,
    "refresh_token": refresh_token,
    "pin": pin
}

res = requests.get(url=verify_auth_url, data=data, headers=headers)
res = res.json()

if res['s'] != 200:
    print("Error in validating auth code")
    print(f"message: {res['message']}")
    quit()

access_token = res['access_token']

print(f"access_token: {access_token}")
print(f"refresh_token: {refresh_token}")

with open("tokens.txt", "w") as file:
    print(f"access_token: {access_token}", file=file)
    print(f"refresh_token: {refresh_token}", file=file)
