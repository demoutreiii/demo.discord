from .snowflake import Snowflake
from typing import Optional


class GuildWidgetSettings(dict):
  @property
  def channel_id(self) -> Optional[Snowflake]:
    return Snowflake(self["channel_id"]) if self["channel_id"] is not None else None
  
  
  @property
  def enabled(self) -> bool:
    return self["enabled"]