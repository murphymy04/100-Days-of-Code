from dotenv import load_dotenv
import os
import requests

load_dotenv()
KEY = os.getenv("key")
PARAMS = {
    "key": KEY,
    "search": "Tears of the Kingdom",
}

data = requests.get(url="https://api.rawg.io/api/games", params=PARAMS).json()
for i in range(len(data["results"])):
    print(data["results"][i]["name"])
id = data["results"][0]["id"]
game_data = requests.get(url=f"https://api.rawg.io/api/games/{id}", params={"key": KEY}).json()
'''print(game_data["description"])
print(data["results"][0]["name"])
print(data["results"][0]["released"])
print(data["results"][0]["background_image"])'''