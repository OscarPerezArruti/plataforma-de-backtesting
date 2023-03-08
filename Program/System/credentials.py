# EXTERNAL MODULES IMPORTS
import keyring
import logging

# OUR MODULES IMPORTS
from Exceptions import *

# WE GET LOGGER
log = logging.getLogger(__name__)



class Credentials:
    """
    A class representing the communication interface between OS Password
    manager and python program

    AttributesA
    ----------
    @TODO rellenar

    Methods
    -------
    @TODO rellenar

    """
    def set_password(self,name,username,password):
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
        try:
            try: 
                keyring.set_password(name, username, password)
                
            except Exception as e: 
                raise CredentialsException("set_password",e)
        except CredentialsException as e:
            log.error(e.CustomMessage)
            log.error(e.message)
        except Exception as e:
            log.error(e)
            
            
    def get_password(self,name,username):
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
        try:
            try: 
                psswd = keyring.get_password(name, username)
                return psswd
            except Exception as e: 
                raise CredentialsException("get_password",e)
        except CredentialsException as e:
            log.error(e.CustomMessage)
            log.error(e.message)
        except Exception as e:
            log.error(e)




        
