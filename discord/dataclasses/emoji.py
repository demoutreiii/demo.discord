from .snowflake import Snowflake
from .user import User
from typing import Optional


class Emoji(dict):
  @property
  def animated(self) -> bool:
    return self.get("animated", False)


  @property
  def available(self) -> bool:
    return self.get("available", True)
  
  
  @property
  def id(self) -> Optional[Snowflake]:
    return Snowflake(self["id"]) if self["id"] is not None else None


  @property
  def managed(self) -> bool:
    return self.get("managed", False)


  @property
  def name(self) -> Optional[str]:
    return self["name"]


  @property
  def require_colons(self) -> bool:
    return self.get("require_colons", True)


  @property
  def roles(self) -> list[Snowflake]:
    return [Snowflake(role_id) for role_id in self["roles"]]


  @property
  def user(self) -> Optional[User]:
    return User(self["user"]) if "user" in self else None