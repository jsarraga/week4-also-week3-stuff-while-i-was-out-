from unittest import TestCase
from app import Account, ORM
from data import schema, seed
import os

DIR = os.path.dirname(__file__)
DBFILENAME = "_test.db"
DBPATH = os.path.join(DIR, DBFILENAME)

ORM.dbpath = DBPATH

class TestAccount(TestCase):

    def setUp(self):
        schema(DBPATH)
        seed(DBPATH)

    def tearDown(self):
        os.remove(DBPATH)

    def test_login(self):
        mike = Account.login("mike_bloom", "password")
        self.assertIsNotNone(mike, "account and password find data")
        self.assertIsInstance(mike, Account)
        self.assertEqual(mike.balance, 10000.00)
    
    def testOnePosition(self):
        account = Account(username="Justin", password_hash="password", balance=50000)
        self.assertEqual(account.username, "Justin")
        self.assertEqual(account.password_hash, "password")
        self.assertEqual(account.balance, 50000)
        self.assertIsInstance(account, Account)

    def testSave(self):
        account = Account(username="Justin", password_hash="password", balance=50000)
        account.save()
        self.assertEqual(account.pk, 2)
        self.assertEqual(account.username, "Justin")
        self.assertEqual(account.password_hash, "password")
        self.assertEqual(account.balance, 50000)
        self.assertIsInstance(account, Account)

        account =  Account(pk=2, username="Justin", password_hash="password1", balance=25000)
        account.save()
        self.assertEqual(account.pk, 2)
        self.assertEqual(account.username, "Justin")
        self.assertEqual(account.password_hash, "password1")
        self.assertEqual(account.balance, 25000)
        self.assertIsInstance(account, Account)

    def testAPIKey(self):
        account = Account(pk=2, username="Justin", password_hash="password", balance=50000)
        api_key = account.generate_api_key()
        account.save()
        test = Account.one_from_where_clause("WHERE api_key=?", (account.api_key,))
        self.assertEqual(test, api_key)

    def testApiAuthenticate(self):
        account = Account(pk=2, username="Justin", password_hash="password", balance=50000)
        api_key = account.generate_api_key()
        account.save()
        test = account.api_authenticate(api_key)
        self.assertAlmostEqual(account, test)