from ..flags import GuildMemberFlag
from .asset import Asset
from .avatar_decoration_data import AvatarDecorationData
from .snowflake import Snowflake
from .user import User
from typing import Optional


class GuildMember(dict):
  @property
  def avatar(self) -> Optional[Asset]:
    return Asset(self["avatar"]) if self.get("avatar") is not None else None


  @property
  def avatar_decoration_data(self) -> Optional[AvatarDecorationData]:
    return AvatarDecorationData(self["avatar_decoration_data"]) if self.get("avatar_decoration_data") is not None else None


  @property
  def banner(self) -> Optional[Asset]:
    return Asset(self["banner"]) if self.get("banner") is not None else None


  @property
  def communication_disabled_until(self) -> Optional[int]:
    return self.get("communication_disabled_until")


  @property
  def deaf(self) -> bool:
    return self["deaf"]


  @property
  def flags(self) -> GuildMemberFlag:
    return GuildMemberFlag(self["flags"])
  
  
  @property
  def joined_at(self) -> Optional[int]:
    return self["joined_at"]


  @property
  def mute(self) -> bool:
    return self["mute"]
  
  
  @property
  def nick(self) -> Optional[str]:
    return self.get("nick")


  @property
  def pending(self) -> Optional[bool]:
    return self.get("pending")


  @property
  def permissions(self) -> Optional[str]:
    return self.get("permissions")
  
  
  @property
  def premium_since(self) -> Optional[int]:
    return self.get("premium_since")
  
  
  @property
  def roles(self) -> list[Snowflake]:
    return [Snowflake(data) for data in self["roles"]]
  
  
  @property
  def user(self) -> Optional[User]:
    return User(self["user"]) if "user" in self else None