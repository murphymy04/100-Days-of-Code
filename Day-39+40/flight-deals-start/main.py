# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_data()["prices"]
flight_data = FlightSearch()

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_data.hi()


