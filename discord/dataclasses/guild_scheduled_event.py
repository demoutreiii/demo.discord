from ..enums import GuildScheduledEventEntityType, GuildScheduledEventPrivacyLevel, GuildScheduledEventStatus
from .asset import Asset
from .guild_scheduled_event_entity_metadata import GuildScheduledEventEntityMetadata
from .guild_scheduled_event_recurrence_rule import GuildScheduledEventRecurrenceRule
from .snowflake import Snowflake
from .user import User
from datetime import datetime
from typing import Optional


class GuildScheduledEvent(dict):
  @property
  def channel_id(self) -> Optional[Snowflake]:
    return Snowflake(self["channel_id"]) if self["channel_id"] is not None else None


  @property
  def creator(self) -> Optional[User]:
    return User(self["creator"]) if "creator" in self else None


  @property
  def creator_id(self) -> Optional[Snowflake]:
    return Snowflake(self["creator_id"]) if self.get("creator_id") is not None else None


  @property
  def description(self) -> Optional[str]:
    return self.get("description")


  @property
  def entity_id(self) -> Optional[Snowflake]:
    return Snowflake(self["entity_id"]) if self["entity_id"] is not None else None


  @property
  def entity_metadata(self) -> Optional[GuildScheduledEventEntityMetadata]:
    return GuildScheduledEventEntityMetadata(self["entity_metadata"]) if self["entity_metadata"] is not None else None


  @property
  def entity_type(self) -> GuildScheduledEventEntityType:
    return GuildScheduledEventEntityType(self["entity_type"])
  
  
  @property
  def guild_id(self) -> Snowflake:
    return Snowflake(self["guild_id"])
  
  
  @property
  def id(self) -> Snowflake:
    return Snowflake(self["id"])


  @property
  def image(self) -> Optional[Asset]:
    return Asset(self["image"]) if self.get("image") is not None else None


  @property
  def name(self) -> str:
    return self["name"]


  @property
  def privacy_level(self) -> GuildScheduledEventPrivacyLevel:
    return GuildScheduledEventPrivacyLevel(self["privacy_level"])


  @property
  def recurrence_rule(self) -> Optional[GuildScheduledEventRecurrenceRule]:
    return GuildScheduledEventRecurrenceRule(self["recurrence_rule"]) if self["recurrence_rule"] is not None else None


  @property
  def scheduled_end_time(self) -> Optional[datetime]:
    return datetime.fromisoformat(self["scheduled_end_time"]) if self["scheduled_end_time"] is not None else None


  @property
  def scheduled_start_time(self) -> datetime:
    return datetime.fromisoformat(self["scheduled_start_time"])


  @property
  def status(self) -> GuildScheduledEventStatus:
    return GuildScheduledEventStatus(self["status"])


  @property
  def user_count(self) -> Optional[int]:
    return self["user_count"] if "user_count" in self else None