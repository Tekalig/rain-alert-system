# Importing necessary modules
import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

# Loading environment variables from a .env file
load_dotenv()

try:
    # Fetching Twilio account SID and authentication token from environment variables
    account_sid = os.getenv("TW_ACCOUNT_SID")
    auth_token = os.getenv("TW_AUTH_TOKEN")
    if not account_sid or not auth_token:
        raise ValueError("Twilio credentials are missing in environment variables.")

    # Setting up the OpenWeatherMap API URL and parameters
    api_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {"lat": 38.7469, "lon": 9.025, "cnt": 3, "appid": os.getenv("OWN_API_ID")}
    if not params["appid"]:
        raise ValueError("OpenWeatherMap API key is missing in environment variables.")

    # Sending a GET request to the OpenWeatherMap API
    response = requests.get(api_url, params)
    # Raising an exception if the request was unsuccessful
    response.raise_for_status()
    # Parsing the JSON response from the API
    weather_data = response.json()

    # Initializing a variable to calculate the sum of weather condition IDs
    w_id = 0
    # Iterating through the weather data to sum up the weather condition IDs
    for weather in weather_data["list"]:
        w_id += weather["weather"][0]["id"]

    # Calculating the average weather condition ID
    avg_id = w_id / 3

    # Initializing a message variable
    msg = ""
    # Checking weather conditions and setting an appropriate message
    if 700 > avg_id >= 500:
        msg += "It's going to rain today. Remember to bring ☂️"
    elif avg_id > 800:
        msg += "It's going to be cloudy. Remember to wear some 🧥"
    else:
        msg += "Happy day!"

    # Creating a Twilio client instance
    client = Client(account_sid, auth_token)
    # Sending the weather message via Twilio SMS
    message = client.messages.create(body=msg, from_="+13609723632", to="+251972530650")
    # Printing the status of the sent message
    print(message.status)

except requests.exceptions.RequestException as e:
    print(f"Error occurred while fetching weather data: {e}")
except KeyError as e:
    print(f"Missing expected data in the API response: {e}")
except ValueError as e:
    print(f"Configuration error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
