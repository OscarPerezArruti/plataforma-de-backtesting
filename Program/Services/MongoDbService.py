# EXTERNAL MODULES IMPORTS
import logging
import json
from pymongo import MongoClient
import re
# OUR MODULES IMPORTS
from .ServiceUtilities import serviceUtilities
from Exceptions import *

# WE GET LOGGER
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

    def __init__(self, user=None, password=None, url="mongodb://localhost:27017/") -> None:
        self.user = user
        self.password = password
        #   TODO controlar url
        """ La idea es con regex detectar los dos tipos de URLs y en caso contrario
        lanzar un excepción persanalizada con los formato validos."""
        self.url = url
        self.utilities = serviceUtilities()
        # MONGODB CONNECTION
        self.client = None

    def __enter__(self):
        self.client = MongoClient(self.url)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def doRequest(self):
        pass

    def MongoDbPost(self):
        pass
    
    def test(self):
        db = self.client["TFG_Finance_2023"] # SELECTION OF DB
        one = db["1day_data"] # SELECTION OF COLLECTION
        return one
        



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
