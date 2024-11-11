from .base  import BaseObject
from typing import *


class AuditLogObject(BaseObject):
  from .application_command   import ApplicationCommandObject
  from .audit_log_entry       import AuditLogEntryObject
  from .auto_moderation_rule  import AutoModerationRuleObject
  from .guild_scheduled_event import GuildScheduledEventObject
  from .integration           import IntegrationObject
  from .channel               import ChannelObject
  from .user                  import UserObject
  from .webhook               import WebhookObject

  application_commands   : List[ApplicationCommandObject]  = []
  audit_log_entries      : List[AuditLogEntryObject]       = []
  auto_moderation_rules  : List[AutoModerationRuleObject]  = []
  guild_scheduled_events : List[GuildScheduledEventObject] = []
  integrations           : List[IntegrationObject]         = []
  threads                : List[ChannelObject]             = []
  users                  : List[UserObject]                = []
  webhooks               : List[WebhookObject]             = []