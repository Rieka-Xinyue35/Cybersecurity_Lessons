name = "Olive"
lengthofname = len(name)
print(lengthofname)

firstname = "Olive"
lastname = "Ansah-Abiesi"
#concantenation
fullname = firstname+ " " +lastname
print(fullname)

# formatted string
fullname = f"{firstname} {lastname}"
print(fullname)

# .format
fullname = "{} {}".format(firstname,lastname)
print(fullname)

sentence = "He is my teacher. He teaches ICT and he is Mr. Samuel"
sentence = sentence.upper()
print(sentence)
sentence = sentence.lower()
print(sentence)

sentence = "He is my teacher. He teaches ICT and he is Mr. Samuel"
sentence = sentence.replace("ICT", "Physics")
numberofs = sentence.find("s")
print(sentence)
print(numberofs)

sentence = "He is my teacher. He teaches ICT and he is Mr. Samuel"
sentence = sentence.replace("ICT", "Physics")
numberofs = sentence.count("s")
print(sentence)
print(numberofs)

nameofmonth = "April,May,June"
newNames = nameofmonth.split(",")
print(newNames)
