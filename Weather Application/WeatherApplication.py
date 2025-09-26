# WeatherApplication.py
# Main runner for Weather Application

from WeatherApplicationBackend import WeatherApp
import input

def main():
    city = input.get_inputs()
    app = WeatherApp()
    app.get_weather(city)

if __name__ == "__main__":
    main()
