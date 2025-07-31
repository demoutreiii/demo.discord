from .snowflake import Snowflake


class AutoModerationActionMetadata(dict):
  def __init__(self, data: dict[str, ...]) -> None:
    self.__data: dict[str, ...] = data


  @property
  def channel_id(self) -> Snowflake:
    return Snowflake(self.__data["channel_id"])


  @property
  def custom_message(self) -> Optional[str]:
    return self.__data.get("custom_message")


  @property
  def duration_seconds(self) -> int:
    return self.__data["duration_seconds"]