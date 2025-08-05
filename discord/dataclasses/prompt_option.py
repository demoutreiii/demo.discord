from .emoji import Emoji
from .snowflake import Snowflake
from typing import Optional


class PromptOption(dict):
  @property
  def channel_ids(self) -> list[Snowflake]:
    return [Snowflake(data) for data in self["channel_ids"]]


  @property
  def description(self) -> Optional[str]:
    return self["description"]


  @property
  def emoji(self) -> Optional[Emoji]:
    return Emoji(self["emoji"]) if "emoji" in self else None


  @property
  def emoji_animated(self) -> Optional[bool]:
    return self["emoji_animated"] if "emoji_animated" in self else None


  @property
  def emoji_name(self) -> Optional[str]:
    return self["emoji_name"] if "emoji_name" in self else None
  
  
  @property
  def id(self) -> Snowflake:
    return Snowflake(self["id"])


  @property
  def role_ids(self) -> list[Snowflake]:
    return [Snowflake(data) for data in self["role_ids"]]


  @property
  def title(self) -> str:
    return self["title"]