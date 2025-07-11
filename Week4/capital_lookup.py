import json
import pyttsx3

dictAI = pyttsx3.init()

with open("countries_capitals_100.json", 'r') as word:
    country = json.load(word)
    data = list(country)


country_lookup = input("Enter the country you are looking for to reveal the capital: ")
for words in data:
    if words['country'] == country_lookup:
        capital = words['capital']
        print(capital)
        dictAI.say(f" The capital of {country_lookup} is {capital} ")
        dictAI.runAndWait()

else:
    dictAI.say(f" The country {country_lookup} is not found")
    dictAI.runAndWait()
