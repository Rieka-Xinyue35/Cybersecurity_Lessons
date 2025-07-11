for number_of_times in range(3):
    atm_pin = input("> Please enter pin: ")
    if atm_pin == "9198":
        print("Access Granted! Cashout successful!")
    else:
        print("Too many wrong attempts. Card blocked.")