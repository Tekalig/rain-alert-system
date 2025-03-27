import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TW_ACCOUNT_SID")
auth_token = os.getenv("TW_AUTH_TOKEN")
api_url = "https://api.openweathermap.org/data/2.5/forecast"
params = {"lat": 38.7469, "lon": 9.025, "cnt": 3, "appid": os.getenv("OWN_API_ID")}

response = requests.get(api_url, params)
response.raise_for_status()
weather_data = response.json()
# print(data)
w_id = 0
for weather in weather_data["list"]:
    w_id += weather["weather"][0]["id"]
avg_id = w_id / 3
msg = ""
if 700 > avg_id >= 500:
    msg += "It's going to rain today. Remember to bring️ ☂ "
elif avg_id > 800:
    msg += "It's going to could. Remember to wear some 🧥"
else:
    msg += "Happy day"

client = Client(account_sid, auth_token)
message = client.messages.create(body=msg, from_="+13609723632", to="+251972530650")
print(message.status)
