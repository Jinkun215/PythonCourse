import csv

with open("starfolder/weather.txt", "r") as file:
    data = list(csv.reader(file))

print(data)

city = input("Enter a city: ")
city = city.title()

for row in data[1:]:
    if row[0] == city:
        print(row[1])