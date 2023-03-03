from .TwelveDataExceptions import * 
from .CredentialsException import * 


    
from colorama import Fore
color_red = Fore.RED
reset = Fore.RESET
def buildMessage(message):
    return color_red + message + reset