names_of_students = ['Olive','Palm','Stephenie','Zelba','Petra','Karmel',]
surnames = ['','Ansah-Abiesi','Ansah-Abiesi','Sackey','McBagonluri','Sarpong','Adjani']
# Olive = names_of_students[]
# print("Olive")

# for names in names_of_students:
#     print(names)
#
# for itemize in range(6):
itemize = 0
INDEX = 0
# for names in names_of_students:
#         itemize = itemize + 1
#         print(f"({itemize}) {names}")

for fnames in names_of_students:
    itemize = itemize + 1
    print(f"({itemize}){fnames} {surnames[INDEX + itemize]}") 