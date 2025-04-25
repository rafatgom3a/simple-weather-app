import requests

class WeatherApi:
    BASE_URL = "http://api.weatherapi.com/v1"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_current_temperature(self, city):
        url = f"{self.BASE_URL}/current.json"
        params = {"key": self.api_key, "q": city}
        response = requests.get(url, params=params)
        data = response.json()

        try:
            return data["current"]["temp_c"]
        except KeyError:
            print("Error getting current temperature:", data.get("error", {}).get("message"))
            return None

    def get_temperature_after(self, city, days, hour=None):
        url = f"{self.BASE_URL}/forecast.json"
        params = {"key": self.api_key, "q": city, "days": days + 1}
        response = requests.get(url, params=params)
        data = response.json()

        try:
            forecast_day = data["forecast"]["forecastday"][days]
            if hour is not None:
                return forecast_day["hour"][hour]["temp_c"]
            return forecast_day["day"]["avgtemp_c"]
        except (KeyError, IndexError):
            print("Error getting forecast:", data.get("error", {}).get("message"))
            return None

    def get_lat_and_long(self, city):
        url = f"{self.BASE_URL}/current.json"
        params = {"key": self.api_key, "q": city}
        response = requests.get(url, params=params)
        data = response.json()

        try:
            location = data["location"]
            return location["lat"], location["lon"]
        except KeyError:
            print("Error getting coordinates:", data.get("error", {}).get("message"))
            return None, None


