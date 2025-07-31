from .snowflake import Snowflake


class PermissionOverwrite(dict):
  def __init__(self, data: dict[str, ...]) -> None:
    self.__data: dict[str, ...] = data


  @property
  def allow(self) -> str:
    return self.__data["allow"]


  @property
  def deny(self) -> str:
    return self.__data["deny"]


  @property
  def id(self) -> Snowflake:
    return Snowflake(self.__data["id"])


  @property
  def type(self) -> int:
    return self.__data["type"]