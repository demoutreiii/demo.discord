from .guild_member import GuildMember
from .snowflake import Snowflake
from .user import User
from typing import Optional


class GuildScheduledEventUser(dict):
  @property
  def guild_scheduled_event_id(self) -> Snowflake:
    return Snowflake(self["guild_scheduled_event_id"])


  @property
  def member(self) -> Optional[GuildMember]:
    return GuildMember(self["member"]) if "member" in self else None


  @property
  def user(self) -> User:
    return User(self["user"])