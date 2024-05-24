import pymongo
client1=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
myDataBase=client1["Employee1"]
information=myDataBase.informationAboutEmployee
record=[{"firstname":"Raj1","lastname":"kumar","age":21},{"firstname":"Raj2","lastname":"kumar2","age":22}]
information.insert_many(record)