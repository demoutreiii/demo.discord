from ..enums import ChannelType
from .snowflake import Snowflake


class ChannelMention(dict):
  @property
  def guild_id(self) -> Snowflake:
    return Snowflake(self["guild_id"])
  
  
  @property
  def id(self) -> Snowflake:
    return Snowflake(self["id"])


  @property
  def name(self) -> str:
    return self["name"]


  @property
  def type(self) -> ChannelType:
    return ChannelType(self["type"])