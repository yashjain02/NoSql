# Get the list of continents with number of countries in them
import pymongo as pymongo
def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://yash_kumar:<password>@cluster0.oaexh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    col = db['continents']
    cursor=col.aggregate([{'$project': {'name': 1,'_id':0, 'numberOfCountries': { '$size': '$countries' }}}])
    for ContinentName in cursor:
        print(ContinentName)
if __name__ == '__main__':
    connectdb()
