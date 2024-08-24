from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb+srv://gawandeabhishek690:5CKipzzA9ZkrKTpC@cluster1.ml1lv.mongodb.net/")
db = client["usersData"]

# Collections
users_collection = db["users"]
ids_collection = db["linked_ids"]
