import csv
'''
with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperatures = []
    for row in data:
        print(row)
        temperature = row[1]
        if temperature != 'temp':
            temperatures.append(int(temperature))
    print(temperatures)
'''
import pandas
'''
data = pandas.read_csv("weather_data.csv")

temp_list = data['temp'].to_list()
print(data['temp'].mean())
print(data['temp'].max())

print(data[data['temp'] == data['temp'].max()])

monday = data[data.day == "Monday"]
temp_to_F = (monday.temp * 9/5) + 32
print(temp_to_F)
'''
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251001.csv")

grey = data[data['Primary Fur Color'] == 'Gray']
cinnamon = data[data['Primary Fur Color'] == 'Cinnamon']
black = data[data['Primary Fur Color'] == 'Black']

num_of_grey = len(grey)
num_of_cinnamon = len(cinnamon)
num_of_black = len(black)

squirrel_dictionary = {
    'fur color': ['grey', 'cinnamon', 'black'],
    'count': [num_of_grey, num_of_cinnamon, num_of_black],
}

data = pandas.DataFrame(squirrel_dictionary)
data.to_csv("squirrel_count.csv")
