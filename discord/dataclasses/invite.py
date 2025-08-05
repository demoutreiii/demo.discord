from ..enums import InviteTargetType, InviteType
from ..flags import GuildInviteFlag
from .application import Application
from .channel import Channel
from .guild import Guild
from .guild_scheduled_event import GuildScheduledEvent
from .invite_stage_instance import InviteStageInstance
from .user import User
from datetime import datetime
from typing import Optional


class Invite(dict):
  @property
  def approximate_member_count(self) -> Optional[int]:
    return self.get("approximate_member_count")
  
  
  @property
  def approximate_presence_count(self) -> Optional[int]:
    return self.get("approximate_presence_count")
  
  
  @property
  def channel(self) -> Optional[Channel]:
    return Channel(self["channel"]) if self["channel"] is not None else None
  
  
  @property
  def code(self) -> str:
    return self["code"]


  @property
  def expires_at(self) -> Optional[datetime]:
    return datetime.fromisoformat(self["expires_at"]) if self.get("expires_at") is not None else None


  @property
  def flags(self) -> Optional[GuildInviteFlag]:
    return GuildInviteFlag(self["flags"]) if "flags" in self else None


  @property
  def guild(self) -> Optional[Guild]:
    return Guild(self["guild"]) if "guild" in self else None


  @property
  def guild_scheduled_event(self) -> Optional[GuildScheduledEvent]:
    return GuildScheduledEvent(self["guild_scheduled_event"]) if "guild_scheduled_event" in self else None


  @property
  def inviter(self) -> Optional[User]:
    return User(self["inviter"]) if "inviter" in self else None


  @property
  def stage_instance(self) -> Optional[InviteStageInstance]:
    return InviteStageInstance(self["stage_instace"]) if "stage_instance" in self else None
  
  
  @property
  def target_application(self) -> Optional[Application]:
    return Application(self["target_application"]) if "target_application" in self else None
  
  
  @property
  def target_type(self) -> Optional[InviteTargetType]:
    return InviteTargetType(self["target_type"]) if "target_type" in self else None


  @property
  def target_user(self) -> Optional[User]:
    return User(self["target_user"]) if "target_user" in self else None
  
  
  @property
  def type(self) -> InviteType:
    return InviteType(self["type"])