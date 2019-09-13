from unittest import TestCase
from app import Trade

class TestTrade(TestCase):

    def testTrade(self):
        trade = Trade()
        self.assertEqual(trade.tablename, "trades")
        self.assertEqual(trade.fileds, 
                        ['ticker', 'quantity', 'type', 'price', 'date', 'account_pk'])
        self.assertIsInstance(trade, Trade)
        trade1 = Trade(ticker="ibm", quantity=5, type=1, price=400, date=5000, account_pk=20)
        self.assertEqual(trade1.ticker, "ibm")
        self.assertEqual(trade1.quantity, 5)
        self.assertEqual(trade1.type, 1)
        self.assertEqual(trade1.price, 400)
        self.assertEqual(trade1.date, 5000)
        self.assertEqual(trade1.account_pk, 20)



    def testTradeSave(self):
        trade = Trade(ticker='aaaaaaaaa', number_shares=12)
        trade.save()
        test = Trade.one_from_where_clause("WHERE ticker=?", ('aaaaaaaaa',))
        self.assertIsInstance(test, Trade)
        self.assertEqual(test.number_shares, 12)