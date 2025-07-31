from ..enums import ChannelType, ForumLayout, ForumSortOrderType
from .asset import Asset
from .default_reaction import DefaultReaction
from .forum_tag import ForumTag
from .permission_overwrite import PermissionOverwrite
from .snowflake import Snowflake
from .thread_member import ThreadMember
from .thread_metadata import ThreadMetadata
from .user import User
from typing import Optional


class Channel(dict):
  def __init__(self, data: dict[str, ...]) -> None:
    self.__data: dict[str, ...] = data


  @property
  def application_id(self) -> Optional[Snowflake]:
    return Snowflake(self.__data["application_id"]) if "application_id" in self.__data else None


  @property
  def applied_tags(self) -> Optional[list[Snowflake]]:
    return [Snowflake(tag_id) for tag_id in self.__data["applied_tags"]] if "applied_tags" in self.__data else None


  @property
  def available_tags(self) -> Optional[list[ForumTag]]:
    return [ForumTag(forum_tag_data) for forum_tag_data in self.__data["available_tags"]] if "available_tags" in self.__data else None


  @property
  def bitrate(self) -> Optional[int]:
    return self.__data.get("bitrate")


  @property
  def default_auto_archive_duration(self) -> Optional[int]:
    return self.__data.get("default_auto_archive_duration")


  @property
  def default_forum_layout(self) -> Optional[ForumLayoutType]:
    return ForumLayoutType(self.__data["default_forum_layout"]) if "default_forum_layout" in self.__data else None


  @property
  def default_reaction_emoji(self) -> Optional[DefaultReaction]:
    return DefaultReaction(self.__data["default_reaction_emoji"]) if self.__data.get("default_reaction_emoji") is not None else None


  @property
  def default_sort_order(self) -> Optional[ForumSortOrderType]:
    return ForumSortOrderType(self.__data["default_sort_order"]) if self.__data.get("default_sort_order") is not None else None


  @property
  def default_thread_rate_limit_per_user(self) -> Optional[int]:
    return self.__data.get("default_thread_rate_limit_per_user")


  @property
  def flags(self) -> Optional[int]:
    return self.__data.get("flags")


  @property
  def guild_id(self) -> Optional[Snowflake]:
    return Snowflake(self.__data["guild_id"]) if "guild_id" in self.__data else None


  @property
  def icon(self) -> Optional[Asset]:
    return Asset(self.__data["icon"]) if self.__data.get("icon") is not None else None


  @property
  def id(self) -> Snowflake:
    return Snowflake(self.__data["id"])


  @property
  def last_message_id(self) -> Optional[Snowflake]:
    return Snowflake(self.__data["last_message_id"]) if "last_message_id" in self.__data else None


  @property
  def last_pin_timestamp(self) -> Optional[int]:
    return self.__data.get("last_pin_timestamp")


  @property
  def managed(self) -> bool:
    return self.__data.get("managed", False)


  @property
  def member(self) -> Optional[ThreadMember]:
    return ThreadMember(self.__data["member"]) if "member" in self.__data else None


  @property
  def member_count(self) -> Optional[int]:
    return self.__data.get("member_count")


  @property
  def message_count(self) -> Optional[int]:
    return self.__data.get("message_count")


  @property
  def name(self) -> Optional[str]:
    return self.__data.get("name")


  @property
  def nsfw(self) -> bool:
    return self.__data.get("nsfw", False)


  @property
  def owner_id(self) -> Optional[Snowflake]:
    return Snowflake(self.__data["owner_id"]) if "owner_id" in self.__data else None


  @property
  def parent_id(self) -> Optional[Snowflake]:
    return Snowflake(self.__data["parent_id"]) if self.__data.get("parent_id") is not None else None


  @property
  def permission_overwrites(self) -> Optional[list[PermissionOverwrite]]:
    return [PermissionOverwrite(permission_overwrite_data) for permission_overwrite_data in self.__data["permission_overwrites"]] if "permission_overwrites" in self.__data else None


  @property
  def permissions(self) -> Optional[str]:
    return self.__data.get("permissions")


  @property
  def position(self) -> Optional[int]:
    return self.__data.get("position")


  @property
  def rate_limit_per_user(self) -> Optional[int]:
    return self.__data.get("rate_limit_per_user")


  @property
  def recipients(self) -> Optional[list[User]]:
    return [User(user_data) for user_data in self.__data["recipients"]] if "recipients" in self.__data else None


  @property
  def rtc_region(self) -> Optional[str]:
    return self.__data.get("rtc_region")


  @property
  def thread_metadata(self) -> Optional[ThreadMetadata]:
    return ThreadMetadata(self.__data["thread_metadata"]) if "thread_metadata" in self.__data else None


  @property
  def topic(self) -> Optional[str]:
    return self.__data.get("topic")


  @property
  def total_message_sent(self) -> Optional[int]:
    return self.__data.get("total_message_sent")


  @property
  def type(self) -> ChannelType:
    return ChannelType(self.__data["type"])


  @property
  def user_limit(self) -> Optional[int]:
    return self.__data.get("user_limit")


  @property
  def video_quality_mode(self) -> Optional[int]:
    return self.__data.get("video_quality_mode")