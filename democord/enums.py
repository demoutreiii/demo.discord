from enum   import (
                   auto,
                   Enum,
                   StrEnum
                   )
from typing import *


class ActivityLocationKind(StrEnum):
  gc = auto()
  pc = auto()


class ApplicationEventWebhookStatus(Enum):
  disabled            = 1
  enabled             = 2
  disabled_by_discord = 3


class ApplicationIntegrationType(Enum):
  guild_install = 0
  user_intall   = 1


class AuditLogEvent(Enum):
  guild_update                                =   1
  channel_create                              =  10
  channel_update                              =  11
  channel_delete                              =  12
  channel_overwrite_create                    =  13
  channel_overwrite_update                    =  14
  channel_overwrite_delete                    =  15
  member_kick                                 =  20
  member_prune                                =  21
  member_ban_add                              =  22
  member_ban_remove                           =  23
  member_update                               =  24
  member_role_update                          =  25
  member_move                                 =  26
  member_disconnect                           =  27
  bot_add                                     =  28
  role_create                                 =  30
  role_update                                 =  31
  role_delete                                 =  32
  invite_create                               =  40
  invite_update                               =  41
  invite_delete                               =  42
  webhook_create                              =  50
  webhook_update                              =  51
  webhook_delete                              =  52
  emoji_create                                =  60
  emoji_update                                =  61
  emoji_delete                                =  62
  message_delete                              =  72
  message_bulk_delete                         =  73
  message_pin                                 =  74
  message_unpin                               =  75
  integration_create                          =  80
  integration_update                          =  81
  integration_delete                          =  82
  stage_instance_create                       =  83
  stage_instance_update                       =  84
  stage_instance_delete                       =  85
  sticker_create                              =  90
  sticker_update                              =  91
  sticker_delete                              =  92
  guild_scheduled_event_create                = 100
  guild_scheduled_event_update                = 101
  guild_scheduled_event_delete                = 102
  thread_create                               = 110
  thread_update                               = 111
  thread_delete                               = 112
  application_command_permission_update       = 121
  soundboard_sound_create                     = 130
  soundboard_sound_update                     = 131
  soundboard_sound_delete                     = 132
  auto_moderation_rule_create                 = 140
  auto_moderation_rule_update                 = 141
  auto_moderation_rule_delete                 = 142
  auto_moderation_block_message               = 143
  auto_moderation_flag_to_channel             = 144
  auto_moderation_user_communication_disabled = 145
  creator_monetization_request_created        = 150
  creator_monetization_terms_accepted         = 151
  onboarding_prompt_create                    = 163
  onboarding_prompt_update                    = 164
  onboarding_prompt_delete                    = 165
  onboarding_create                           = 166
  onboarding_update                           = 167
  home_settings_create                        = 190
  home_settings_update                        = 191


class AutomodActionType(Enum):
  block_message            = 1
  send_alert_message       = 2
  timeout                  = 3
  block_member_interaction = 4


class AutomodRuleEventType(Enum):
  message_send  = 1
  member_update = 2


class AutomodRuleTriggerType(Enum):
  keyword        = 1
  spam           = 3
  keyword_preset = 4
  mention_spam   = 5
  member_profile = 6


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
  forum               = 15
  media               = 16


class KeywordPresetType(Enum):
  profanity      = 1
  sexual_content = 2
  slurs          = 3