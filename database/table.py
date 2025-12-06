# table.py
from .row import Row

class Table:
    def __init__(self, name, schema):
        self.name = name
        self.schema = schema  # List of field names
        self.rows = []

    def insert(self, row_data: dict):
        if set(row_data.keys()) != set(self.schema):
            raise ValueError("Row does not match table schema")
        self.rows.append(Row(row_data))
    

    def filter(self, condition, attr) -> list:
        ans = []
        for row in self.rows:
            row_data = row.data
            if attr not in row_data:
                print(f"column {attr} not present in {row_data}")
                continue
            
            if condition(row.data.get(attr)):
                ans.append(row)
        return ans
    
    def delete(self, condition, attr):
        for row in self.filter(condition, attr):
            self.rows.remove(row)

    def all(self):
        return self.rows

