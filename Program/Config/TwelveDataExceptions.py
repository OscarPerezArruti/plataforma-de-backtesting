from colorama import Fore
color_red = Fore.RED
reset = Fore.RESET



class twelveDataBadRequest(Exception):
  def __init__(self,error):
    self.message = buildMessage(f"[TWELVE_DATA_ERROR] {error}")

class twelveDataNoParams(Exception):
  def __init__(self):
    self.message = buildMessage(f"[TWELVE_DATA_ERROR] There is not params")

class twelveDataRequieredParam(Exception):
  def __init__(self,param):
    self.message = buildMessage(f"[TWELVE_DATA_ERROR] Requiered param {param}")

class twelveDataInvalidEndpoint(Exception):
  def __init__(self,endpoint):
    self.message = buildMessage(f"[TWELVE_DATA_ERROR] Invalid endpoint {endpoint}")

class twelveDataInvalidParam(Exception):
  def __init__(self,param):
    self.message = buildMessage(f"[TWELVE_DATA_ERROR] Invalid parameter {param}")
    
    
def buildMessage(message):
    return color_red + message + reset