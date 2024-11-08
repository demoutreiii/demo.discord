from ..guild import Guild
from ..types import Snowflake
from .base   import Baseobject
from typing  import *


class GuildObject(BaseObject, Guild):
  from .emoji          import EmojiObject
  from .role           import RoleObject
  from .sticker        import StickerObject
  from .welcome_screen import WelcomeScreenObject

  afk_channel_id                : Optional[Snowflake]
  afk_timeout                   : int                 = 0
  application_id                : Optional[Snowflake]
  approximate_member_count      : int                 = 0
  approximate_presence_count    : int                 = 0
  banner                        : Optional[str]
  default_message_notifications : int
  description                   : Optional[str]
  discovery_splash              : Optional[str]
  emojis                        : List[EmojiObject]   = []
  explicit_content_filter       : int
  features                      : List[str]           = [] 
  icon                          : Optional[str]
  icon_hash                     : Optional[str]
  id                            : Snowflake
  max_members                   : int
  max_presences                 : Optional[int]
  max_stage_video_channel_users : int
  max_video_channel_users       : int
  mfa_level                     : int
  name                          : str
  nsfw_level                    : int
  owner                         : bool                = False
  owner_id                      : Snowflake
  permissions                   : str
  preferred_locale              : str                 = "en-US"
  premium_progress_bar_enabled  : bool                = False
  premium_subscription_count    : int
  premium_tier                  : int
  public_updates_channel_id     : Optional[Snowflake]
  roles                         : List[RoleObject]    = []
  rules_channel_id              : Optional[Snowflake]
  safety_alerts_channel_id      : Optional[Snowflake]
  splash                        : Optional[str]
  stickers                      : List[StickerObject] = []
  system_channel_flags          : int                 = 0
  system_channel_id             : Optional[Snowflake]
  vanity_url_code               : Optional[str]
  verification_level            : int
  welcome_screen                : WelcomeScreenObject
  widget_channel_id             : Optional[Snowflake]
  widget_enabled                : bool                = False