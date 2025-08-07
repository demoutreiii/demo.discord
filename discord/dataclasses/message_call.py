from .snowflake import Snowflake
from datetime import datetime
from typing import Optional


class MessageCall(dict):
  @property
  def ended_timestamp(self) -> Optional[datetime]:
    return datetime.fromisoformat(self["ended_timestamp"]) if self.get("ended_timestamp") is not None else None
  
  
  @property
  def participants(self) -> list[Snowflake]:
    return [Snowflake(data) for data in self["participants"]]