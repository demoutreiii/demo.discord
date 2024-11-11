from ..emoji import Emoji
from ..types import Snowflake
from .base   import BaseObject
from typing  import *


class EmojiObject(BaseObject, Emoji):
  from .role import RoleObject
  from .user import UserObject

  animated       : bool                = False
  available      : bool                = True
  id             : Optional[Snowflake]
  managed        : bool                = False
  name           : Optional[str]
  require_colons : bool                = True
  roles          : List[RoleObject]    = []
  user           : UserObject