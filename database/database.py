# database.py
from .table import Table

class Database:
    def __init__(self):
        self.tables = {}

    def create_table(self, name, schema):
        if name in self.tables:
            raise ValueError("Table already exists")
        self.tables[name] = Table(name, schema)
