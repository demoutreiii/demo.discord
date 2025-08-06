from ..enums import MessageActivityType
from typing import Optional


class MessageActivity(dict):
  @property
  def party_id(self) -> Optional[str]:
    return self["party_id"] if "party_id" in self else None
  
  
  @property
  def type(self) -> MessageActivityType:
    return MessageActivityType(self["type"])