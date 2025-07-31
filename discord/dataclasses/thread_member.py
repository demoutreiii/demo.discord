from .guild_member import GuildMember
from .snowflake import Snowflake
from typing import Optional


class ThreadMember(dict):
  def __init__(self, data: dict[str, ...]) -> None:
    self.__data: dict[str, ...] = data


  @property
  def flags(self) -> int:
    return self.__data["flags"]


  @property
  def id(self) -> Optional[Snowflake]:
    return Snowflake(self.__data["id"]) if "id" in self.__data else None


  @property
  def join_timestamp(self) -> int:
    return self.__data["join_timestamp"]


  @property
  def member(self) -> Optional[GuildMember]:
    return GuildMember(self.__data["member"]) if "member" in self.__data else None


  @property
  def user_id(self) -> Optional[Snowflake]:
    return Snowflake(self.__data["user_id"]) if "user_id" in self.__data else None