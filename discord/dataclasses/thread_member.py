from .guild_member import GuildMember
from .snowflake import Snowflake
from .datetime import datetime
from typing import Optional


class ThreadMember(dict):
  @property
  def flags(self) -> int:
    return self["flags"]


  @property
  def id(self) -> Optional[Snowflake]:
    return Snowflake(self["id"]) if "id" in self else None


  @property
  def join_timestamp(self) -> datetime:
    return datetime.fromisoformat(self["join_timestamp"])


  @property
  def member(self) -> Optional[GuildMember]:
    return GuildMember(self["member"]) if "member" in self else None


  @property
  def user_id(self) -> Optional[Snowflake]:
    return Snowflake(self["user_id"]) if "user_id" in self else None