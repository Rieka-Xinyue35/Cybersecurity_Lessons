# age = int(input("Enter your age: "))
#
# if age > 18:
#     print("You  are eligible to vote")
#
# else:
#     print("You are not eligible to vote")

score = int(input("Enter your score: "))

if score >= 90 and score <= 100:
    print("Excellent  job, you made an A")
elif score >=80 and score <= 89 :
    print("Great job you made a B")
elif score > 100:
    print("Invalid score")
    
else:
    print("Sorry, you failed the course with an F")

