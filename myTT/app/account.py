from app.orm import ORM
from app.util import hash_password, get_price
from app.postion import Position
from app.trade import Trade
import random, string


class Account(ORM):
    tablename = 'accounts'
    fields = ['username', 'password_hash', 'balance', 'api_key']

    def __init__(self, **kwargs):
        self.username = kwargs.get('username')
        self.password_hash = kwargs.get('password_hash')
        self.balance = kwargs.get('balance')
        self.pk = kwargs.get('pk')
        self.api_key = kwargs.get('api_key')

    def generate_api_key(self):
        letters = string.ascii_lowercase
        key = ''.join(random.choice(letters) for i in range(20))
        self.api_key = key
    
    @classmethod
    def api_authenticate(cls, api_key):
        account = Account.one_from_where_clause("WHERE api_key=?", 
                                                    (api_key,))
        if account is None:
            return None
        return account

    @classmethod
    def login(cls, username, password):
        return Account.one_from_where_clause("WHERE username=? AND password_hash=?", 
                                                (username, hash_password(password)))

    def set_password(self, password):
        self.password_hash = hash_password(password)

    def get_positions(self):
    #get all of positions for account
        return Position.all_from_where_clause('WHERE account_pk=?', (self.pk,))

    def get_position_for(self, ticker):
    #take in ticker symbol and get accounts position for that symbol
        ticker = ticker.lower()
        position = Position.one_from_where_clause('WHERE account_pk=? AND ticker=?', (self.pk, ticker))
        if position is None:
            return Position(ticker=ticker, number_shares=0, account_pk=self.pk)
        return position

    def get_trades(self):
    #return all trades by that user
        return Trade.all_from_where_clause("WHERE account_pk=?", (self.pk,))

    def get_trades_for(self, ticker):
    #takes in ticker symbol, return all trades for that symbol
        return Trade.all_from_where_clause('WHERE account_pk=? AND ticker=?' 
                                            (self.pk, ticker))

    def buy(self, ticker, amount):
        """ if balance is greater than equal to amount * current price, 
        updates a Position if it exists, or creates a new Position for
        this ticker in our datase. saves a new Trade object ans updates self.balance"""
        price = get_price(ticker) * amount
        if self.balance < price:
            raise ValueError("Insufficient Funds")
        position = self.get_position_for(ticker)
        print(position.ticker, ": ", position.number_shares)
        position.number_shares += amount
        self.balance -= price
        trade = Trade(ticker=ticker, quantity=amount, type=1,
                    price=price, account_pk=self.pk)
        trade.save()
        position.save()
        self.save()

    def sell(self, ticker, amount):
        """ if current Postion.number_shares is greater than or equal to amount,
        updates a Position, saves a new Trade object and updates self.balance"""
        position = self.get_position_for(ticker)
        price = get_price(ticker) * amount
        if position.number_shares < amount:
            raise ValueError("Insufficient stocks")
        print(position.ticker, ": ", position.number_shares)
        position.number_shares -= amount
        self.balance += price
        trade = Trade(ticker=ticker, quantity=amount, type=0,
                    price=price, account_pk=self.pk)  # changed type from 1 to 0
        trade.save()
        position.save()
        self.save()