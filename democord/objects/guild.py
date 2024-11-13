from ..types import Snowflake
from .base   import BaseObject
from typing  import *


class GuildObject(BaseObject):
  from .emoji          import EmojiObject
  from .role           import RoleObject
  from .sticker        import StickerObject
  from .welcome_screen import WelcomeScreenObject

  afk_channel_id                : Optional[Snowflake]
  afk_timeout                   : int
  application_id                : Optional[Snowflake]
  approximate_member_count      : Optional[int]
  approximate_presence_count    : Optional[int]
  banner                        : Optional[str]
  default_message_notifications : int
  description                   : Optional[str]
  discovery_splash              : Optional[str]
  emojis                        : List[EmojiObject]             = []
  explicit_content_filter       : int
  features                      : List[str]                     = []
  icon                          : Optional[str]
  icon_hash                     : Optional[str]
  id                            : Snowflake
  max_members                   : Optional[int]
  max_presences                 : Optional[int]
  max_stage_video_channel_users : Optional[int]
  max_video_channel_users       : Optional[int]
  mfa_level                     : int
  name                          : str
  nsfw_level                    : int
  owner                         : Optional[bool]
  owner_id                      : Snowflake
  permissions                   : Optional[str]
  preferred_locale              : str
  premium_progress_bar_enabled  : bool
  premium_subscription_count    : Optional[int]
  premium_tier                  : int
  public_updates_channel_id     : Optional[Snowflake]
  roles                         : List[RoleObject]              = []
  rules_channel_id              : Optional[Snowflake]
  safety_alerts_channel_id      : Optional[Snowflake]
  splash                        : Optional[str]
  stickers                      : List[StickerObject]           = []
  system_channel_flags          : int
  system_channel_id             : Optional[Snowflake]
  vanity_url_code               : Optional[str]
  verification_level            : int
  welcome_screen                : Optional[WelcomeScreenObject]
  widget_channel_id             : Optional[Snowflake]
  widget_enabled                : Optional[bool]