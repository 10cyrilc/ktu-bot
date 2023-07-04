from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)

db = client[Config.SESSION_NAME]

collection = db["test-hashes"]


def add_hash(hash):
    new_item = {
        "hash": hash
    }
    post_id = collection.insert_one(new_item).inserted_id
    return post_id


def get_hash(hash):
    item = collection.find_one({"hash": hash})
    return True if item else False
