from ..channels import (
                       AnnouncementChannel,
                       CategoryChannel,
                       GuildChannel
                       )
from ..types    import (
                       ISO8601Timestamp,
                       Snowflake
                       )
from .base      import BaseObject
from typing     import *


class AnnouncementChannelObject(BaseObject, AnnouncementChannel):
  from .overwrite import OverwriteObject

  default_auto_archive_duration : Optional[int]               = 60
  guild_id                      : Optional[Snowflake]
  id                            : Snowflake
  last_message_id               : Optional[Snowflake]
  last_pin_timestamp            : Optional[ISO8601Timestamp]
  name                          : str
  nsfw                          : Optional[bool]              = False
  parent_id                     : Optional[Snowflake]
  permission_overwrites         : List[OverwriteObject]       = []
  permissions                   : Optional[str]
  position                      : int
  topic                         : Optional[str]
  type                          : int                         = 5


class CategoryChannelObject(BaseObject, CategoryChannel):
  from .overwrite import OverwriteObject

  guild_id              : Snowflake
  id                    : Snowflake
  name                  : str
  permission_overwrites : List[OverwriteObject]
  permissions           : Optional[str]
  position              : int
  type                  : int                   = 4


class GuildChannelObject(BaseObject, GuildChannel):
  from .overwrite import OverwriteObject

  guild_id              : Snowflake
  id                    : Snowflake
  name                  : str
  permission_overwrites : List[OverwriteObject] = []
  permissions           : Optional[str]
  position              : int
  type                  : int