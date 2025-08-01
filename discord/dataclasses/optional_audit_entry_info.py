from .snowflake import Snowflake


class OptionalAuditEntryInfo(dict):
  @property
  def application_id(self) -> Optional[Snowflake]:
    return Snowflake(self["application_id"]) if "application_id" in self else None


  @property
  def auto_moderation_rule_name(self) -> Optional[str]:
    return self.get("auto_moderation_rule_name")


  @property
  def auto_moderation_rule_trigger_type(self) -> Optional[str]:
    return self.get("auto_moderation_rule_trigger_type")


  @property
  def channel_id(self) -> Optional[Snowflake]:
    return Snowflake(self["channel_id"]) if "channel_id" in self else None


  @property
  def count(self) -> Optional[str]:
    return self.get("count")


  @property
  def delete_member_days(self) -> Optional[str]:
    return self.get("delete_member_days")


  @property
  def id(self) -> Optional[Snowflake]:
    return Snowflake(self["id"]) if "id" in self else None


  @property
  def integration_type(self) -> Optional[str]:
    return self.get("integration_type")


  @property
  def members_removed(self) -> Optional[str]:
    return self.get("members_removed")


  @property
  def message_id(self) -> Optional[Snowflake]:
    return Snowflake(self["message_id"]) if "message_id" in self else None


  @property
  def role_name(self) -> Optional[str]:
    return self.get("role_name")


  @property
  def type(self) -> Optional[str]:
    return self.get("type")