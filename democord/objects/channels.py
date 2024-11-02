from ..channels import (
                       AnnouncementChannel,
                       CategoryChannel,
                       Forum,
                       GuildChannel,
                       MediaChannel,
                       StageChannel
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


class ForumObject(BaseObject, Forum):
  from .emoji     import EmojiObject
  from .overwrite import OverwriteObject
  from .tag       import TagObject

  available_tags                     : List[TagObject]       = []
  default_auto_archive_duration      : int                   = 60
  default_forum_layout               : Optional[int]
  default_reaction_emoji             : Optional[EmojiObject]
  default_sort_order                 : Optional[int]
  default_thread_rate_limit_per_user : Optional[int]
  flags                              : Optional[int]
  guild_id                           : Snowflake
  id                                 : Snowflake
  last_message_id                    : Optional[Snowflake]
  name                               : str
  nsfw                               : bool                  = False
  parent_id                          : Optional[Snowflake]
  permission_overwrites              : List[OverwriteObject] = []
  permissions                        : Optional[str]
  position                           : int
  topic                              : Optional[str]
  type                               : int                   = 15


class GuildChannelObject(BaseObject, GuildChannel):
  from .overwrite import OverwriteObject

  guild_id              : Snowflake
  id                    : Snowflake
  name                  : str
  permission_overwrites : List[OverwriteObject] = []
  permissions           : Optional[str]
  position              : int
  type                  : int


class MediaChannelObject(BaseObject, MediaChannel):
  from .emoji     import EmojiObject
  from .overwrite import OverwriteObject
  from .tag       import TagObject

  available_tags                     : List[TagObject]       = []
  default_auto_archive_duration      : int                   = 60
  default_reaction_emoji             : Optional[EmojiObject]
  default_sort_order                 : Optional[int]
  default_thread_rate_limit_per_user : Optional[int]
  flags                              : Optional[int]
  guild_id                           : Snowflake
  id                                 : Snowflake
  last_message_id                    : Optional[Snowflake]
  name                               : str
  nsfw                               : bool                  = False
  parent_id                          : Optional[Snowflake]
  permission_overwrites              : List[OverwriteObject] = []
  permissions                        : Optional[str]
  position                           : int
  topic                              : Optional[str]
  type                               : int                   = 16


class StageChannelObject(BaseObject, StageChannel):
  from .overwrite import OverwriteObject
  
  guild_id              : Snowflake
  id                    : Snowflake
  last_message_id       : Optional[int]
  name                  : str
  nsfw                  : bool                  = False
  parent_id             : Optional[int]
  permission_overwrites : List[OverwriteObject] = []
  permissions           : Optional[str]
  position              : int
  rate_limit_per_user   : Optional[int]
  topic                 : Optional[str]
  type                  : int                   = 13