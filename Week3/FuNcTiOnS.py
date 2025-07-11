# def name():
#    fname = "Olive"
#    print(fname)
# name()

# def nameCall(name):
#     return f'{name} is entered'
#
# fname = input("Enter name: ")
# print(nameCall(fname))

DATABASE = {}

def login(username,password):
   if username ==DATABASE['Username'] and password == DATABASE['Password']:
       message = 'Login Successful'
       print(message)
   else:
       message = 'Login Unsuccessful'
       print(message)

def registration(username,email,password):
    if username and email and password:
        DATABASE['Username'] = username
        DATABASE['Password'] = password
        DATABASE['Email'] = email
    print('Registration Successful')

def main():
    while True:
        print("1. Login")
        print("2. Register")
        userInput = input('Enter(1/2): ')
        match userInput:
            case '1':
                username = input('Username: ')
                password = input('Password: ')
                login(username,password)

            case '2':
                username = input('Username: ')
                email = input('Email: ')
                password = input('Password: ')
                registration(username,email,password)

main()