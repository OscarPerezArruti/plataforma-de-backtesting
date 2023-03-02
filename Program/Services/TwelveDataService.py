import requests
from .UtilitiesServices import utilitiesServices
from Config import *
import logging
import json

log = logging.getLogger(__name__)

class twelveDataService:
    """
    A class representing the interface needed in order
    to use TwelveData API.

    Attributes
    ----------
    api_key : str
        Api key of TwelveData API
    utilities : utilitiesServices
        Class to use auxiliry methods
    baseUrl : str
        Base url of every API call

    Methods
    -------
    def time_series(symbol,interval,**kwargs):



    """

    def __init__(self) -> None:
        self.api_key = '5a0f7179cffa430d84ab153c6c03b604'
        self.utilities = utilitiesServices()
        self.baseUrl = "https://api.twelvedata.com/"

    def __doPost__(self, url, payload={}, headers={}):
      if headers == {}:
        headers = {
          'api_key': self.api_key
        }
      else:headers = headers
      if payload != {}: payload = payload
      res = json.loads(requests.request("GET", url, headers=headers, data=payload).text)
      log.debug(res)
      if res.get("status") != None and  res["status"] == "error":
        raise twelveDataBadRequest(res["message"])
      return res

    def __doPostTwelveData__(self,endpoint,**kwargs):
        """
        
        """

        try:
          self.utilities.checkTwelveDataEndpoint(endpoint=endpoint)
          if kwargs == {}:
            raise twelveDataNoParams() 
          kwargs["apikey"] = self.api_key
          self.utilities.checkTwelveRequiredParams(endpoint,kwargs)
          self.utilities.checkTwelveDataParameters(endpoint,kwargs)
          
          httpURL = self.utilities.makeTwelveDataEndpoint(url=self.baseUrl,endpoint=endpoint,params=kwargs)
          res = self.__doPost__(httpURL)
          return res
        except twelveDataInvalidEndpoint as e:
          log.error(e.message)
          return "NO DATA"
        except twelveDataInvalidParam as e:
          log.error(e.message)
          return "NO DATA"
        except twelveDataBadRequest as e:
          log.error(e.message)
          return "NO DATA"
        except twelveDataRequieredParam as e:
          log.error(e.message)
          return "NO DATA"
        except twelveDataNoParams as e:
          log.error(e.message)
          return "NO DATA"
        except Exception as e:
          log.error(e)
          return "NO DATA"
        
