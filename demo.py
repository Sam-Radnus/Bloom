from database.database import Database

db = Database()

db.create_table("users", ["id", "name", "age", "city"])
# db.tables

def remove_odd_ids(val):
    return val % 2 == 1


db.tables["users"].insert({"id":1, "name":"Alice", "age":25, "city":"NYC"})
db.tables["users"].insert({"id":2, "name":"David", "age":25, "city":"NYC"})
db.tables["users"].insert({"id":3, "name":"Alex", "age":25, "city":"NYC"})
db.tables["users"].insert({"id":4, "name":"Michael", "age":25, "city":"BLD"})
db.tables["users"].insert({"id":5, "name":"Jason", "age":25, "city":"LAX"})
db.tables["users"].insert({"id":6, "name":"Bruce", "age":25, "city":"GTH"})

tbj = db.tables["users"]
print(tbj.all())
print()
print("Before Deletion")
for row in tbj.all():
    print(row.data)


tbj.delete(remove_odd_ids, 'id')

print("After Deletion")
for row in tbj.all():
    print(row.data)

