from ..types import (
                    ISO8601Timestamp,
                    Snowflake
                    )
from .base   import BaseObject
from typing  import *


class GuildMemberObject(BaseObject):
  from .avatar_decoration_data import AvatarDecorationDataObject
  from .user                   import UserObject

  avatar                       : Optional[str]
  avatar_decoration_data       : Optional[AvatarDecorationDataObject]
  banner                       : Optional[str]
  communication_disabled_until : Optional[ISO8601Timestamp]
  deaf                         : bool
  flags                        : int
  joined_at                    : ISO8601Timestamp
  mute                         : bool
  nick                         : Optional[str]
  pending                      : Optional[bool]
  permissions                  : Optional[str]
  premium_since                : Optional[ISO8601Timestamp]
  roles                        : List[Snowflake]                      = []
  user                         : Optional[UserObject]