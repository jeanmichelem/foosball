import config
from pymongo import MongoClient

user_db = None
def database_connect(host=config.DB_HOST, port=27017):
    global user_db
    print "connecting pymongo"
    client = MongoClient(host, port)
    print "client: ", client
    user_db = client[config.DB_NAME]
    print "user db:", user_db