from .asset import Asset
from .user import User
from .snowflake import Snowflake
from typing import Optional


class IntegrationApplication(dict):
  @property
  def bot(self) -> Optional[User]:
    return User(self["bot"]) if "bot" in self else None
  
  
  @property
  def description(self) -> str:
    return self["description"]
  
  
  @property
  def icon(self) -> Optional[Asset]:
    return Asset(self["icon"]) if self["icon"] is not None else None
  
  
  @property
  def id(self) -> Snowflake:
    return Snowflake(self["id"])


  @property
  def name(self) -> str:
    return self["name"]