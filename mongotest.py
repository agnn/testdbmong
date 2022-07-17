import pymongo

client = pymongo.MongoClient("mongodb+srv://achowdh:casannova@agnikc.mmtem.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name":"agnik",
    "email":"agnik.009@gmail.com",
    "surname":"chowdhuri"
}

db1 = client['mongotest']
col = db1['test']
col.insert_one(d)