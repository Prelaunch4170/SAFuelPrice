import os
from twilio.rest import Client

import CallApi
# First follow the Twilio python quick start https://www.twilio.com/docs/sms/quickstart/python
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

fuelAPIMessage = CallApi.Call_api()

message = client.messages \
    .create(
    body=fuelAPIMessage,
    from_='+17068073673',
    to='+61410531436'
)

print(fuelAPIMessage)
print(message.sid)
