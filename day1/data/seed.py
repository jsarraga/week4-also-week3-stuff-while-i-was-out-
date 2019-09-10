import sqlite3
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'todo.db')

def seed(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as connection:
        cur = connection.cursor()

        items = [
            ["Do Hackerrank Problems", "Gotta keep up with these...", 0],
            ["Complete Homework", None, 0],
            ["Get Lunch", "Why is everything so expensive around here?", 1]
        ]

        SQL = """INSERT INTO todoitems (title, description, complete) VALUES
        (?, ?, ?)"""

        for item in items:
            cur.execute(SQL, (item[0], item[1], item[2]))
