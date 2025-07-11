user_trial = 0
number_attempts = 3

Stored_username = "Olive7"
Stored_password = "3757"

while user_trial != number_attempts:
    username = input("Username: ")
    password = input("Password: ")
    if username == Stored_username and password == Stored_password:
        print("Login Successful!")
        break
    else:
        print("Login Unsuccessful, Try again!")
    user_trial = user_trial + 1
    if user_trial == number_attempts:
        print(f"Dear customer, you have entered the wrong password {user_trial} times. Account blocked")