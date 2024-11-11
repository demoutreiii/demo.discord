from ..member import Member
from ..types  import (
                     ISO8601Timestamp,
                     Snowflake
                     )
from .base    import BaseObject


class MemberObject(BaseObject, Member):
  from .avatar_decoration_data import AvatarDecorationDataObject
  from .user                   import UserObject

  avatar                       : Optional[str]
  avatar_decoration_data       : Optional[AvatarDecorationDataObject]
  banner                       : Optional[str]
  communication_disabled_until : Optional[ISO8601Timestamp]
  deaf                         : bool                                 = False
  flags                        : int                                  = 0
  joined_at                    : ISO8601Timestamp
  mute                         : bool                                 = False
  nick                         : Optional[str]
  pending                      : Optional[bool]                       = False
  permissions                  : Optional[str]
  premium_since                : Optional[ISO8601Timestamp]
  roles                        : Optional[Snowflake]
  user                         : Optional[UserObject]