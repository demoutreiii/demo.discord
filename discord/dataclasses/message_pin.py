from .message import Message
from datetime import datetime


class MessagePin(dict):
  @property
  def message(self) -> Message:
    return Message(self["message"])
  
  
  @property
  def pinned_at(self) -> datetime:
    return datetime.fromisotimestamp(self["pinned_at"])