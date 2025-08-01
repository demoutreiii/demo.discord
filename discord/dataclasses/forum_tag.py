from .snowflake import Snowflake
from typing import Optional


class ForumTag(dict):
  @property
  def emoji_id(self) -> Optional[Snowflake]:
    return Snowflake(self["emoji_id"]) if self["emoji_id"] is not None else None


  @property
  def emoji_name(self) -> Optional[str]:
    return self["emoji_name"]
  
  
  @property
  def id(self) -> Snowflake:
    return Snowflake(self["id"])


  @property
  def moderated(self) -> bool:
    return self["moderated"]


  @property
  def name(self) -> str:
    return self["name"]