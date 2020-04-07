from array import array

from bson import ObjectId
from pymongo import MongoClient



fh =open('/home/arnold/mongopw','r')
cnt = fh.readline()
cluster = MongoClient(cnt)


#cluster = MongoClient('mongodb+srv://dbUserX:mOH8td9lUvFkzcQV@cluster0-iub1a.mongodb.net/test')

print(cluster.list_database_names())




print(cluster['thoronka'].list_collection_names())

print(cluster['thoronka']['ls'].count_documents({}))

mydb = cluster['thoronka']
mycol = mydb['ls']

mycolshort = cluster['thoronka']['ls']

mycol.insert_one({  'shift': 300})
mycolshort.insert_one({ 'date': 'date howto'})


print(cluster['thoronka']['ls'].count_documents({}))
print('sdsds')

data = {'name':'piet'}


def insert_data(data):
    """
    :param data:
    :return:
    """
    document = mycol.insert_one(data)
    return document.inserted_id

def update_or_create(document_id, data):
    """
    :param document_d:
    :param data:
    :return:
    """
    document = mycol.update_one({"_id": ObjectId(document_id)},{"$set":data},upsert=True)
    return 1


def get_single_data(document_id):
    """

    :param document_id:
    :return:
    """
    data = mycol.find_one({"_id":ObjectId(document_id)})
    return data

def get_multiple_data():
    """

    :return:
    """
    array = mycol.find()


def remove_one_data(document_id):
    """

    :param document_id:
    :return:
    """
    result = mycol.delete_one({"_id":ObjectId(document_id)})
    return result


# close database/collection
cluster.close()

#data = {"name": "400XX"}
#document_id = insert_data(data)
#print(document_id)
newdata = {"name":"400---"}
outcome = update_or_create('5e8c7068b95a5e99434065b1',newdata)
print(outcome)
found_data =get_single_data('5e8c7068b95a5e99434065b1')
print(found_data)

I put stuf









