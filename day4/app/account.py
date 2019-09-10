from app import ORM, Trade, Position
from .util import hash_password, get_price


class Account(ORM):
    dbpath = ""
    tablename = "accounts"
    fields = ['username', 'password_hash', 'balance', 'contact', 'email']

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.username = kwargs.get('username')
        self.password_hash = kwargs.get('password_hash')
        self.balance = kwargs.get('balance')
        self.contact = kwargs.get('contact')
        self.email = kwargs.get('email')

    def get_positions(self):
        """ return all Positions where account_pk == self.pk. 
        returns a list of Position objects """
        return Position.all_from_where_clause("WHERE account_pk=?",(self.pk,))

    def get_position_for(self, ticker):
        """ return Position for a given ticker symbol for this Account.
        returns a list of Position objects """
        return Position.all_from_where_clause(
                        "WHERE account_pk=? AND ticker=?", (self.pk, ticker))

    def get_trades(self):
        """ return all Trades where account_pk == self.pk. 
        returns a list of Trade objects """
        return []

    def get_trades_for(self, pk):
        """ return all Trades where account_pk == self.pk. 
        returns a list of Trade objects """
        return []

    def buy(self, ticker, amount):
        """ if balance is greater than or equal to amount * current price, 
        updates a Position if it exists, or creates a new Position for this 
        ticker in our database. saves a new Trade object 
        and updates self.balance"""
        pass

    def sell(self, ticker, amount):
        """ if current Position.number_shares is greater than or equal to amount, 
        updates a Position if it exists, or creates a new Position for this 
        ticker in our database. saves a new Trade object 
        and updates self.balance"""
        pass
