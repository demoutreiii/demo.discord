from .snowflake import Snowflake


class OptionalAuditEntryInfo(dict):
  def __init__(self, data: dict[str, ...]) -> None:
    self.__data: dict[str, ...] = data


  @property
  def application_id(self) -> Optional[Snowflake]:
    return Snowflake(self.__data["application_id"]) if "application_id" in self.__data else None


  @property
  def auto_moderation_rule_name(self) -> Optional[str]:
    return self.__data.get("auto_moderation_rule_name")


  @property
  def auto_moderation_rule_trigger_type(self) -> Optional[str]:
    return self.__data.get("auto_moderation_rule_trigger_type")


  @property
  def channel_id(self) -> Optional[Snowflake]:
    return Snowflake(self.__data["channel_id"]) if "channel_id" in self.__data else None


  @property
  def count(self) -> Optional[str]:
    return self.__data.get("count")


  @property
  def delete_member_days(self) -> Optional[str]:
    return self.__data.get("delete_member_days")


  @property
  def id(self) -> Optional[Snowflake]:
    return Snowflake(self.__data["id"]) if "id" in self.__data else None


  @property
  def integration_type(self) -> Optional[str]:
    return self.__data.get("integration_type")


  @property
  def members_removed(self) -> Optional[str]:
    return self.__data.get("members_removed")


  @property
  def message_id(self) -> Optional[Snowflake]:
    return Snowflake(self.__data["message_id"]) if "message_id" in self.__data else None


  @property
  def role_name(self) -> Optional[str]:
    return self.__data.get("role_name")


  @property
  def type(self) -> Optional[str]:
    return self.__data.get("type")