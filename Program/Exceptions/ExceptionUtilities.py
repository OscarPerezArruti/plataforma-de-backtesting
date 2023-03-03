import logging
from colorama import Fore
color_red = Fore.RED
reset = Fore.RESET



logging = logging.getLogger(__name__)

class exceptionUtilities:
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
    def buildMessage(self,message):
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
        return color_red + message + reset