# import csv
# import json
#
# with open("countries_population.csv", 'r',newline="", encoding = "utf-8") as word:
#     data_set = csv.DictReader(word)
#     data_set = list(data_set)
#
#
# with open("countries_population.json",'w') as json_file:
#      json.dump(data_set, json_file,indent = 4)
#
# with open("countries_population.json", 'r') as word:
#     country = json.load(word)
#
# country_lookup = input("Enter the country to reveal it's population: ")
# for data in country:
#
#     if data['Country'] == country_lookup:
#         print(data['Population'])
#

