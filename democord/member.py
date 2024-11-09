from .asset       import Asset
from .channels    import VoiceChannel
from .decoration  import AvatarDecoration
from .permissions import Permissions
from .reqs        import PATCH
from .role        import Role
from .user        import User
from datetime     import (
                         datetime,
                         timedelta
                         )
from typing       import *


class Member:
  @property
  def avatar(self) -> Optional[Asset]:
    # implement: Asset[UserAvatar]
    raise NotImplementedError

  @property
  def avatar_decoration(self) -> Optional[AvatarDecoration]:
    # implement: AvatarDecoration
    raise NotImplementedError

  @property
  def banner(self) -> Optional[Asset]:
    # implement: Asset[UserBanner]
    raise NotImplementedError

  @property
  def deaf(self) -> bool:
    return self["deaf"]

  @property
  def flags(self) -> List[str]:
    # implement: MemberFlags
    raise NotImplementedError

  @property
  def joined_at(self) -> datetime:
    return datetime.fromisoformat(self["joined_at"])

  @property
  def mute(self) -> bool:
    return self["mute"]

  @property
  def nick(self) -> Optional[str]:
    return self["nick"]

  @property
  def pending(self) -> bool:
    return self["pending"]

  @property
  def permissions(self) -> Permissions:
    # implement: Permissions
    raise NotImplementedError

  @property
  def premium_since(self) -> Optional[datetime]:
    if self["premium_since"] is None: return None
    return datetime.fromisoformat(self["premium_since"])

  @property
  def roles(self) -> List[Role]:
    # implement: Role
    raise NotImplementedError

  @property
  def timed_out_until(self) -> Optional[datetime]:
    if self["communication_disabled_until"] is None: return None
    return datetime.fromisoformat(self["communication_disabled_until"])

  @property
  def user(self) -> User:
    # retrieve UserObject from cache by ID
    raise NotImplementedError

  async def add_roles(
    self,
    *roles : Role,
    reason : Optional[str] = None
  ) -> Member:
    try:
      # check permission: manage_roles
      for role in roles:
        if not isinstance(role, Role): raise TypeError("roles: must be of type <Role>")
        if role in self.roles: continue
        response : Dict[str, Any] = self.ws.put(
          PUT.member_role(self.guild.id, self.id, role.id),
          reason = reason
        )
        self : Self = Member.from_data(self.ws, response)
      return self
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)

  async def edit(
    self,
    **attributes
  ) -> Member:
    try:
      data : Dict[str, Any] = {}
      reason : Optional[str] = None
      for attribute in attributes:
        match attribute:
          case "nick":
            if not isinstance(attributes[attribute], str): raise TypeError("nick: must be of type <str>")
            # check permission: manage_nicknames
            data[attribute] : str = attributes[attribute]
          case "roles":
            if isinstance(attributes[attribute], list):
              for role in attributes[attribute]:
                if not isinstance(role, Role): raise ValueError("roles: must contain <Role> objects")
              # check permission: manage_roles
              data[attribute] : List[Role] = [role.id for role in attributes[attribute]]
              data[attribute] += [role.id for role in self.roles if role not in data[attribute]]
            else: raise TypeError("roles: must be of type <list> containing <Role> objects")
          case "mute":
            if not isinstance(attributes[attribute], bool): raise TypeError("mute: must be of type <bool>")
            # check permission: mute_members
            data[attribute] : bool = attributes[attribute]
          case "deaf":
            if not isinstance(attributes[attribute], bool): raise TypeError("deaf: must be of type <bool>")
            # check permission: deafen_members
            data[attribute] : bool = attributes[attribute]
          case "voice_channel":
            if not isinstance(attributes[attribute], VoiceChannel): raise TypeError("voice_channel: must be of type <VoiceChannel>")
            # check permission: move_members
            data[attribute] : int = attributes[attribute].id
          case "reason":
            if not isinstance(attributes[attribute], str): raise TypeError("reason: must be of type <str>")
            reason : Optional[str] = reason
      response : Dict[str, Any] = self.ws.patch(
        PATCH.member(self.guild.id, self.id),
        data = data,
        reason = reason
      )
      self : Self = Member.from_data(self.ws, response)
      return self
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)

  async def kick(
    self,
    reason : Optional[str] = None
  ) -> None:
    try:
      await self.guild.kick(self.id, reason = reason)
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)

  async def remove_roles(
    self,
    *roles : Role,
    reason : Optional[str] = None
  ) -> Member:
    try:
      # check permission: manage_roles
      for role in roles:
        if not isinstance(role, Role): raise TypeError("roles: must be of type <Role>")
        if role in self.roles: continue
        response : Dict[str, Any] = self.ws.delete(
          DELETE.member_role(self.guild.id, self.id, role.id),
          reason = reason
        )
        self : Self = Member.from_data(self.ws, response)
      return self
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)

  async def timeout(
    self,
    until : Optional[timedelta] = None,
    reason : Optional[str] = None
  ) -> Member:
    try:
      if until and not isinstance(until, timedelta): raise TypeError("until: must be of type <timedelta> or <NoneType>")
      if reason and not isinstance(reason, str): raise TypeError("reason: must be of type <str>")
      if until: until += datetime.now()
      response : Dict[str, Any] = self.ws.patch(
        PATCH.member(self.guild.id, self.id),
        data = {
          "communication_disabled_until": until.timestamp()
        },
        reason = reason
      )
      # check permission: moderate_members
      self : Self = Member.from_data(self.ws, response)
      return self
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


class ThreadMember:
  @property
  def id(self) -> int:
    return int(self.__payload["id"])