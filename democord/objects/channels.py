from ..channels import (
                       AnnouncementChannel,
                       GuildChannel
                       )
from ..types    import (
                       ISO8601Timestamp,
                       Snowflake
                       )
from .base      import BaseObject
from typing     import *


class AnnouncementChannelObject(BaseObject, AnnouncementChannel):
  from overwrite import OverwriteObject

  default_auto_archive_duration : Optional[int]               = 60
  guild_id                      : Optional[Snowflake]
  id                            : Snowflake
  last_message_id               : Optional[Snowflake]
  last_pin_timestamp            : Optional[ISO8601Timestamp]
  name                          : Optional[str]
  nsfw                          : Optional[bool]              = False
  parent_id                     : Optional[Snowflake]
  permission_overwrites         : List[OverwriteObject]       = []
  permissions                   : Optional[str]
  position                      : Optional[int]
  topic                         : Optional[str]
  type                          : int                         = 5


class GuildChannelObject(BaseObject, GuildChannel):
  from .overwrite import OverwriteObject

  guild_id              : Optional[Snowflake]
  id                    : Snowflake
  name                  : Optional[str]
  permission_overwrites : List[OverwriteObject] = []
  permissions           : Optional[str]
  position              : Optional[int]
  type                  : int