# -*- coding:utf-8 -*-


import pymongo

from settings.base import SOURCE_DB, SOURCE_PORT, SOURCE_DBNAME


client = pymongo.MongoClient(SOURCE_DB, SOURCE_PORT)
metadb = client[SOURCE_DBNAME]
