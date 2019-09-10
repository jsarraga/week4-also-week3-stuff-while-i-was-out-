import sqlite3
import os

DIR = os.path.dirname(__file__)
DBFILENAME = "ttrader.db"
DBPATH = os.path.join(DIR, DBFILENAME)


def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()
        DROPSQL = "DROP TABLE IF EXISTS {tablename};"

        cur.execute(DROPSQL.format(tablename="accounts"))

        SQL = """CREATE TABLE accounts(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(16) NOT NULL,
                password_hash VARCHAR(128),
                balance FLOAT,
                UNIQUE(username)
            );"""

        cur.execute(SQL)

        cur.execute(DROPSQL.format(tablename="positions"))

        SQL = """CREATE TABLE positions(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            account_pk INT,
            ticker VARCHAR(4) NOT NULL,
            number_shares INT,
            FOREIGN KEY(account_pk) REFERENCES accounts(pk),
            UNIQUE(account_pk, ticker)
            );"""

        cur.execute(SQL)

        cur.execute(DROPSQL.format(tablename="trades"))

        SQL = """CREATE TABLE trades(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            account_pk INT,
            ticker VARCHAR(4) NOT NULL,
            quantity INT,
            type BOOL,
            price FLOAT,
            date FLOAT,
            FOREIGN KEY(account_pk) REFERENCES accounts(pk)
            );"""

        cur.execute(SQL)