# Get all the countries where a letter or word is given
import pymongo as pymongo
def print_hi(name):
         print(f'Hi, {name}')
def connectdb(wordGiven):
    client = pymongo.MongoClient(
        "mongodb+srv://yash_kumar:yashjain@cluster0.oaexh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    col = db['countries']
    cursor=col.find({'name': {'$regex': wordGiven,'$options':'i'}},{'name':1, '_id':0})
    for CountryName in cursor:
        print(CountryName)
if __name__ == '__main__':
    print_hi('PyCharm')
    wordGiven = str(input("Enter the letter or word to be searched"))
    connectdb(wordGiven)
