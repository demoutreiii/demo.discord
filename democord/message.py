from .channels import (
                      DMChannel,
                      GuildChannel
                      )
from .errors   import APILimit
from .reqs     import (
                      DELETE,
                      PUT
                      )
from .user     import User
from datetime  import datetime
from typing    import *


class Message:
  @property
  def activity(self) -> MessageActivity:
    # implement: MessageActivity | Activity
    raise NotImplementedError


  @property
  def application(self) -> Optional[AppInfo]:
    if self["application"] is None: return None
    from .constructor import Constructor
    return Constructor.info(self["application"])


  @property
  def application_id(self) -> Optional[int]:
    if self["application_id"] is None: return None
    return int(self["application_id"])


  @property
  def attachments(self) -> List[Attachment]:
    # implement: Attachment
    raise NotImplementedError


  @property
  def author(self) -> User:
    # implement: User
    # retrieve user object from cache
    raise NotImplementedError


  @property
  def call(self) -> Optional[MessageCall]:
    # implement: MessageCallObject
    raise NotImplementedError


  @property
  def channel(self) -> Union[DMChannel, GuildChannel]:
    # retrieve channel object from cache
    raise NotImplementedError

  
  @property
  def channel_mentions(self) -> List[Union[DMChannel, GuildChannel]]:
    # implement: ChannelMention
    raise NotImplementedError


  @property
  def content(self) -> str:
    return self["content"]


  @property
  def edited(self) -> Optional[datetime]:
    if self["edited_timestamp"] is None: return None
    return datetime.fromisoformat(self["edited_timestamp"])


  @property
  def embeds(self) -> List[Embed]:
    from .constructor import Constructor
    return [
      Constructor.embed(embed_data)
      for embed_data in self["embeds"]
    ]


  @property
  def flags(self) -> List[str]:
    return [
      flag.name
      for flag in MessageFlags
      if (self["flags"] & flag.value) == flag.value
    ]


  @property
  def id(self) -> int:
    return int(self["id"])


  @property
  def interaction_metadata(self) -> Optional[InteractionMetadata]:
    # implement: InteractionMetadata
    raise NotImplementedError


  @property
  def is_tts(self) -> bool:
    return self["tts"]


  @property
  def mentions(self) -> List[User]:
    from .constructor import Constructor
    return [
      Constructor.user(user_data)
      for user_data in self["mentions"]
    ]


  @property
  def mentions_everyone(self) -> bool:
    return self["mention_everyone"]


  @property
  def nonce(self) -> Optional[Union[int, str]]:
    return self["nonce"]


  @property
  def panel(self) -> Panel:
    # implement: Panel
    raise NotImplementedError


  @property
  def pinned(self) -> bool:
    return self["pinned"]


  @property
  def poll(self) -> Optional[Poll]:
    # implement: Poll
    raise NotImplementedError


  @property
  def position(self) -> Optional[int]:
    return self["position"]


  @property
  def reactions(self) -> List[Reaction]:
    # implement: ReactionObject
    raise NotImplementedError


  @property
  def reference(self) -> Optional[MessageReference]:
    # implement: MessageReference
    raise NotImplementedError

  
  @property
  def referenced(self) -> Optional[Message]:
    # implement: MessageReferenced
    raise NotImplementedError


  @property
  def resolved(self) -> Optional[ResolvedData]:
    # implement: ResolvedData
    raise NotImplementedError


  @property
  def role_mentions(self) -> List[Role]:
    # implement: Role
    raise NotImplementedError


  @property
  def role_subscription(self) -> Optional[RoleSubscription]:
    # implement: RoleSubscription
    raise NotImplementedError


  @property
  def snapshots(self) -> List[Snapshot]:
    # implement: Snapshot
    raise NotImplementedError


  @property
  def stickers(self) -> List[Sticker]:
    # implement: Sticker
    raise NotImplementedError


  @property
  def thread(self) -> Optional[Thread]:
    if self["thread"] is None: return None
    from .constructor import Constructor
    return Cosntructor.channel(self["thread"])


  @property
  def timestamp(self) -> datetime:
    return datetime.fromisoformat(self["timestamp"])


  @property
  def type(self) -> MessageType:
    return MessageType(self["type"])


  @property
  def webhook_id(self) -> Optional[int]:
    if self["webhook_id"] is None: return None
    return int(self["webhook_id"])


  async def create_thread(self, **attributes) -> Thread:
    # implement: await Message.create_thread(...)
    # pending for Message minor update
    ...


  async def pin(self, reason : Optional[str] = None) -> None:
    try:
      # check permission: manage_messages
      if len(await self.channel.pins()) == 50:
        raise Constructor.exception(APILimit, message = "can only pin up to 50 messages")
      response : Dict[None] = self.ws.put(
        PUT.pin_message(self.channel.id, self.id),
        reason = reason
      )
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def unpin(self, reason : Optional[str] = None) -> None:
    try:
      # check permission: manage_messages
      response : Dict[None] = self.ws.delete(
        DELETE.unpin_message(self.channel.id, self.id),
        reason = reason
      )
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)