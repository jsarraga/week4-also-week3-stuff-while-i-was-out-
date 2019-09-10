from app import ORM


class Position(ORM):
    dbpath = ""
    tablename = "positions"
    fields = ['ticker', 'number_shares', 'account_pk']

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.ticker = kwargs.get('ticker')
        self.number_shares = kwargs.get('number_shares')
        self.account_pk = kwargs.get('account_pk')
