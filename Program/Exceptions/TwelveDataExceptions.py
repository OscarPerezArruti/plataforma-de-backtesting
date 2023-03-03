from .ExceptionUtilities import exceptionUtilities

exeU = exceptionUtilities()



class twelveDataBadRequest(Exception):
  """
  @TODO Generar DOC
  """
  def __init__(self,error):
    self.message = exeU.buildMessage(f"[TWELVE_DATA_ERROR] {error}")

class twelveDataNoParams(Exception):
  """
  @TODO Generar DOC
  """
  def __init__(self):
    self.message = exeU.buildMessage(f"[TWELVE_DATA_ERROR] There is not params")

class twelveDataRequieredParam(Exception):
  """
  @TODO Generar DOC
  """
  def __init__(self,param):
    self.message = exeU.buildMessage(f"[TWELVE_DATA_ERROR] Requiered param {param}")

class twelveDataInvalidEndpoint(Exception):
  """
  @TODO Generar DOC
  """
  def __init__(self,endpoint):
    self.message = exeU.buildMessage(f"[TWELVE_DATA_ERROR] Invalid endpoint {endpoint}")

class twelveDataInvalidParam(Exception):
  """
  @TODO Generar DOC
  """
  def __init__(self,param):
    self.message = exeU.buildMessage(f"[TWELVE_DATA_ERROR] Invalid parameter {param}")
