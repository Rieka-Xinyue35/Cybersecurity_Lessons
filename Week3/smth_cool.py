database = {}
print("REGISTRATION")
while True:
    print("1. Login")
    print("2. Register")
    userInput = input('Enter(1/2): ')
    match userInput:
        case '1':
            username = input('Username: ')
            password = input('Password: ')
            print('Login Successful') if username == database['Username'] and database['Password']  else print('Invalid Login')
        case '2':
            username = input('Username: ')
            email = input('Email: ')
            password = input('Password: ')
            if username and email and password:
                database['Username'] = username
                database['Password'] = password
                database['Email'] = email