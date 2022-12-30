from pymongo import MongoClient, ReadPreference
from lib.settings import mongo_uri, mongo_dbname


mongo_client = MongoClient(mongo_uri)
primary_db = mongo_client[mongo_dbname]
secondary_db = mongo_client.get_database(mongo_dbname, read_preference=ReadPreference.SECONDARY)


class DB:
    def __init__(self, collection):
        self.collection = collection

    def insert_document(self, insert_query):
        primary_db[self.collection].insert_one(insert_query)

    def upsert_document(self, search_query, update_query):
        primary_db[self.collection].update_one(search_query, update_query, True)
