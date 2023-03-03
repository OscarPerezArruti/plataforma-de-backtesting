from . import buildMessage


class CredentialSimpleError(Exception):
  def __init__(self,action,error):
    self.CustomMessage = buildMessage(f"[CREDENTIAL_MANAGER] Problem on method: {action}")
    self.message = buildMessage(f"[CREDENTIAL_MANAGER] {error}")
    