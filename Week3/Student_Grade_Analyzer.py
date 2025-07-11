name = input("Enter the name of the student: ")
grade = input("Enter the grade of the student: ")
subject = input("Enter the subject: ")
score = int(input("Enter the score of the corresponding student: "))

if score >= 90 and score <= 100:
    print(f"Excellent job {name}, you made an A")
elif score >= 80 and score <= 89:
    print(f"Great job {name}, you made a B")
elif score >=70 and score <= 79:
    print(f"Try Harder {name}, you made a C")
elif score >= 60 and score <= 69:
    print(f"Needs improvement {name}, you made a D")
else:
    print("Sorry, you failed the course with an F")