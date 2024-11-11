from .base  import BaseObject
from typing import *


class InstallParamsObject(BaseObject):
  scopes      : List[str] = []
  permissions : str