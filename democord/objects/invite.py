from ..invite import Invite
from ..types  import ISO8601Timestamp
from .base    import BaseObject


class InviteObject(BaseObject, Invite):
  from .application           import ApplicationObject
  from .channels              import ChannelObject
  from .guild                 import GuildObject
  from .guild_scheduled_event import GuildScheduledEventObject
  from .user                  import UserObject

  approximate_member_count   : Optional[int]
  approximate_presence_count : Optional[int]
  channel                    : Optional[ChannelObject]
  code                       : str
  expires_at                 : Optional[ISO8601Timestamp]
  guild                      : Optional[GuildObject]
  guild_scheduled_event      : Optional[GuildScheduledEventObject]
  inviter                    : Optional[UserObject]
  target_application         : Optional[ApplicationObject]
  target_type                : Optional[int]
  target_user                : Optional[UserObject]
  type                       : int