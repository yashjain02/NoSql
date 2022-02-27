#Add the new attribute population in countries, population data is taken from wikipedia and its approximate
import pymongo as pymongo
def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://yash_kumar:<password>@cluster0.oaexh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    col = db['countries']
    col.updateMany({}, {'$set': {"population": 'null'}})
    col.update_one({'name':'USA'},{'$set':{'population': 332915073}})
    col.update_one({'name': 'Greece'}, {'$set': {'population': 10720000}})
    col.update_one({'name': 'germany'}, {'$set': {'population': 832400000}})
    col.update_one({'name': 'South africa'}, {'$set': {'population': 593100000}})
    col.update_one({'name': 'India'}, {'$set': {'population': 14000000000}})
if __name__ == '__main__':
    connectdb()
