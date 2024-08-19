from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from pymongo import collection
from pymongo.errors import PyMongoError

# Replace with your actual MongoDB URI
MONGO_DB_URI = "mongodb+srv://SHASHANK:STRANGER@shashank.uj7lold.mongodb.net/?retryWrites=true&w=majority"

# Initialize MongoDB client
mongo = MongoCli(MONGO_DB_URI)
Mukeshdb = mongo.MUK_ROB

async def get_collection(name: str) -> collection:
    """Get the collection from the database."""
    return Mukeshdb[name]

class MongoDB:
    """Class for interacting with the Bot database."""

    def __init__(self, collection) -> None:
        self.collection = Mukeshdb[collection]

    async def insert_one(self, document):
        result = await self.collection.insert_one(document)
        return repr(result.inserted_id)

    async def find_one(self, query):
        result = await self.collection.find_one(query)
        return result if result else False

    async def find_all(self, query=None):
        query = query or {}
        return [doc async for doc in self.collection.find(query)]

    async def count(self, query=None):
        query = query or {}
        return await self.collection.count_documents(query)

    async def delete_one(self, query):
        await self.collection.delete_many(query)
        return await self.collection.count_documents({})

    async def replace(self, query, new_data):
        old = await self.collection.find_one(query)
        _id = old["_id"]
        await self.collection.replace_one({"_id": _id}, new_data)
        new = await self.collection.find_one({"_id": _id})
        return old, new

    async def update(self, query, update):
        result = await self.collection.update_one(query, {"$set": update})
        new_document = await self.collection.find_one(query)
        return result.modified_count, new_document

    async def close(self):
        await mongo.close()

async def __connect_first():
    db = MongoDB("test")
    await db.insert_one({"test": "value"})  # Example operation

# Example usage:
# import asyncio
# asyncio.run(__connect_first())
