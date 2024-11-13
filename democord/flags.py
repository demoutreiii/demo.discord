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


class SystemChannelFlag(IntFlag):
  suppress_join_notifications                              = 1 << 0
  suppress_premium_subscriptions                           = 1 << 1
  suppress_guild_reminder_notifications                    = 1 << 2
  suppress_join_notification_replies                       = 1 << 3
  suppress_role_subscription_purchase_notifications        = 1 << 4
  suppress_role_subscription_purchase_notification_replies = 1 << 5