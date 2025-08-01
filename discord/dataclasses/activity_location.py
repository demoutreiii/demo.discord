from ..enums import ActivityLocationKind
from .snowflake import Snowflake


class ActivityLocation(dict):
  @property
  def channel_id(self) -> Snowflake:
    return self["channel_id"]


  @property
  def guild_id(self) -> Optional[Snowflake]:
    return Snowflake(self["guild_id"]) if self.get("guild_id") is not None else None


  @property
  def id(self) -> str:
    return self["id"]


  @property
  def kind(self) -> ActivityLocationKind:
    return ActivityLocationKind(self["kind"])