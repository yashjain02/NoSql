import pymongo as pymongo
def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://yash_kumar:yashjain@cluster0.oaexh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    col = db['countries']
    cursor=col.find({'name': {'$regex': 'u','$options':'i'}, 'population':{'$gt':100000}},{'name':1, '_id':0, 'population':1})
    for i in cursor:
        print(i)
if __name__ == '__main__':
    connectdb()
