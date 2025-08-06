from ..enums import MessageType
from ..flags import MessageFlag
from ..ui import Component
from .application import Application
from .attachment import Attachment
from .channel import Channel
from .channel_mention import ChannelMention
from .embed import Embed
from .message_activity import MessageActivity
from .message_call import MessageCall
from .message_interaction_metadata import MessageInteractionMetadata
from .message_reference import MessageReference
from .message_snapshot import MessageSnapshot
from .poll import Poll
from .reaction import Reaction
from .resolved_data import ResolvedData
from .role_subscription_data import RoleSubscriptionData
from .snowflake import Snowflake
from .sticker import Sticker
from .sticker_item import StickerItem
from .user import User
from datetime import datetime
from typing import Optional, Self, Union


class Message(dict):
  @property
  def activity(self) -> Optional[MessageActivity]:
    return MessageActivity(self["activity"]) if "activity" in self else None


  @property
  def application(self) -> Optional[Application]:
    return Application(self["application"]) if "application" in self else None


  @property
  def application_id(self) -> Optional[Snowflake]:
    return Snowflake(self["application_id"]) if "application_id" in self else None
  
  
  @property
  def attachments(self) -> list[Attachment]:
    return [Attachment(data) for data in self["attachments"]]


  @property
  def call(self) -> Optional[MessageCall]:
    return MessageCall(self["call"]) if "call" in self else None
  
  
  @property
  def channel_id(self) -> Snowflake:
    return Snowflake(self["channel_id"])
  
  
  @property
  def components(self) -> Optional[list[Component]]:
    return [Component(data) for data in self["components"]] if "components" in self else None
  
  
  @property
  def content(self) -> str:
    return self["content"]


  @property
  def edited_timestamp(self) -> Optional[datetime]:
    return datetime.fromisoformat(self["edited_timestamp"]) if self["edited_timestamp"] is not None else None


  @property
  def embeds(self) -> list[Embed]:
    return [Embed(data) for data in self["embeds"]]


  @property
  def flags(self) -> Optional[MessageFlag]:
    return MessageFlag(self["flags"]) if "flags" in self else None
  
  
  @property
  def id(self) -> Snowflake:
    return Snowflake(self["id"])


  @property
  def interaction_metadata(self) -> Optional[MessageInteractionMetadata]:
    return MessageInteractionMetadata(self["interaction_metadata"]) if "interaction_metadata" in self else None


  @property
  def mention_channels(self) -> list[ChannelMention]:
    return [ChannelMention(data) for data in self["mention_channels"]]


  @property
  def mention_everyone(self) -> bool:
    return self["mention_everyone"]


  @property
  def mention_roles(self) -> list[Snowflake]:
    return [Snowflake(data) for data in self["mention_roles"]]


  @property
  def mentions(self) -> list[User]:
    return [User(data) for data in self["mentions"]]


  @property
  def message_reference(self) -> Optional[MessageReference]:
    return MessageReference(self["message_reference"]) if "message_reference" in self else None


  @property
  def message_snapshost(self) -> Optional[list[MessageSnapshot]]:
    return [MessageSnapshot(data) for data in self["message_snapshots"]] if "message_snapshots" in self else None


  @property
  def nonce(self) -> Optional[Union[int, str]]:
    return self["nonce"] if "nonce" in self else None


  @property
  def pinned(self) -> bool:
    return self["pinned"]


  @property
  def poll(self) -> Optional[Poll]:
    return Poll(self["poll"]) if "poll" in self else None


  @property
  def position(self) -> Optional[int]:
    return self["position"] if "position" in self else None


  @property
  def reactions(self) -> list[Reaction]:
    return [Reaction(data) for data in self["reactions"]]


  @property
  def referenced_message(self) -> Optional[Self]:
    return Message(self["referenced_message"]) if self.get("referenced_message") is not None else None


  @property
  def resolved(self) -> Optional[ResolvedData]:
    return ResolvedData(self["resolved"]) if "resolved" in self else None


  @property
  def role_subscription_data(self) -> Optional[RoleSubscriptionData]:
    return RoleSubscriptionData(self["role_subscription_data"]) if "role_subscription_data" in self else None


  @property
  def stickers(self) -> Optional[list[Sticker]]:
    return [Sticker(data) for data in self["stickers"]] if "stickers" in self else None


  @property
  def sticker_items(self) -> Optional[list[StickerItem]]:
    return [StickerItem(data) for data in self["sticker_items"]] if "sticker_items" in self else None


  @property
  def thread(self) -> Optional[Channel]:
    return Channel(self["thread"]) if "thread" in self else None


  @property
  def timestamp(self) -> datetime:
    return datetime.fromisoformat(self["timestamp"])


  @property
  def tts(self) -> bool:
    return self["tts"]


  @property
  def type(self) -> MessageType:
    return MessageType(self["type"])


  @property
  def user(self) -> User:
    return User(self["user"])


  @property
  def webhook_id(self) -> Optional[Snowflake]:
    return Snowflake(self["webhook_id"]) if "webhook_id" in self else None