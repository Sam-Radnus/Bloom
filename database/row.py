# row.py
class Row:
    def __init__(self, data: dict):
        self.data = data

    def get(self, field):
        return self.data.get(field)

    def update(self, updates: dict):
        self.data.update(updates)
