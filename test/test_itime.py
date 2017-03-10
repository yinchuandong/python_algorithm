from pymongo import MongoClient
from bson.dbref import DBRef
from pymongo.son_manipulator import AutoReference, NamespaceInjector
import json

client = MongoClient()
db = client.mytest
# for auto dereference
db.add_son_manipulator(NamespaceInjector())
db.add_son_manipulator(AutoReference(db))

with open('api/event.json') as f:
    event = json.load(f)
    db.events.remove()
    db.events.insert(event)

events = db.events.find()[0]
del events['_id']
events['userUid'] = 'wangjiewen'
db.events.insert(events)

# events = db.events.find()
# print events[0]
# for event in events:
#     print event
