from ..types import Snowflake
from .base   import BaseObject
from typing  import *


class DefaultReactionObject(BaseObject):
  emoji_id   : Optional[Snowflake]
  emoji_name : Optional[str]