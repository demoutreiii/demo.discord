from .appinfo          import AppInfo
from .enums            import (
                              InviteTargetType,
                              InviteType
                              )
from .guild            import Guild
from .scheduled_events import ScheduledEvent
from .user             import User
from datetime          import datetime
from typing            import *


class Invite:
  @property
  def approximate_member_count(self) -> Optional[int]:
    if self["approximate_member_count"] is None: return None
    return self["approximate_member_count"]
  
  @property
  def approximate_presence_count(self) -> Optional[int]:
    if self["approximate_presence_count"] is None: return None
    return self["approximate_presence_count"]

  @property
  def channel(self) -> Optional[Union[DMChannel, GuildChannel]]:
    from .constructor import Constructor
    return Constructor.channel(self["channel"]) if self["channel"] is not None else None

  @property
  def code(self) -> str:
    return self["code"]

  @property
  def expires_at(self) -> Optional[datetime]:
    if self["expires_at"] is None: return None
    return datetime.fromisoformat(self["expires_at"])

  @property
  def guild(self) -> Optional[Guild]:
    if self["guild"] is None: return None
    from .constructor import Constructor
    return Constructor.guild(self["guild"])

  @property
  def guild_scheduled_event(self) -> ScheduledEvent:
    # implement: ScheduledEvent
    raise NotImplementedError

  @property
  def inviter(self) -> Optional[User]:
    if self["inviter"] is None: return None
    from .constructor import Constructor
    return Constructor.user(self["inviter"])

  @property
  def target_application(self) -> Optional[AppInfo]:
    if self["target_application"] is None: return None
    from .constructor import Constructor
    return Constructor.info(self["target_application"])

  @property
  def target_type(self) -> Optional[str]:
    if self["target_type"] is None: return None
    return InviteTargeType(self["target_type"]).name

  @property
  def target_user(self) -> Optional[User]:
    if self["target_user"] is None: return None
    from .constructor import Constructor
    return Constructor.user(self["target_user"])

  @property
  def type(self) -> InviteType:
    return InviteType(self["type"])


class InviteTarget: ...