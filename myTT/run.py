from app import controller
from app import ORM
import os

ORM.dbpath = "ttrader.db"

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'data', 'ttrader.db')

ORM.dbpath = DBPATH
controller.run()