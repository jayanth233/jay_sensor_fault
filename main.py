from sensor.configaration.mongo_db_connection import MongoDBClient


if __name__=='__main__':
    mongodb_clinet=MongoDBClient()
    print("collection names : ",mongodb_clinet.database.list_collection_names())