# table.py
from .row import Row

class Schema:
    def __init__(self, name, type, optional = False):
        self.name = name
        self.type = type
        self.optional = optional


class Table:
    def __init__(self, name, schema, **kwargs):
        print(kwargs)
        self.name = name
        self.schema:list[Schema] = schema  # {'id': int, 'name': str}
        self.schema_fields = { s.name:s for s in schema }
        self.unique_attr = set(kwargs.get('unique_attr'))
        self.foreign_attr = kwargs.get('foreign_attr')
        self.keys = set()
        self.rows = []

        # check constraint that key is not null
        if all(self.schema_fields[attr].optional for attr in self.unique_attr):
            raise Exception(
                'all values of key cannot have null constraint atleast one of them should have not null'
            )

    def insert(self, row_data: dict):
        # Check missing columns
        '''
        missing = set(self.schema.keys()) - set(row_data)
        if missing:
            raise ValueError(f"Missing fields: {missing}")

        # Check no extra fields
        extra = set(row_data) - set(self.schema)
        if extra:
            raise ValueError(f"Unexpected fields: {extra}")
        
        '''

        # Type validation & construct unique key
        key = []
        for field_name, field_object in self.schema_fields.items():
            
            value = row_data.get(field_name)
            expected_type = field_object.type
            
            if field_object.optional and value is None:
                continue

            if not isinstance(value, expected_type):
                raise TypeError(
                    f"Field '{field_name}' expected type {expected_type.__name__}, "
                    f"got {type(value).__name__}"
                )
            
            if field_name in self.unique_attr:
                key.append(value)

        key = tuple(key)
        if key in self.keys:
            raise ValueError(f"Unique constraint violation on fields {self.unique_attr}: {key}")

        self.keys.add(key)
        self.rows.append(Row(row_data))

    def filter(self, condition, attr):
        if attr not in self.schema:
            raise KeyError(f"Field '{attr}' does not exist in table '{self.name}'")

        return [row for row in self.rows if condition(row.data[attr])]

    def delete(self, condition, attr):
        self.rows = [row for row in self.rows if not condition(row.data.get(attr))]

    def all(self):
        return self.rows
