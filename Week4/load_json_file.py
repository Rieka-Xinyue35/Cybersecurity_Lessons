import json
import pyttsx3
dictAI = pyttsx3.init()

with open("dictionary.json", 'r') as word:
    data_set = json.load(word)

word = input("Enter the word you are looking for: ")
if word in data_set:
    desc = data_set[word]
    print(desc)
    dictAI.say(f"{word} means {desc}")
    dictAI.runAndWait()
else:
    dictAI.say(f"The word {word} is not found")
    dictAI.runAndWait()