from .base  import BaseObject
from typing import *


class ActivityLocationObject(BaseObject):
  from .enums import ActivityLocationKind

  channel_id : Snowflake
  guild_id   : Optional[Snowflake]
  id         : str
  kind       : ActivityLocationKind