import logging
from .ServiceConstants import *
from Exceptions import *

logging = logging.getLogger(__name__)

class serviceUtilities:
    """
    A class that stores avery auxiliary method needed
    in order to use any class inside Services package.
    
    Attributes
    ----------
    No attributes are needed!
    
    Methods
    -------
    makeTwelveDataEndpoint(self,url,base,**kwargs ) -> str:
        Builds up a URL needed to use TwelveData API
        
        
    """
    def checkTwelveDataEndpoint(self,endpoint):
        """
        Checks if a given endpoint exists on TwelveData API

        Parameters
        ----------
        endpoint : str
            enpoint to be checked

        Returns
        -------
        boolean:True if the endpoint exists
        """
        if ValidParameters.get(endpoint) == None:
            raise twelveDataInvalidEndpoint(endpoint)
        return True

    def checkTwelveRequiredParams(self,endpoint,params):
        """
        @TODO rellenar

        Parameters
        ----------
        @TODO rellenar

        Returns
        -------
        @TODO rellenar
        
        Exceptions
        ----------
        @TODO rellenar
        """
        # Checks if valid enpoint
        self.checkTwelveDataEndpoint(endpoint=endpoint) 
        # checks if every requiered param is on params dict
        if len(RequieredParameters[endpoint]) > 0:
            for requieredParam in RequieredParameters[endpoint]: 
                if params.get(requieredParam) == None:
                    raise twelveDataRequieredParam(requieredParam)
        return True    
    
    def checkTwelveDataParameters(self,endpoint,params):
        """
        Checks if a array of parameters are allowed for 
        a endpoint of TwelveData API

        Parameters
        ----------
        endpoint : str
            Valid endpoint
        args 
            Parameters to be checked

        Returns
        -------
        boolean:True if the endpoint exists
        
        Exceptions
        ----------
        @TODO rellenar
        
        """
        self.checkTwelveDataEndpoint(endpoint=endpoint)
        if(len(ValidParameters[endpoint])==0 and params != {}):
             raise twelveDataNoParamsNeeded() # IF 
        for param in params.keys():  # Checks if every param is a valid one
            if param not in ValidParameters[endpoint]:
                raise twelveDataInvalidParam(param)
        return True
        
    
    
    def makeTwelveDataEndpoint(self,url,endpoint,params) -> str:
        """
        Builds up a URL needed to use TwelveData API

        Parameters
        ----------
        url : str
            Base url of TwelveData API
        endpoint : str
            Endpoint of TwelveData API
        params
            Variable parameters allowed in TwelveData API calls

        Returns
        -------
        str:Returns the complete url ready to use on a HTTP Request
        
        Exceptions
        ----------
        @TODO rellenar
        
        """
        logging.debug("Inicio de ejecución de def makeEnpoint()")
        parameters = [] # ARRAY DONDE IRÁN LOS PARAMETROS
        for key,value in params.items(): # CONSTRUIMOS TODOS LOS PARAMETROS
            parameters.append(f"{key}={value}") # aÑADIMOS TODOS LOS PARAMETROS
        logging.debug(f"endpoint={endpoint}, Parameters={parameters}")    
        return url+endpoint + "?" + "&".join(parameters) #


        
        