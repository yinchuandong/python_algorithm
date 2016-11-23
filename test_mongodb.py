from pymongo import MongoClient
from bson.dbref import DBRef
from pymongo.son_manipulator import AutoReference, NamespaceInjector

client = MongoClient()
db = client.mytest
# for auto dereference
db.add_son_manipulator(NamespaceInjector())
db.add_son_manipulator(AutoReference(db))

peter = {'name': 'peter'}
marry = {'name': 'marry'}
john = {'name': 'john'}
db.users.remove()
db.contacts.remove()
db.users.insert([peter, marry, john])
users = db.users.find()
for user in users:
    print user

db.contacts.insert({
    'user_id': DBRef('users', peter['_id']),
    'friend_id': DBRef('users', john['_id']),
})

contacts = db.contacts.find()
for contact in contacts:
    user_name = contact['user_id']['name']
    friend_name = contact['friend_id']['name']
    # user_name = db.dereference(contact['user_id'])['name']
    # friend_name = db.dereference(contact['friend_id'])['name']
    print user_name, friend_name
