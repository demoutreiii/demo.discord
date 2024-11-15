from enum   import IntFlag
from typing import *


class ApplicationFlag(IntFlag):
  application_auto_moderation_rule_create_badge = 1 <<  6
  gateway_presence                              = 1 << 12
  gateway_presence_limited                      = 1 << 13
  gateway_guild_members                         = 1 << 14
  gateway_guild_members_limited                 = 1 << 15
  verification_pending_guild_limit              = 1 << 16
  embedded                                      = 1 << 17
  gateway_message_content                       = 1 << 18
  gateway_message_content_limited               = 1 << 19
  application_command_badge                     = 1 << 23


class ChannelFlag(IntFlag):
  pinned                      = 1 <<  1
  require_tag                 = 1 <<  4
  hide_media_download_options = 1 << 15


class MemberFlag(IntFlag):
  did_rejoin                      = 1 << 0
  completed_onboarding            = 1 << 1
  bypasses_verification           = 1 << 2
  started_onboarding              = 1 << 3
  is_guest                        = 1 << 4
  started_home_acitons            = 1 << 5
  completed_home_actions          = 1 << 6
  automod_quarantined_username    = 1 << 7
  dm_settings_upsell_acknowledged = 1 << 9


class SystemChannelFlag(IntFlag):
  suppress_join_notifications                              = 1 << 0
  suppress_premium_subscriptions                           = 1 << 1
  suppress_guild_reminder_notifications                    = 1 << 2
  suppress_join_notification_replies                       = 1 << 3
  suppress_role_subscription_purchase_notifications        = 1 << 4
  suppress_role_subscription_purchase_notification_replies = 1 << 5