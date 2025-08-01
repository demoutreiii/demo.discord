from .snowflake import Snowflake


class PermissionOverwrite(dict):
  @property
  def allow(self) -> str:
    return self["allow"]


  @property
  def deny(self) -> str:
    return self["deny"]


  @property
  def id(self) -> Snowflake:
    return Snowflake(self["id"])


  @property
  def type(self) -> int:
    return self["type"]