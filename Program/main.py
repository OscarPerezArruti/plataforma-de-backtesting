from Services import *
from System import *


cred = Credentials()
api_key = cred.get_password(name="api_key",username="api_key")

objt = twelveDataService(api_key)
res = objt.TwelveDataRequest(endpoint="time_series",symbol="AAPL",interval="1day",outputsize=5000,apikey=api_key,pepe="pepe")
#quote = objt.TwelveDataRequest(endpoint="quote",symbol="AAPL")
#symbol = objt.TwelveDataRequest(endpoint="symbol_search",symbol="AAPL")

"""
with baseMongoDbService() as db:
    collection = db.test()
    if res.get("status") != None:
        res.pop("status")
    collection.insert_one(res)
"""
    
    
"""for i in startup_log.find({"hostname": 'ltaudit-tropea'}):
    print(i["hostname"])"""
    
