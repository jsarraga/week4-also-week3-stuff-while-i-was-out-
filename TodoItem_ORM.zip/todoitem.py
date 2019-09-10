import sqlite3
from .orm import ORM


class TodoItem(ORM):
    dbpath = ""
    tablename = "todoitems"
    fields = ['title', 'description', 'complete']

    def __init__(self, **kwargs):
        self.pk = kwargs.get('pk')
        self.title = kwargs.get('title')
        self.description = kwargs.get('description')
        self.complete = kwargs.get('complete')

    @classmethod
    def all(cls, complete=None):
        if complete is None:
            return cls.all_from_where_clause()
        elif bool(complete) is True:
            return cls.all_from_where_clause('WHERE complete=?', (1,))
        elif bool(complete) is False:
            return cls.all_from_where_clause('WHERE complete=?', (0,))
            
    def __repr__(self):
        pattern = "<TodoItem: title={}, pk={}>"
        return pattern.format(self.title, self.pk)
