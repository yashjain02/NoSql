import pymongo as pymongo
def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://yash_kumar:yashjain@cluster0.oaexh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    col = db['continents']
    cursor=col.find({},{'name':1, 'countries':{'$slice':4}}).sort('countries')
    for CountryName in cursor:
        print(CountryName)
if __name__ == '__main__':
    connectdb()