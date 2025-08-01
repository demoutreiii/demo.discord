from ..enums import AutoModerationRuleEventType, AutoModerationRuleTriggerType
from .auto_moderation_action import AutoModerationAction
from .auto_moderation_rule_trigger_metadata import AutoModerationRuleTriggerMetadata
from .snowflake import Snowflake


class AutoModerationRule(dict):
  @property
  def actions(self) -> list[AutoModerationAction]:
    return [AutoModerationAction(auto_moderation_action_data) for auto_moderation_action_data in self["actions"]]


  @property
  def creator_id(self) -> Snowflake:
    return Snowflake(self["creator_id"])


  @property
  def enabled(self) -> bool:
    return self["enabled"]


  @property
  def event_type(self) -> AutoModerationRuleEventType:
    return AutoModerationRuleEventType(self["event_type"])


  @property
  def exempt_channels(self) -> list[Snowflake]:
    return [Snowflake(channel_id) for channel_id in self["exempt_channels"]]


  @property
  def exempt_roles(self) -> list[Snowflake]:
    return [Snowflake(role_id) for role_id in self["exempt_roles"]]


  @property
  def guild_id(self) -> Snowflake:
    return Snowflake(self["guild_id"])


  @property
  def id(self) -> Snowflake:
    return Snowflake(self["id"])


  @property
  def name(self) -> str:
    return self["name"]


  @property
  def trigger_metadata(self) -> AutoModerationRuleTriggerMetadata:
    return AutoModerationRuleTriggerMetadata(self["trigger_metadata"])


  @property
  def trigger_type(self) -> AutoModerationRuleTriggerType:
    return AutoModerationRuleTriggerType(self["trigger_type"])