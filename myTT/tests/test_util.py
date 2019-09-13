from unittest import TestCase
from app import util

class testUtil(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetPrice(self):
        response = util.get_price("tsla")
        self.assertIsInstance(response, float)

    def testHashPass(self):
        hashed_pass = util.hash_password('password')
        t = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
        self.assertEqual(hashed_pass, t)