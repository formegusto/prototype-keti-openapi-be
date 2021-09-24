import pymongo
import json

mongo_info_file = open("auth/mongo_info.json", "r", encoding="utf8")
mongo_info = json.load(mongo_info_file)

MONGO_CONN = pymongo.MongoClient("mongodb://{}".format(mongo_info['HOST']))


def conn_mongodb():
    global MONGO_CONN
    try:
        MONGO_CONN.admin.command("ismaster")
    except:
        MONGO_CONN = pymongo.MongoClient(
            "mongodb://{}".format(mongo_info['HOST']))

    return MONGO_CONN
