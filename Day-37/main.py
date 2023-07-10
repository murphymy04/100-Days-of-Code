import requests
from datetime import datetime

USERNAME = "murphymy"
TOKEN = "mBfM27$9Q5@6"

pixela = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela, json=user_params)
# print(response.text)

graph_id = "graph18"
graph_endpoint = f"{pixela}/{USERNAME}/graphs"
graph_config = {
    "id": graph_id,
    "name": "Bible Habit Graph",
    "unit": "chapters",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

today = datetime.now()
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1"
}
pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_id}"
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)
