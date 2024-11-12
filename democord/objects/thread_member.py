from ..types import (
                    ISO8601Timestamp,
                    Snowflake
                    )
from .base   import BaseObject
from typing  import *


class ThreadMemberObject(BaseObject):
  from .guild_member import GuildMemberObject

  flags          : int
  id             : Optional[Snowflake]
  join_timestamp : ISO8601Timestamp
  member         : Optional[GuildMemberObject]
  user_id        : Optional[Snowflake]