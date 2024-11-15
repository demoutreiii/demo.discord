from ..types import Snowflake
from .base   import BaseObject
from typing  import *


class IntegrationApplicationObject(BaseObject):
  from .user import UserObject

  bot         : Optional[UserObject]
  description : str
  icon        : Optional[str]
  id          : Snowflake
  name        : str