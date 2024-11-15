from .base  import BaseObject
from typing import *


class BanObject(BaseObject):
  from .user import UserObject

  reason : Optional[str]
  user   : UserObject