
from pymongo import MongoClient

fh =open('/home/arnold/mongopw','r')
cnt = fh.readline()
print(cnt)


c = MongoClient(cnt)










