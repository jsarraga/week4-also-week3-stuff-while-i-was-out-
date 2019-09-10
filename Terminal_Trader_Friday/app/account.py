from app.orm import ORM
from app.trade import Trade
from app.position import Position
from .util import hash_password, get_price


class Account(ORM):
    dbpath = ""
    tablename = "accounts"
    fields = ['username', 'password_hash', 'balance']#, 'contact', 'email']

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.username = kwargs.get('username')
        self.password_hash = kwargs.get('password_hash')
        self.balance = kwargs.get('balance')
        # self.contact = kwargs.get('contact')
        # self.email = kwargs.get('email')

    @classmethod
    def login(cls, username, password):
        return cls.one_from_where_clause("WHERE username=? AND password_hash=?",
                                        (username, hash_password(password)))

    def set_password(self, password):
        self.password = hash_password(password)

    def get_positions(self):
        """ return all Positions where account_pk == self.pk. 
        returns a list of Position objects """
        return Position.all_from_where_clause("WHERE account_pk=?",(self.pk,))

    def get_position_for(self, ticker):
        """ return Position for a given ticker symbol for this Account.
        returns a list of Position objects """
        ticker = ticker.lower()
        position = Position.all_from_where_clause(
                        "WHERE account_pk=? AND ticker=?", (self.pk, ticker))
        if not Position:
            return Position(ticker=ticker,number_shares=0,account_pk=self.pk)
        return position

    def get_trades(self):
        """ return all Trades where account_pk == self.pk. 
        returns a list of Trade objects """
        return Trade.all_from_where_clause("WHERE account_pk=?", (self.pk,))

    def get_trades_for(self, ticker):
        """ return all Trades where account_pk == self.pk. 
        returns a list of Trade objects """
        return Trade.all_from_where_clause("WHERE account_pk=? AND ticker=?", 
                                            (self.pk, ticker))

    def buy(self, ticker, amount):
        """ if balance is greater than or equal to amount * current price, 
        updates a Position if it exists, or creates a new Position for this 
        ticker in our database. saves a new Trade object 
        and updates self.balance"""
        # check current price
        price = get_price(ticker) * amount
        # check our balance
        if self.balance < price:
            raise ValueError("Insufficient Funds")
        # get our current position
        position = self.get_position_for(ticker)
        # add shares to position
        position.number_shares += amount
        # subtract from self.balance
        self.balance -= price
        # save the Trade
        trade = Trade(ticker=ticker,quantity=amount,type=1,
                      price=price,account_pk=self.pk)
        trade.save()
        # save the Position, save the Account
        position.save()
        self.save()

    def sell(self, ticker, amount):
        """ if current Position.number_shares is greater than or equal to amount, 
        updates a Position if it exists, or creates a new Position for this 
        ticker in our database. saves a new Trade object 
        and updates self.balance"""
        pass
