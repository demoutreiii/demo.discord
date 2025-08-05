from .channel import Channel
from .snowflake import Snowflake
from .user import User
from typing import Optional


class GuildWidget(dict):
  @property
  def channels(self) -> list[Channel]:
    return [Channel(data) for data in self["channels"]]
  
  
  @property
  def id(self) -> Snowflake:
    return Snowflake(self["id"])


  @property
  def instant_invite(self) -> Optional[str]:
    return self["instant_invite"]


  @property
  def members(self) -> list[User]:
    return [User(data) for data in self["members"]]


  @property
  def name(self) -> str:
    return self["name"]


  @property
  def presence_count(self) -> int:
    return self["presence_count"]