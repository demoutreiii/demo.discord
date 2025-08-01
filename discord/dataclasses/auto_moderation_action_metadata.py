from .snowflake import Snowflake


class AutoModerationActionMetadata(dict):
  @property
  def channel_id(self) -> Snowflake:
    return Snowflake(self["channel_id"])


  @property
  def custom_message(self) -> Optional[str]:
    return self.get("custom_message")


  @property
  def duration_seconds(self) -> int:
    return self["duration_seconds"]