import pymongo

client = pymongo.MongoClient("mongodb+srv://kkobzar:12345@cluster0.k2acs6d.mongodb.net/?retryWrites=true&w=majority")

db = client["zakhar"]

col = db["zakhar"]

x = col.insert_one("zakhar":{"My test data"})