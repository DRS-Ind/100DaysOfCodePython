import requests
from credentials import open_weather_map_token


parameters = {
    "lat": 50.447731,
    "lon": 30.542721,
    "cnt": 4,
    "appid": open_weather_map_token,
    "lang": "ua"
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)

response.raise_for_status()

weather_data = response.json()["list"]
