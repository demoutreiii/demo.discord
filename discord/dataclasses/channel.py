from ..enums import ChannelType, ForumLayout, ForumSortOrderType
from .asset import Asset
from .default_reaction import DefaultReaction
from .forum_tag import ForumTag
from .permission_overwrite import PermissionOverwrite
from .snowflake import Snowflake
from .thread_member import ThreadMember
from .thread_metadata import ThreadMetadata
from .user import User
from datetime import datetime
from typing import Optional


class Channel(dict):
  @property
  def application_id(self) -> Optional[Snowflake]:
    return Snowflake(self["application_id"]) if "application_id" in self else None


  @property
  def applied_tags(self) -> Optional[list[Snowflake]]:
    return [Snowflake(tag_id) for tag_id in self["applied_tags"]] if "applied_tags" in self else None


  @property
  def available_tags(self) -> Optional[list[ForumTag]]:
    return [ForumTag(forum_tag_data) for forum_tag_data in self["available_tags"]] if "available_tags" in self else None


  @property
  def bitrate(self) -> Optional[int]:
    return self.get("bitrate")


  @property
  def default_auto_archive_duration(self) -> Optional[int]:
    return self.get("default_auto_archive_duration")


  @property
  def default_forum_layout(self) -> Optional[ForumLayoutType]:
    return ForumLayoutType(self["default_forum_layout"]) if "default_forum_layout" in self else None


  @property
  def default_reaction_emoji(self) -> Optional[DefaultReaction]:
    return DefaultReaction(self["default_reaction_emoji"]) if self.get("default_reaction_emoji") is not None else None


  @property
  def default_sort_order(self) -> Optional[ForumSortOrderType]:
    return ForumSortOrderType(self["default_sort_order"]) if self.get("default_sort_order") is not None else None


  @property
  def default_thread_rate_limit_per_user(self) -> Optional[int]:
    return self.get("default_thread_rate_limit_per_user")


  @property
  def flags(self) -> Optional[int]:
    return self.get("flags")


  @property
  def guild_id(self) -> Optional[Snowflake]:
    return Snowflake(self["guild_id"]) if "guild_id" in self else None


  @property
  def icon(self) -> Optional[Asset]:
    return Asset(self["icon"]) if self.get("icon") is not None else None


  @property
  def id(self) -> Snowflake:
    return Snowflake(self["id"])


  @property
  def last_message_id(self) -> Optional[Snowflake]:
    return Snowflake(self["last_message_id"]) if "last_message_id" in self else None


  @property
  def last_pin_timestamp(self) -> Optional[datetime]:
    return datetime.fromisoformat(self.get("last_pin_timestamp")) if self.get("last_pin_timestamp") is not None else None


  @property
  def managed(self) -> bool:
    return self.get("managed", False)


  @property
  def member(self) -> Optional[ThreadMember]:
    return ThreadMember(self["member"]) if "member" in self else None


  @property
  def member_count(self) -> Optional[int]:
    return self.get("member_count")


  @property
  def message_count(self) -> Optional[int]:
    return self.get("message_count")


  @property
  def name(self) -> Optional[str]:
    return self.get("name")


  @property
  def nsfw(self) -> bool:
    return self.get("nsfw", False)


  @property
  def owner_id(self) -> Optional[Snowflake]:
    return Snowflake(self["owner_id"]) if "owner_id" in self else None


  @property
  def parent_id(self) -> Optional[Snowflake]:
    return Snowflake(self["parent_id"]) if self.get("parent_id") is not None else None


  @property
  def permission_overwrites(self) -> Optional[list[PermissionOverwrite]]:
    return [PermissionOverwrite(permission_overwrite_data) for permission_overwrite_data in self["permission_overwrites"]] if "permission_overwrites" in self else None


  @property
  def permissions(self) -> Optional[str]:
    return self.get("permissions")


  @property
  def position(self) -> Optional[int]:
    return self.get("position")


  @property
  def rate_limit_per_user(self) -> Optional[int]:
    return self.get("rate_limit_per_user")


  @property
  def recipients(self) -> Optional[list[User]]:
    return [User(user_data) for user_data in self["recipients"]] if "recipients" in self else None


  @property
  def rtc_region(self) -> Optional[str]:
    return self.get("rtc_region")


  @property
  def thread_metadata(self) -> Optional[ThreadMetadata]:
    return ThreadMetadata(self["thread_metadata"]) if "thread_metadata" in self else None


  @property
  def topic(self) -> Optional[str]:
    return self.get("topic")


  @property
  def total_message_sent(self) -> Optional[int]:
    return self.get("total_message_sent")


  @property
  def type(self) -> ChannelType:
    return ChannelType(self["type"])


  @property
  def user_limit(self) -> Optional[int]:
    return self.get("user_limit")


  @property
  def video_quality_mode(self) -> Optional[int]:
    return self.get("video_quality_mode")