# with open("weather_data.csv") as file:
#    data = file.readlines()

'''import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)'''

import pandas

'''data = pandas.read_csv("weather_data.csv")

monday = data[data.day == "Monday"]
new_temp = (monday.temp * (9/5)) + 32
print(new_temp)'''

# create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
