import requests
api_key = "6612c8d75ddedb1e906fbd6df278813a"

endpoint = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
    "lat": 27.197548,
    "lon": -80.252823,
    "appid": api_key
}

response = requests.get(endpoint, params=parameters)
response.raise_for_status()
data = response.json()

