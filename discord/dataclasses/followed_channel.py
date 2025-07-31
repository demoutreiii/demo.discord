from .snowflake import Snowflake


class FollowedChannel(dict):
  def __init__(self, data: dict[str, ...]) -> None:
    self.__data: dict[str, ...] = data


  @property
  def channel_id(self) -> Snowflake:
    return Snowflake(self.__data["channel_id"])


  @property
  def webhook_id(self) -> Snowflake:
    return Snowflake(self.__data["webhook_id"])