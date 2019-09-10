#! /usr/bin/env python3

from app.todoitem import TodoItem
from app import controller
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'data', 'todo.db')

TodoItem.dbpath = DBPATH
controller.run()
