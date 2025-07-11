import csv
import json

with open("World Population Live Dataset.csv", 'r', newline="", encoding="utf-8") as word:
    data_set = csv.DictReader(word)
    data_set = list(data_set)

with open("World Population Live Dataset.json", 'w') as json_file:
     json.dump(data_set, json_file,indent = 4)

with open("World Population Live Dataset", 'r') as word:
    country = json.load(word)

country_lookup = input("Enter the country to reveal it's population, area, density, growth rate, population: ")
