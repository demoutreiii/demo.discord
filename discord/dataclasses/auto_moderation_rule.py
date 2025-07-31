from ..enums import AutoModerationRuleEventType, AutoModerationRuleTriggerType
from .auto_moderation_action import AutoModerationAction
from .auto_moderation_rule_trigger_metadata import AutoModerationRuleTriggerMetadata
from .snowflake import Snowflake


class AutoModerationRule(dict):
  def __init__(self, data: dict[str, ...]) -> None:
    self.__data: dict[str, ...] = data


  @property
  def actions(self) -> list[AutoModerationAction]:
    return [AutoModerationAction(auto_moderation_action_data) for auto_moderation_action_data in self.__data["actions"]]


  @property
  def creator_id(self) -> Snowflake:
    return Snowflake(self.__data["creator_id"])


  @property
  def enabled(self) -> bool:
    return self.__data["enabled"]


  @property
  def event_type(self) -> AutoModerationRuleEventType:
    return AutoModerationRuleEventType(self.__data["event_type"])


  @property
  def exempt_channels(self) -> list[Snowflake]:
    return [Snowflake(channel_id) for channel_id in self.__data["exempt_channels"]]


  @property
  def exempt_roles(self) -> list[Snowflake]:
    return [Snowflake(role_id) for role_id in self.__data["exempt_roles"]]


  @property
  def guild_id(self) -> Snowflake:
    return Snowflake(self.__data["guild_id"])


  @property
  def id(self) -> Snowflake:
    return Snowflake(self.__data["id"])


  @property
  def name(self) -> str:
    return self.__data["name"]


  @property
  def trigger_metadata(self) -> AutoModerationRuleTriggerMetadata:
    return AutoModerationRuleTriggerMetadata(self.__data["trigger_metadata"])


  @property
  def trigger_type(self) -> AutoModerationRuleTriggerType:
    return AutoModerationRuleTriggerType(self.__data["trigger_type"])