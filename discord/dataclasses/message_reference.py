from ..enums import MessageReferenceType
from .snowflake import Snowflake
from typing import Optional


class MessageReference(dict):
  @property
  def channel_id(self) -> Optional[Snowflake]:
    return Snowflake(self["channel_id"]) if "channel_id" in self else None


  @property
  def fail_if_not_exists(self) -> bool:
    return self.get("fail_if_not_exists", True)


  @property
  def guild_id(self) -> Optional[Snowflake]:
    return Snowflake(self["guild_id"]) if "guild_id" in self else None
  
  
  @property
  def message_id(self) -> Optional[Snowflake]:
    return Snowflake(self["message_id"]) if "message_id" in self else None
  
  
  @property
  def type(self) -> Optional[MessageReferenceType]:
    return MessageReferenceType(self["type"]) if "type" in self else None