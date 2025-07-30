from .application_command import ApplicationCommand
from .audit_log_entry import AuditLogEntry
from .auto_moderation_rule import AutoModerationRule
from .channel import Channel
from .guild_scheduled_event import GuildScheduledEvent
from .integrations import Integration
from .user import User
from .webhook import Webhook


class AuditLog(dict):
  def __init__(self, data: dict[str, ...]) -> None:
    self.__data: dict[str, ...] = data


  @property
  def application_commands(self) -> list[ApplicationCommand]:
    return [ApplicationCommand(application_command_data) for application_command_data in self.__data["application_commands"]]


  @property
  def audit_log_entries(self) -> list[AuditLogEntry]:
    return [AuditLogEntry(audit_log_entry_data) for audit_log_entry_data in self.__data["audit_log_entries"]]


  @property
  def auto_moderation_rules(self) -> list[AutoModerationRule]:
    return [AutoModerationRule(auto_moderation_rule_data) for auto_moderation_rule_data in self.__data["auto_moderation_rules"]]


  @property
  def guild_scheduled_events(self) -> list[GuildScheduledEvent]:
    return [GuildScheduledEvent(guild_scheduled_event_data) for guild_scheduled_event_data in self.__data["guild_scheduled_events"]]


  @property
  def integrations(self) -> list[Integration]:
    return [Integration(integration_data) for integration_data in self.__data["integrations"]]


  @property
  def threads(self) -> list[Channel]:
    return [Channel(thread_data) for thread_data in self.__data["threads"]]


  @property
  def users(self) -> list[User]:
    return [User(user_data) for user_data in self.__data["users"]]


  @property
  def webhooks(self) -> list[Webhook]:
    return [Webhook(webhook_data) for webhook_data in self.__data["webhooks"]]