from pymongo import MongoClient
from config import Config
from datetime import date
client = MongoClient(Config.MONGO_URI)

db = client[Config.SESSION_NAME]

collection = db["hashes"]


def add_hash(hash):
    new_item = {
        "hash": hash,
        "date": str(date.today())
    }
    post_id = collection.insert_one(new_item).inserted_id
    return post_id


def get_hash(hash):
    item = collection.find_one({"hash": hash})
    return True if item else False
