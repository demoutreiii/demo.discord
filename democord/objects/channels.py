from ..channels import (
                       AnnouncementChannel,
                       CategoryChannel,
                       DMChannel,
                       Forum,
                       GuildChannel,
                       MediaChannel,
                       StageChannel,
                       TextChannel,
                       Thread,
                       VoiceChannel
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


class DMChannelObject(BaseObject, DMChannel):
  from .user import UserObject

  application_id  : Optional[Snowflake]
  icon            : Optional[str]
  id              : Snowflake
  last_message_id : Optional[Snowflake]
  managed         : bool                = False
  name            : Optional[str]
  recipients      : List[UserObject]    = []
  type            : Literal[1, 3]


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


class TextChannelObject(BaseObject, TextChannel):
  from .overwrite import Overwrite

  default_auto_archive_duration      : int                        = 60
  default_thread_rate_limit_per_user : Optional[int]
  guild_id                           : int
  id                                 : Snowflake
  last_message_id                    : Optional[Snowflake]
  last_pin_timestamp                 : Optional[ISO8601Timestamp]
  name                               : str
  nsfw                               : bool                       = False
  parent_id                          : Optional[Snowflake]
  permission_overwrites              : List[OverwriteObject]      = []
  permissions                        : Optional[str]
  position                           : int
  rate_limit_per_user                : Optional[int]
  topic                              : Optional[str]
  type                               : int                        = 0


class ThreadObject(BaseObject, Thread):
  from .overwrite       import OverwriteObject
  from .thread_member   import ThreadMemberObject
  from .thread_metadata import ThreadMetadataObject

  applied_tags          : List[Snowflake]
  flags                 : int
  guild_id              : Snowflake
  id                    : Snowflake
  member                : ThreadMemberObject
  member_count          : int
  message_count         : int
  name                  : str
  owner_id              : Snowflake
  parent_id             : Optional[Snowflake]
  permission_overwrites : List[OverwriteObject]
  position              : int
  rate_limit_per_user   : Optional[int]
  thread_metadata       : Optional[ThreadMetadataObject]
  total_message_sent    : int
  type                  : Literal[10, 11, 12]


class VoiceChannelObject(BaseObject, VoiceChannel):
  from .overwrite import OverwriteObject

  bitrate               : int
  guild_id              : Snowflake
  id                    : Snowflake
  last_message_id       : Optional[Snowflake]
  last_pin_timestamp    : Optional[ISO8601Timestamp]
  name                  : str
  nsfw                  : bool                       = False
  parent_id             : Optional[Snowflake]
  permission_overwrites : List[OverwriteObject]      = []
  permissions           : Optional[str]
  position              : int
  rate_limit_per_user   : Optional[int]
  rtc_region            : Optional[str]
  topic                 : Optional[str]
  type                  : int                        = 2
  user_limit            : int
  video_quality_mode    : int