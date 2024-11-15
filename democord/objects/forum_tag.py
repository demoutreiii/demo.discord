from ..types import Snowflake
from .base   import BaseObject
from typing  import *


class ForumTagObject(BaseObject):
  emoji_id   : Optional[Snowflake]
  emoji_name : Optional[str]
  id         : Snowflake
  moderated  : bool
  name       : str