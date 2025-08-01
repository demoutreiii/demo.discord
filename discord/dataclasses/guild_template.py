from .guild import Guild
from .snowflake import Snowflake
from .user import User
from typing import Optional


class GuildTemplate(dict):
  @property
  def code(self) -> str:
    return self["code"]


  @property
  def created_at(self) -> int:
    return self["created_at"]


  @property
  def creator(self) -> User:
    return User(self["creator"])


  @property
  def creator_id(self) -> Snowflake:
    return Snowflake(self["creator_id"])


  @property
  def description(self) -> Optional[str]:
    return self["description"]


  @property
  def is_dirty(self) -> Optional[bool]:
    return self["is_dirty"]


  @property
  def name(self) -> str:
    return self["name"]


  @property
  def serialized_source_guild(self) -> Guild:
    return Guild(self["serialized_source_guild"])


  @property
  def source_guild_id(self) -> Snowflake:
    return Snowflake(self["source_guild_id"])


  @property
  def updated_at(self) -> int:
    return self["updated_at"]


  @property
  def usage_count(self) -> int:
    return self["usage_count"]