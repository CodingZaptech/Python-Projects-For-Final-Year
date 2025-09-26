# WeatherApplicationBackend.py
# Backend logic for Weather App

import requests

class WeatherApp:
    def __init__(self):
        self.api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your API key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city: str):
        try:
            params = {"q": city, "appid": self.api_key, "units": "metric"}
            response = requests.get(self.base_url, params=params)
            data = response.json()
            if data.get("cod") != 200:
                print("City not found or error fetching data.")
                return
            print(f"Weather in {city}:")
            print(f"Temperature: {data['main']['temp']} °C")
            print(f"Weather: {data['weather'][0]['description'].title()}")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
        except Exception as e:
            print(f"Error fetching weather data: {e}")
