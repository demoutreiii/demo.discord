from ..flags import LobbyMemberFlag
from .snowflake import Snowflake
from typing import Optional


class LobbyMember(dict):
  @property
  def flags(self) -> Optional[LobbyMemberFlag]:
    return LobbyMemberFlag(self["flags"]) if "flags" in self else None
  
  
  @property
  def id(self) -> Snowflake:
    return Snowflake(self["id"])


  @property
  def metadata(self) -> Optional[dict[str, str]]:
    return self.get("metadata")