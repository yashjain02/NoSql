# Get the list of continents with number of countries in them
import pymongo as pymongo
def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://yash_kumar:yashjain@cluster0.oaexh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    col = db['continents']
    cursor=col.aggregate([{'$project': {'name': 1,'_id':0, 'numberOfCountries': { '$size': '$countries' }}}])
    for CountryName in cursor:
        print(CountryName)
if __name__ == '__main__':
    connectdb()
