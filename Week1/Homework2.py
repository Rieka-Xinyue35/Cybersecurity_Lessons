Day1 = int(input("Enter the number of steps you walked in Day 1: "))
Day2 = int(input("Enter the number of steps you walked in Day 2: "))
Day3 = int(input("Enter the number of steps you walked in Day 3: "))
Day4 = int(input("Enter the number of steps you walked in Day 4: "))
Day5 = int(input("Enter the number of steps you walked in Day 5: "))

result = Day1 + Day2 + Day3 + Day4 + Day5
print(f"{Day1} + {Day2} + {Day3} + {Day4} + {Day5} = {result}")

result = result//2
print(result)

