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

    def __init__(self,user=None,password=None,url="mongodb://localhost:27017/") -> None:
        self.user = user
        self.password = password
        self.url = url
        self.utilities = serviceUtilities()
       
    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

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
  
    