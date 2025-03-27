# Rain Alert System

This project is a weather alert system that uses the OpenWeatherMap API to fetch weather forecasts and sends SMS notifications using Twilio. It informs the user if it's going to rain, be cloudy, or if it's a happy day.

## Features
- Fetches weather data for a specific location using OpenWeatherMap API.
- Analyzes the weather data to determine the average weather condition.
- Sends an SMS alert to the user with the weather forecast.

## Requirements
Install the required dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

## Environment Variables
The following environment variables must be set:
- `OWN_API_ID`: Your OpenWeatherMap API key.
- `TW_AUTH_TOKEN`: Your Twilio Auth Token.

## Usage
1. Set the required environment variables.
2. Run the script using `python main.py`.
3. Receive SMS alerts based on the weather forecast.
