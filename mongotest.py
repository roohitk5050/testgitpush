import pymongo
client = pymongo.MongoClient("mongodb+srv://Rohit:roohitk5050@rohit.zu0o9db.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name":"Rohit",
    "email":"roohitk5050@gmail.com",
    "surname":"kulkarni"
}
db1=client['mongodb']
coll=db1['test']
coll.insert_one(d)