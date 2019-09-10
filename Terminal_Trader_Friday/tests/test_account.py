import os
from unittest import TestCase

from app import ORM
from app import Account
from data import schema, seed

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
        mike_bloom = Account.login("mike_bloom", 'password')
        self.assertIsNotNone(mike_bloom, "account and password find data")
        self.assertIsInstance(mike_bloom, Account, "login returns Account object")
        self.assertEqual(mike_bloom.balance, 10000.00)