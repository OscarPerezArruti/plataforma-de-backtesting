from Services import *
from System import *


cred = Credentials()
api_key = cred.get_password(name="api_key",username="api_key")

objt = twelveDataService(api_key)
#res = objt.TwelveDataRequest(endpoint="time_series",symbol="AAPL",interval="1min",outputsize=1)
#quote = objt.TwelveDataRequest(endpoint="quote",symbol="AAPL")
#symbol = objt.TwelveDataRequest(endpoint="symbol_search",symbol="AAPL")
print("Hello")