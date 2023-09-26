import os
import requests

import CallApi


fuelAPIMessage = CallApi.Call_api()
# to set ENV token use "setx TOKEN_NAME TOKEN_VARIABLE"
# non self-hosting NTFY uses no authentication
# so make the token variable random using something like a password generator
NTFY_SUB_TOKEN = os.environ['NTFY_SUB']

requests.post("https://ntfy.sh/"+NTFY_SUB_TOKEN,
              data=fuelAPIMessage.encode(encoding='utf-8'),
              headers={"Title": "Fuel Price"})

print(fuelAPIMessage)
