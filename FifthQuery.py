#Get all teh countries order by number of people, first less populated and last highly populated, I have removed my password for security purpose
import pymongo as pymongo
def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://yash_kumar:<password>@cluster0.oaexh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    col = db['countries']
    cursor=col.find({},{'_id':0, 'name':1, 'population':1}).sort('population')
    for i in cursor:
        print(i)
if __name__ == '__main__':
    connectdb()
