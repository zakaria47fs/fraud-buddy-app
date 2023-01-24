from pymongo import MongoClient
from urllib.parse import quote_plus
import configuration as cfg
import logging


class MongoService:

    def __init__(self):
        try:
            host = cfg.db["host"]
            port = cfg.db["port"]
            database_name = cfg.db["dbname"]

            uri = "mongodb://%s:%s" % (host, port)
            mongo_client = MongoClient(uri, connect=False)
            self._database = mongo_client[database_name]
                    
        except Exception as ex:
            logging.error(ex)

    def add_item_db(self, collection_name, data):
        self._database[collection_name].insert_one(data)

    def get_item_db(self, collection_name, item_id):
        return self._database[collection_name].find_one({"_id": item_id})

    def get_all_items_db(self, collection_name):
        return self._database[collection_name].find({})

    def filter_items_db(self, collection_name, filter):
        return self._database[collection_name].find(filter)

    def update_item_db(self, collection_name, item_id, data):
        self._database[collection_name].update_one(
                                            {"_id": item_id},
                                            {"$set": data}
                                        )

    def remove_item_db(self, collection_name, item_id):
        self._database[collection_name].delete_one({"_id": item_id})

