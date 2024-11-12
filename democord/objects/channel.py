from ..types import (
                    ISO8601Timestamp,
                    Snowflake
                    )
from .base   import BaseObject
from typing  import *


class ChannelObject(BaseObject):
  from .default_reaction import DefaultReactionObject
  from .forum_tag        import ForumTagObject
  from .overwrite        import OverwriteObject
  from .thread_member    import ThreadMemberObject
  from .thread_metadata  import ThreadMetadataObject
  from .user             import UserObject

  application_id                     : Optional[Snowflake]
  applied_tags                       : List[Snowflake]                 = []
  available_tags                     : List[ForumTagObject]            = []
  bitrate                            : Optional[int]
  default_auto_archive_duration      : Optional[int]
  default_forum_layout               : Optional[int]
  default_reaction_emoji             : Optional[DefaultReactionObject]
  default_sort_order                 : Optional[int]
  default_thread_rate_limit_per_user : Optional[int]
  flags                              : Optional[int]
  guild_id                           : Optional[Snowflake]
  icon                               : Optional[str]
  id                                 : Snowflake
  last_message_id                    : Optional[Snowflake]
  last_pin_timestamp                 : Optional[ISO8601Timestamp]
  managed                            : Optional[bool]
  member_count                       : Optional[int]
  message_count                      : Optional[int]
  name                               : Optional[str]
  nsfw                               : Optional[bool]
  owner_id                           : Optional[Snowflake]
  permission_overwrites              : List[OverwriteObject]           = []
  permissions                        : Optional[str]
  position                           : Optional[int]
  rate_limit_per_user                : Optional[int]
  recipients                         : List[UserObject]                = []
  rtc_region                         : Optional[str]
  thread_member                      : Optional[ThreadMemberObject]
  thread_metadata                    : Optional[ThreadMetadataObject]
  topic                              : Optional[str]
  total_message_sent                 : Optional[int]
  type                               : int
  user_limit                         : Optional[int]
  video_quality_mode                 : Optional[int]