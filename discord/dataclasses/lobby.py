from .channel import Channel
from .lobby_member import LobbyMember
from .snowflake import Snowflake
from typing import Optional


class Lobby(dict):
  @property
  def application_id(self) -> Snowflake:
    return Snowflake(self["application_id"])
  
  
  @property
  def id(self) -> Snowflake:
    return Snowflake(self["id"])


  @property
  def linked_channel(self) -> Optional[Channel]:
    return Channel(self["linked_channel"]) if "linked_channel" in self else None


  @property
  def members(self) -> list[LobbyMember]:
    return [LobbyMember(data) for data in self["members"]]


  @property
  def metadata(self) -> Optional[dict[str, str]]:
    return self["metadata"]