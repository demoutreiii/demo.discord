from .base  import BaseObject
from typing import *


class AuditLogChangeObject(BaseObject):
  key       : str
  new_value : Optional[Any]
  old_value : Optional[Any]