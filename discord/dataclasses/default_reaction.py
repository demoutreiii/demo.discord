from .snowflake import Snowflake
from typing import Typing


class DefaultReaction(dict):
  @property
  def emoji_id(self) -> Optional[Snowflake]:
    return Snowflake(self["emoji_id"]) if self["emoji_id"] is not None else None


  @property
  def emoji_name(self) -> Optional[str]:
    return self["emoji_name"]