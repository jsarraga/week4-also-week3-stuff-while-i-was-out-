import sqlite3
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'todo.db')

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as connection:
        cur = connection.cursor()

        SQL = "DROP TABLE IF EXISTS todoitems;"
        cur.execute(SQL)

        SQL = """ CREATE TABLE todoitems (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(128),
            description TEXT,
            complete INTEGER
        );"""
        cur.execute(SQL)
