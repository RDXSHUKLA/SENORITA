from pymongo import MongoClient, collection
from pymongo.errors import PyMongoError

# Replace with your actual MongoDB URI
MONGO_DB_URI = "mongodb+srv://SHASHANK:STRANGER@shashank.uj7lold.mongodb.net/?retryWrites=true&w=majority"

# Initialize MongoDB client
client = MongoClient(MONGO_DB_URI)
main_db = client["MUKESH_ROBOT"]
MukeshXdb = main_db

def get_collection(name: str) -> collection:
    """Get the collection from the database."""
    return MukeshXdb[name]

class MongoDB:
    """Class for interacting with the Bot database."""

    def __init__(self, collection) -> None:
        self.collection = MukeshXdb[collection]

    def insert_one(self, document):
        result = self.collection.insert_one(document)
        return repr(result.inserted_id)

    def find_one(self, query):
        result = self.collection.find_one(query)
        return result if result else False

    def find_all(self, query=None):
        query = query or {}
        return list(self.collection.find(query))

    def count(self, query=None):
        query = query or {}
        return self.collection.count_documents(query)

    def delete_one(self, query):
        self.collection.delete_many(query)
        return self.collection.count_documents({})

    def replace(self, query, new_data):
        old = self.collection.find_one(query)
        _id = old["_id"]
        self.collection.replace_one({"_id": _id}, new_data)
        new = self.collection.find_one({"_id": _id})
        return old, new

    def update(self, query, update):
        result = self.collection.update_one(query, {"$set": update})
        new_document = self.collection.find_one(query)
        return result.modified_count, new_document

    @staticmethod
    def close():
        client.close()

def __connect_first():
    db = MongoDB("test")
    db.insert_one({"test": "value"})  # Example operation

# Example usage:
# __connect_first()
