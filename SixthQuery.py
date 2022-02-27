# Get the countries which has "u" in there name and more 100000 people inside
import pymongo as pymongo
def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://yash_kumar:<password>@cluster0.oaexh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    col = db['countries']
    cursor=col.find({'name': {'$regex': 'u','$options':'i'}, 'population':{'$gt':100000}},{'name':1, '_id':0, 'population':1})
    for CountryName in cursor:
        print(CountryName)
if __name__ == '__main__':
    connectdb()
