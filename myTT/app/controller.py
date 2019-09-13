from app.account import Account
from app.util import hash_password, get_price
from app import view


def run():
    welcomemenu()

def welcomemenu():
    while True:
        view.welcome_menu()
        selection = view.get_input()
        if selection == "1":
            create_account()
        if selection == "2":
            login()
        if selection == "3":
            return

def create_account():
    username = view.create_username()
    password = view.create_password()
    password_hash = hash_password(password)
    new_account = Account(username=username, password_hash=password_hash, balance=0)
    new_account.save()
    login()
    

def login():
    username = view.get_username()
    password = view.get_password()
    account = Account.login(username, password)
    if account:
        mainmenu(account)
    else:
        view.bad_input()

def mainmenu(account):
    view.mainmenu()
    selection = view.get_input()
    if selection == "7":
        answer = view.quit_input()
        if answer == "y":
            pass # save?
        elif answer == 'n':
            return
    elif selection == "1":
        print(account.balance) 
        print(account.get_positions())
    
        


"""
Sample execution
Welcome to Terminal Trader!
    
    1. create account
    2. login
    3. quit
Your choice: 2

Main Menu:
    1. see balance & positions
    2. deposit money
    3. look up stock price
    4. buy stock
    5. sell stock
    6. trade history
etc.
you should have useful output if a user inputs a stock that does not exist
you should not allow a user to spend money they don't have or sell
shares they don't have
your display of positions or trades should be well-formatted, don't
just print a python list
"""

if __name__ == "__main__":
    run()