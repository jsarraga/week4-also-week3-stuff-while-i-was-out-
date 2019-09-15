from unittest import TestCase
from app import util, ORM
from data import schema, seed
import os

DIR = os.path.dirname(__file__)
DBFILENAME = "_test.db"
DBPATH = os.path.join(DIR, DBFILENAME)

ORM.dbpath = DBPATH


class testUtil(TestCase):

    def setUp(self):
        schema(DBPATH)
        seed(DBPATH)

    def tearDown(self):
        os.remove(DBPATH)

    def testGetPrice(self):
        response = util.get_price("tsla")
        self.assertIsInstance(response, float)

    def testHashPass(self):
        hashed_pass = util.hash_password('password')
        t = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
        self.assertEqual(hashed_pass, t)