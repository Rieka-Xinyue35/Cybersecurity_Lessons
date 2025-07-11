Apartment_budget_assistant = "User"
print("Hello tenant, I am your apartment budget assistant, please fill in the form below.")

Name = input("Enter your name: ")
Unit = input("Enter the unit you live in: ")
Apartment_number = input("Enter your apartment number: ")
Monthly_income = input("Enter your monthly income: ")
Rent = int(input("Enter the amount of money you spend on rent monthly: "))
Food = int(input("Enter the amount of money you spend on food monthly: "))
Entertainment = int(input("Enter the amount of money you spend on entertainment monthly: "))
Daily_necessities  = int(input("Enter the amount of money you spend on daily necessities monthly: "))

Total_expenses = Rent + Food + Entertainment + Daily_necessities
print(f"{Rent} + {Food} + {Entertainment} + {Daily_necessities} = {Total_expenses}")

