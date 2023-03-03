from Services import *


objt = twelveDataService()
res = objt.__doPostTwelveData__(endpoint="time_series",symbol="AAPL",interval="1min",outputsize=1)
quote = objt.__doPostTwelveData__(endpoint="quote",symbol="AAPL")
 