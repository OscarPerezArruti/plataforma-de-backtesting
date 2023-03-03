import requests
from .UtilitiesServices import utilitiesServices
from Exceptions import *
import logging
import json

log = logging.getLogger(__name__)

class baseTwelveDataService:
    """
    A class representing the interface needed in order
    to use TwelveData API.

    Parameters
    ----------
    api_key : str
        Api key of you TwelveData account
    
    Attributes
    ----------
    api_key : str
        Api key of you TwelveData account
    utilities : utilitiesServices
        Class to use auxiliry methods
    baseUrl : str
        Base url of every API call

    Methods
    -------
    @TODO Rellenar los métodos
    """

    def __init__(self,api_key) -> None:
        self.api_key = api_key
        self.utilities = utilitiesServices()
        self.baseUrl = "https://api.twelvedata.com/"

    def doPost(self, url, action="GET",payload={}, headers={}):
      """
        Checks if a given endpoint exists on TwelveData API

        Parameters
        ----------
        url : str
            url where request will be performed
        action : str
            action performed by the HTTP request
        payload : dict
            HTTP request payload
        header : dict
            HTTP request header
            
        Returns
        -------
        dict:Return the data queried 
      """
      if headers == {}: 
        # We set the default header
        headers = {
          'api_key': self.api_key
        }
        
      
      # We make the HTTP Request
      res = json.loads(requests.request(action, url, headers=headers, data=payload).text)
      log.debug(res)
      if res.get("status") != None and  res["status"] == "error":
        raise twelveDataBadRequest(res["message"])
      return res

    def TwelveDataPost(self,endpoint,**kwargs):
        """
        Starts the process of performign a HTTP request to the TwelveData API
        by making some checks like:
          - Checking if the given endpoint is valid
          - Checking ig the requiered parameters of the endpoint were given
          - Checking if the given parameters are allowed on this endpoint
        It also calls a method to construct the url that will be use on the request
      
        At the end, just if all the checks are succeded and with no exceptions raised
        this methods call another method, that will perform the HTTP request.

        Parameters
        ----------
        endpoint : str
            enpoint to be checked
        kwargs : dict
            variable number of parameters 

        Returns
        -------
        dict:Return the data queried 
        
        Exceptions
        ----------
        @TODO Rellenar las excepciones
        
        """

        try:
          self.utilities.checkTwelveDataEndpoint(endpoint=endpoint)
          if kwargs == {}:
            raise twelveDataNoParams() 
          kwargs["apikey"] = self.api_key
          self.utilities.checkTwelveRequiredParams(endpoint,kwargs)
          self.utilities.checkTwelveDataParameters(endpoint,kwargs)
          
          httpURL = self.utilities.makeTwelveDataEndpoint(url=self.baseUrl,endpoint=endpoint,params=kwargs)
          res = self.doPost(httpURL)
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
        

class twelveDataService(baseTwelveDataService):
  """
    A class representing all predefined TwelveData API Call

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
    @TODO Rellenar los métodos
    """
  def __init__(self, api_key) -> None:
    super().__init__(api_key)
    