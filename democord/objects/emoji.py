from ..types import Snowflake
from .base   import BaseObject
from typing  import *


class EmojiObject(BaseObject):
  from .user import UserObject

  animated       : Optional[bool]
  available      : Optional[bool]
  id             : Optional[Snowflake]
  managed        : Optional[bool]
  name           : Optional[str]
  require_colons : Optional[bool]
  roles          : List[Snowflake]      = []
  user           : Optional[UserObject]