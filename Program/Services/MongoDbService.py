from .ServiceUtilities import serviceUtilities
from Exceptions import *
import logging
import json

log = logging.getLogger(__name__)

class baseMongoDbService:
    """
    A class representing the communication interface between OS Password
    manager and python program
    
    Parameters
    ----------
    @TODO rellenar

    Attributes
    ----------
    @TODO rellenar

    Methods
    -------
    @TODO rellenar

    """

    def __init__(self,api_key) -> None:
        self.api_key = api_key
        self.utilities = serviceUtilities()
        self.baseUrl = "https://api.twelvedata.com/"

    def doRequest(self):
      pass

    def MongoDbPost(self):
        pass
        

class mongoDbService(baseMongoDbService):
  """
    A class representing all predefined TwelveData API Call

    Attributes
    ----------
    api_key : str
        Api key of TwelveData API
    utilities : serviceUtilities
        Class to use auxiliry methods
    baseUrl : str
        Base url of every API call

    Methods
    -------
    @TODO Rellenar los métodos
    """
  
    