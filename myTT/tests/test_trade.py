from unittest import TestCase
from app import ORM, Trade
from data import schema, seed
import os

DIR = os.path.dirname(__file__)
DBFILENAME = "_test.db"
DBPATH = os.path.join(DIR, DBFILENAME)

ORM.dbpath = DBPATH

class TestTrade(TestCase):

    def setUp(self):
        schema(DBPATH)
        seed(DBPATH)

    def tearDown(self):
        os.remove(DBPATH)

    def testTrade(self):
        trade = Trade()
        self.assertEqual(trade.tablename, "trades")
        self.assertEqual(trade.fields, 
                        ['ticker', 'quantity', 'type', 'price', 'date', 'account_pk'])
        self.assertIsInstance(trade, Trade)
        trade1 = Trade(ticker="ibm", quantity=5, type=1, price=400, date=5000, account_pk=20)
        self.assertEqual(trade1.ticker, "ibm")
        self.assertEqual(trade1.quantity, 5)
        self.assertEqual(trade1.type, 1)
        self.assertEqual(trade1.price, 400)
        self.assertEqual(trade1.date, 5000)
        self.assertEqual(trade1.account_pk, 20)

    def testTrade(self):
        trade = Trade(ticker='aaaaaaaaa', quantity=12, type=0)
        trade.save()
        test = Trade.one_from_where_clause("WHERE ticker=?", ('aaaaaaaaa',))
        self.assertIsInstance(test, Trade)
        self.assertEqual(test.quantity, 12)
      