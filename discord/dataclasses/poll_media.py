from .emoji import Emoji
from typing import Optional


class PollMedia(dict):
  @property
  def emoji(self) -> Optional[Emoji]:
    return Emoji(self["emoji"]) if "emoji" in self else None
  
  
  @property
  def text(self) -> Optional[str]:
    return self["text"] if "text" in self else None