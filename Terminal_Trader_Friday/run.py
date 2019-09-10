#! /usr/bin/env python3

from app import Account
from app import controller
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'data', 'ttrader.db')

Account.dbpath = DBPATH
controller.run()
