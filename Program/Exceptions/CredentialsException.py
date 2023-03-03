from .ExceptionUtilities import exceptionUtilities

exeU = exceptionUtilities()


class CredentialSimpleError(Exception):
  """
  @TODO Generar DOC
  """
  def __init__(self,action,error):
    self.CustomMessage = exeU.buildMessage(f"[CREDENTIAL_MANAGER] Problem on method: {action}")
    self.message = exeU.buildMessage(f"[CREDENTIAL_MANAGER] {error}")
    