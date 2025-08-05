from .snowflake import Snowflake
from typing import Optional


class WelcomeScreenChannel(dict):
  @property
  def channel_id(self) -> Snowflake:
    return Snowflake(self["channel_id"])


  @property
  def description(self) -> str:
    return self["description"]
  
  
  @property
  def emoji_id(self) -> Optional[Snowflake]:
    return Snowflake(self["emoji_id"]) if self["emoji_id"] is not None else None


  @property
  def emoji_name(self) -> Optional[str]:
    return self["emoji_name"]