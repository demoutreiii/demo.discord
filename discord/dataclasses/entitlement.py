from ..enums import EntitlementType
from .snowflake import Snowflake
from typing import Optional


class Entitlement(dict):
  @property
  def application_id(self) -> Snowflake:
    return Snowflake(self["application_id"])
  
  
  @property
  def consumed(self) -> bool:
    return self.get("consumed", False)
  
  
  @property
  def deleted(self) -> bool:
    return self["deleted"]
  
  
  @property
  def ends_at(self) -> Optional[int]:
    return self["ends_at"]
  
  
  @property
  def guild_id(self) -> Optional[Snowflake]:
    return Snowflake(self["guild_id"]) if "guild_id" in self else None
  
  
  @property
  def id(self) -> Snowflake:
    return Snowflake(self["id"])


  @property
  def sku_id(self) -> Snowflake:
    return Snowflake(self["sku_id"])


  @property
  def starts_at(self) -> Optional[int]:
    return self["starts_at"]


  @property
  def type(self) -> EntitlementType:
    return EntitlementType(self["type"])


  @property
  def user_id(self) -> Optional[Snowflake]:
    return Snowflake(self["user_id"]) if "user_id" in self else None