from ..enums import ActivityLocationKind
from .snowflake import Snowflake


class ActivityLocation(dict):
  def __init__(self, data: dict[str, ...]) -> None:
    self.__data: dict[str, ...] = data


  @property
  def channel_id(self) -> Snowflake:
    return self.__data["channel_id"]


  @property
  def guild_id(self) -> Optional[Snowflake]:
    return Snowflake(self.__data["guild_id"]) if self.__data.get("guild_id") is not None else None


  @property
  def id(self) -> str:
    return self.__data["id"]


  @property
  def kind(self) -> ActivityLocationKind:
    return ActivityLocationKind(self.__data["kind"])