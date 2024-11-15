from ..types import Snowflake
from .base   import BaseObject
from typing  import *


class GuildWidgetObject(BaseObject):
  from .channel import ChannelObject
  from .user    import UserObject

  channels         : List[ChannelObject] = []
  id               : Snowflake
  instant_invite   : Optional[str]
  name             : str
  presence_count   : int
  users            : List[UserObject]    = []