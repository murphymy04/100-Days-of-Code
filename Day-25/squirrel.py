import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = data[data["Primary Fur Color"] == "Gray"]
cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
black = data[data["Primary Fur Color"] == "Black"]
squirrel_dict = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Count": [len(gray), len(cinnamon), len(black)]
}
dataframe = pd.DataFrame(squirrel_dict)
dataframe.to_csv("squirrel_count.csv")
