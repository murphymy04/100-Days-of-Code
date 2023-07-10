import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url_get = "https://api.sheety.co/1913008450b172e1421dd5c5ba7bb69e/copyOfFlightDeals/prices"
        self.url_put = "https://api.sheety.co/1913008450b172e1421dd5c5ba7bb69e/copyOfFlightDeals/prices/[Object ID]"
        self.response = requests.get(url=self.url_get)
        self.data = self.response.json()

    def get_data(self):
        return self.data

