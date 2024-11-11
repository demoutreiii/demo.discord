from enum   import Enum, StrEnum, auto
from typing import *


class ChannelType(Enum):
  text                =  0
  dm                  =  1
  voice               =  2
  group_dm            =  3
  category            =  4
  announcement        =  5
  announcement_thread = 10
  public_thread       = 11
  private_thread      = 12
  stage               = 13
  directory           = 14
  forum               = 14
  media               = 16


class DefaultMessageNotification(Enum):
  """
  Set default message notification level of a guild
  """
  all_messages  = 0
  only_mentions = 1


class EmbedType(StrEnum):
  article     = auto()
  gifv        = auto()
  image       = auto()
  link        = auto()
  poll_result = auto()
  rich        = auto()
  video       = auto()


class ErrorCodes(Enum):
  """
  Represents an error code received from Discord
  """
  BotMissingPermissions = 50013


class ExplicitContentFilter(Enum):
  """
  Set explicit content filter level of a guild
  """
  disabled              = 0
  members_without_roles = 1
  all_members           = 2


class ForumLayout(Enum):
  list_view    = 1
  gallery_view = 2


class ForumSortOrder(Enum):
  latest_activity = 0
  creation_date   = 1


class GatewayEvents(Enum):
  """
  Type of Dispatch gateway event
  """
  GuildCreate = "GUILD_CREATE"
  Ready       = "READY"
  Resumed     = "RESUMED"


class GatewayIntents(Enum):
  """
  Gateway intents the application can use
  """
  guilds                = 1 << 0
  members               = 1 << 1
  moderation            = 1 << 2
  emojis_and_stikers    = 1 << 3
  integrations          = 1 << 4
  webhooks              = 1 << 5
  invites               = 1 << 6
  voice_states          = 1 << 7
  presences             = 1 << 8
  messages              = ( 1 << 9  ) | ( 1 << 12 )
  reactions             = ( 1 << 10 ) | ( 1 << 13 )
  typing                = ( 1 << 11 ) | ( 1 << 14 )
  message_content       = 1 << 15
  scheduled_events      = 1 << 16
  automod_configuration = 1 << 20
  automod_execution     = 1 << 21
  polls                 = ( 1 << 24 ) | ( 1 << 25 )


class GuildFeatures(Enum):
  animated_banner                           = "ANIMATED_BANNER"
  animated_icon                             = "ANIMATED_ICON"
  application_command_permissions_v2        = "APPLICATION_COMMAND_PERMISSIONS_V2"
  automod                                   = "AUTO_MODERATION"
  banner                                    = "BANNER"
  community                                 = "COMMUNITY"
  creator_monetization_provisional          = "CREATOR_MONETIZATION_PROVISIONAL"
  creator_store_page                        = "CREATOR_STORE_PAGE"
  developer_support_server                  = "DEVELOPER_SUPPORT_SERVER"
  discoverable                              = "DISCOVERABLE"
  featurable                                = "FEATURABLE"
  invites_disabled                          = "INVITES_DISABLED"
  invite_splash                             = "INVITE_SPLASH"
  member_verification_gate                  = "MEMBER_VERIFICATION_GATE_ENABLED"
  more_stickers                             = "MORE_STICKERS"
  news                                      = "NEWS"
  partnered                                 = "PARTNERED"
  preview                                   = "PREVIEW_ENABLED"
  raid_alerts_disabled                      = "RAID_ALERTS_DISABLED"
  role_icons                                = "ROLE_ICONS"
  role_subscriptions_available_for_purchase = "ROLE_SUBSCRIPTIONS_AVAILABLE_FOR_PURCHASE"
  role_subscriptions                        = "ROLE_SUBSCRIPTIONS_ENABLED"
  ticketed_events                           = "TICKETED_EVENTS_ENABLED"
  vanity_url                                = "VANITY_URL"
  verified                                  = "VERIFIED"
  vip_regions                               = "VIP_REGIONS"
  welcome_screen                            = "WELCOME_SCREEN_ENABLED"


class InviteTargetType(Enum):
  stream               = 1
  embedded_application = 2


class InviteType(Enum):
  guild    = 0
  group_dm = 1
  friend   = 2


class MFALevel(Enum):
  """
  Set multi-factor authentication level of a guild
  """
  none     = 0
  elevated = 1


class NSFWLevel(Enum):
  """
  Set NSFW level for a guild
  """
  default        = 0
  explicit       = 1
  safe           = 2
  age_restricted = 3


class PayloadType(Enum):
  """
  Type of payload that is received or sent by the socket
  """
  Dispatch            = 0
  HeartBeat           = 1
  Identify            = 2
  PresenceUpdate      = 3
  VoiceStateUpdate    = 4
  Resume              = 6
  Reconnect           = 7
  RequestGuildMembers = 8
  InvalidSession      = 9
  Hello               = 10
  HeartBeatACK        = 11


class PremiumTier(Enum):
  """
  Tier level of a guild ( AKA Server Boost Tier )
  """
  none   = 0
  tier_1 = 1
  tier_2 = 2
  tier_3 = 3


class PremiumType(Enum):
  """
  Type of Premium ( Nitro ) subscription the user is subscribed to
  """
  none          = 0
  nitro_classic = 1
  nitro         = 2
  nitro_basic   = 3


class PermissionFlags(Enum):
  """
  Permission flags for a certain context
  """
  create_instant_invite               = 1 << 0
  kick_members                        = 1 << 1
  ban_members                         = 1 << 2
  administrator                       = 1 << 3
  manage_channels                     = 1 << 4
  manage_guild                        = 1 << 5
  add_reactions                       = 1 << 6
  view_audit_log                      = 1 << 7
  priority_speaker                    = 1 << 8
  stream                              = 1 << 9
  view_channel                        = 1 << 10
  send_messages                       = 1 << 11
  send_tts_messages                   = 1 << 12
  manage_messages                     = 1 << 13
  embed_links                         = 1 << 14
  attach_files                        = 1 << 15
  read_message_history                = 1 << 16
  mention_everyone                    = 1 << 17
  use_external_emojis                 = 1 << 18
  view_guild_insights                 = 1 << 19
  connect                             = 1 << 20
  speak                               = 1 << 21
  mute_members                        = 1 << 22
  deafen_members                      = 1 << 23
  move_members                        = 1 << 24
  use_voice_activity                  = 1 << 25
  change_nickname                     = 1 << 26
  manage_nicknames                    = 1 << 27
  manage_roles                        = 1 << 28
  manage_webhooks                     = 1 << 29
  manage_expressions                  = 1 << 30
  use_application_commands            = 1 << 31
  request_to_speak                    = 1 << 32
  manage_events                       = 1 << 33
  manage_threads                      = 1 << 34
  create_public_threads               = 1 << 35
  create_private_threads              = 1 << 36
  use_external_stickers               = 1 << 37
  send_messages_in_threads            = 1 << 38
  use_embedded_activities             = 1 << 39
  moderate_members                    = 1 << 40
  view_creator_monetization_analytics = 1 << 41
  use_soundboard                      = 1 << 42
  create_guild_expressions            = 1 << 43
  create_events                       = 1 << 44
  use_external_sounds                 = 1 << 45
  send_voice_messages                 = 1 << 46
  send_polls                          = 1 << 49
  use_external_apps                   = 1 << 50


class VerificationLevel(Enum):
  """
  Set verification level of a guild
  """
  none      = 0
  low       = 1
  medium    = 2
  high      = 3
  very_high = 4


class VideoQualityMode(Enum):
  auto = 1
  full = 2