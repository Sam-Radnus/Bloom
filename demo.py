from database.database import Database
from database.table import Schema
from database.join import Join

db = Database()

db.create_table("users", [
    Schema("id", int), Schema("name", str), Schema("age", int), Schema("city", str), Schema("state", "str", True)
    ], **{'unique_attr':('id','name'), 'foreign_attr':('id', 'id')})
# db.tables

db.tables["users"].insert({"id":1, "name":"Alice", "age":25, "city":"NYC"})
db.tables["users"].insert({"id":2, "name":"David", "age":25, "city":"NYC"})
db.tables["users"].insert({"id":3, "name":"David", "age":25, "city":"NYC"})
db.tables["users"].insert({"id":4, "name":"Michael", "age":25, "city":"BLD"})
db.tables["users"].insert({"id":5, "name":"Jason", "age":25, "city":"LAX"})
db.tables["users"].insert({"id":6, "name":"Bruce", "age":25, "city":"GTH"})


tbj = db.tables["users"]

for row in tbj.all():
    print(row.data)

db.create_table("employees", [
    Schema("id", int), Schema("name", str), Schema("title", str), Schema("salary", int)
    ], **{'unique_attr':('id', )}
)

print()


tbl_obj_2 = db.tables["employees"]


tbl_obj_2.insert({"id":1, "name":"Alice", "title":"software engineer", "salary":10000})
tbl_obj_2.insert({"id":3, "name":"David", "title":"QA Analyst", "salary":10000})
tbl_obj_2.insert({"id":8, "name":"John", "title":"software engineer", "salary":10000})


tbj = db.tables["users"]

for row in tbl_obj_2.all():
    print(row.data)

print()

j = Join(tbj, tbl_obj_2)

for row in j.left_join():
    print(row)