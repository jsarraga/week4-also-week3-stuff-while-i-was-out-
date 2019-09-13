
def welcome_menu():
    print()
    print("Welcome to Terminal Trader! ")
    print()
    print("1 - Create Account")
    print("2 - Log In")
    print("3 - Quit")

def mainmenu():
    print()
    print("Main Menu")
    print("1. see balance & positions")
    print("2. deposit money")
    print("3. look up stock price")
    print("4. buy stock")
    print("5. sell stock")
    print("6. trade history")
    print("7. quit")

def get_input():
    print()
    print("Your choice: ", end="")
    return input()

def create_username():
    print("Account Creation ")
    print()
    return input("Username: ")

def create_password():
    print()
    input("Password: ")
    return input("Confirm password: ")

def get_username():
    return input("Username: ")

def get_password():
    return input("Password: ")

def bad_input():
    print()
    print("Bad Input")
    print()

def quit_input():
    print()
    print("Are you finished? y/n ")
    return input()

def your_balance():
    print()
    print("balance: ")

def your_positions():
    print("Positions: ")

def get_amount_input():
    print()
    print("Amount: ", end="")
    return int(input())

def get_ticker_input():
    print()
    print("Stock Ticker: ", end="")
    return input()