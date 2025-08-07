from .message import Message


class MessageSnapshot(dict):
  @property
  def message(self) -> Message:
    return Message(self["message"])