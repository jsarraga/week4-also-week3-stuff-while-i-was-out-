from app.account import Account
from app.util import hash_password, get_price
from app import view
import time


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
    new_account.generate_api_key()
    new_account.save()
    view.login_menu()
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
    while True:
        view.mainmenu()
        selection = view.get_input()
        if selection == "8":
            break
        elif selection == "1":
            view.your_balance()
            print(account.balance) 
            view.your_positions()
            pos = account.get_positions()
            for position in pos:
                print(position.ticker, ":", position.number_shares)
        elif selection == "2":
            amount = int(view.get_amount_input())
            account.balance += amount
            view.your_balance()
            print(account.balance) 
            account.save()
        elif selection == "3":
            ticker = view.get_ticker_input()
            ticker = ticker.lower()
            print("Price: $", get_price(ticker))
        elif selection == "4":
            ticker = view.get_ticker_input()
            amount = int(view.get_amount_input())
            account.buy(ticker, amount)
        elif selection == "5":
            ticker = view.get_ticker_input()
            amount = int(view.get_amount_input())
            account.sell(ticker, amount)
        elif selection == "6":
            trades = account.get_trades()
            for trade in trades:
                date = time.ctime(int(trade.date))
                if trade.type == 1:
                    trade.type = "bought"
                if trade.type == 0:
                    trade.type = "sold"
                print(date,":", trade.ticker.upper(), ":",trade.type,trade.quantity)
        elif selection == "7":
            print("Your API Key: ", account.api_key)

    
    
        


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