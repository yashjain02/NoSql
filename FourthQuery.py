#Add the new attribute population in countries, population data is taken from wikipedia and its approximate
import pymongo as pymongo
def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://yash_kumar:<password>@cluster0.oaexh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    col = db['countries']
    col.updateMany({}, {'$set': {"population": 'null'}})
    col.update_one({'name':'USA'},{'$set':{'population': 332403650}})
    col.update_one({'name': 'Greece'}, {'$set': {'population': 10720000}})
    col.update_one({'name': 'germany'}, {'$set': {'population':83240000}})
    col.update_one({'name': 'South africa'}, {'$set': {'population': 59310000}})
    col.update_one({'name': 'India'}, {'$set': {'population': 140000000}})
    col.update_one({'name': 'France'}, {'$set': {'population': 65800000}})
    col.update_one({'name': 'Italy'}, {'$set': {'population': 59550000}})
if __name__ == '__main__':
    connectdb()
