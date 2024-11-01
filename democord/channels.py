from .constructor import Constructor
from .embed       import Embed
from .emoji       import Emoji
from .enums       import (
                         ChannelType,
                         ErrorCodes,
                         ForumLayout,
                         ForumSortOrder,
                         InviteTargetType,
                         VideoQualityMode
                         )
from .errors      import (
                         BotMissingPermissions,
                         DiscordException,
                         Forbidden,
                         MissingArguments,
                         NotFound
                         )
from .file        import File
from .flags       import ChannelFlags
from .guild       import Guild
from .invite      import Invite
from .member      import Member
from .message     import Message
from .permissions import PermissionOverwrites
from .regex       import PATTERN
from .reqs        import (
                         DELETE,
                         PATCH,
                         POST,
                         PUT
                         )
from .role        import Role
from .sticker     import Sticker
from .user        import User
from datetime     import datetime
from pathlib      import Path
from re           import findall
from typing       import *

if TYPE_CHECKING:
  from .ws        import DiscordWebSocket


class DMChannel:
  async def close(self, reason : Optional[str] = None) -> Self:
    try:
      response : Dict[str, Any] = self.ws.delete(
        DELETE.channel(self.id),
        reason = reason
      )
      if response.get("code"):
        match ErrorCodes(response.get("code")):
          case ErrorCodes.MissingPermissions:
            raise Constructor.exception(BotMissingPermissions, PermissionFlags.manage_channels, PermissionFlags.manage_threads)
      self : Self = Constructor.channel(response)
      return self
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)

  
  async def edit(self, **attributes) -> Self:
    try:
      data : Dict[str, Any] = {}
      reason : Optional[str] = str(reason.get("reason")) if reason.get("reason") else None
      for attribute in attributes:
        match attribute:
          case "name":
            if not isinstance(attributes[attribute], str):
              raise TypeError("name: must be of type <str>")
            if len(attributes[attribute]) < 1 or len(attributes[attribute]) > 100:
              raise ValueError("name: must be between 1 and 100 characters")
            data[attribute] : str = attributes[attribute]
          case "icon":
            if not isinstance(attributes[attribute], File):
              raise TypeError("name: must be of type <File>")
            if not attributes[attribute].data.startswith("image/"):
              raise ValueError("icon: must be an image file")
            data[attribute] : str = attributes[attribute].data
      response : Dict[str, Any] = self.ws.patch(
        PATCH.channel(self.id),
        data = data,
        reason = reason
      )
      if response.get("code"):
        match ErrorCodes(response.get("code")):
          case ErrorCodes.MissingPermissions:
            raise Constructor.exception(BotMissingPermissions, PermissionFlags.manage_channels)
      self : Self = Constructor.channel(response)
      return self
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def typing(self) -> None:
    try:
      # implement: Typing
      ...
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


class GuildChannel:
  @property
  def guild_id(self) -> int:
    return int(self["id"])

  @property
  def id(sself) -> int:
    return int(self["id"])

  @property
  def name(self) -> str:
    return self["name"]

  @property
  def overwrites(self) -> List[PermissionOverwrites]:
    # implement: PermissionOverwrites
    raise NotImplementedError

  @property
  def permissions(self) -> Optional[str]:
    return self.get("permissions")

  @property
  def position(self) -> int:
    return self["position"]

  @property
  def type(self) -> ChannelType:
    return ChannelType(self["type"])


  async def create_invite(self, **attributes) -> Invite:
    try:
      reason : Optional[str] = str(attributes["reason"]) if attributes.get("reason") else None
      data : Dict[str, Any] = {}
      for attribute in attributes:
        match attribute:
          case "max_age":
            if not isinstance(attributes[attribute], int):
              raise TypeError("max_age: must be of type <int>")
            if attributes[attribute] < 0 or attributes[attribute] > 604_800:
              raise ValueError("max_age: must be between 0 and 604800")
            data[attribute] : int = attributes[attribute]
          case "max_uses":
            if not isinstance(attributes[attribute], int):
              raise TypeError("max_uses: must be of type <int>")
            if attributes[attribute] < 0 or attributes[attribute] > 100:
              raise ValueError("max_uses: must be between 0 and 100")
            data[attribute] : bool = attributes[attribute]
          case "target_application":
            if not isinstance(attributes[attribute], AppInfo):
              raise TypeError("target_application: must be of type <AppInfo>")
            if not attributes.get("target_type"):
              raise Constructor.exception(MissingArguments, "target_type", message = attribute)
            if attributes["target_type"] != InviteTargetType.embedded_application:
              raise Constructor.exception(Forbidden, message = "target_application: can only be specified if target_type is InviteTargetType.embedded_application")
            if "embedded" not in self.ws.app.info:
              raise Constructor.exception(Forbidden, message = f"{attribute}: application is not flagged as EMBEDDED")
            data["target_application_id"] : str = str(attributes[attribute].id)
          case "target_type":
            if not isinstance(attributes[attribute], InviteTargetType):
              raise TypeError("target_type: must be of type <InviteTargetType>")
            if attributes[attribute] == InviteTargetType.stream and not attributes.get("target_user"):
              raise Constructor.exception(MissingArguments, "target_user", message = attribute)
            if attributes[attribute] == InviteTargetType.embedded_application and not attributes.get("target_application"):
              raise Constructor.exception(MissingArguments, "target_application", message = attribute)
            data[attribute] : int = attributes[attribute].value
          case "target_user":
            if not isinstance(attributes[attribute], User):
              raise TypeError("target_user: must be of type <User>")
            if not attributes.get("target_type"):
              raise Constructor.exception(MissingArguments, "target_type", message = attribute)
            if attributes["target_type"] != InviteTargetType.stream:
              raise Constructor.exception(Forbidden, message = "target_user: can only be specified if target_type is InviteTargetType.stream")
            data["target_user_id"] : str = str(attributes[attribute].id)
          case "temporary":
            if not isinstance(attributes[attribute], bool):
              raise TypeError("temporary: must be of type <bool>")
            data[attribute] : bool = attributes[attribute]
          case "unique":
            if not isinstance(attributes[attribute], bool):
              raise TypeError("unique: must be of type <bool>")
            data[attribute] : bool = attributes[attribute]
      response : Dict[str, Any] = self.ws.post(
        POST.channel_invite(self.id),
        data = data,
        reason = reason
      )
      return Constructor.invite(response)
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def create_thread(self, **attributes) -> Thread:
    try:
      reason : Optional[str] = str(attributes["reason"]) if attributes.get("reason") else None
      data : Dict[str, Any] = {}
      if not attributes.get("name"):
        raise Constructor.exception(MissingArguments, "name")
      for attribute in attributes:
        match attribute:
          case "auto_archive_duration":
            if not isinstance(attributes[attribute], int):
              raise TypeError(f"{attribute}: must be of type <int>")
            if attributes[attribute] not in [60, 1440, 4_320, 10_080]:
              raise ValueError(f"{attribute}: can only specify as 60, 1440, 4320, or 10080")
            data[attribute] : int = attributes[attribute]
          case "invitable":
            if not isinstance(attributes[attribute], bool):
              raise TypeError(f"{attribute}: must be of type <bool>")
            data[attribute] : bool = attributes[attribute]
          case "name":
            if not isinstance(attributes[attribute], str):
              raise TypeError(f"{attribute}: must be of type <str>")
            if len(attributes[attribute]) < 0 or len(attributes[attribute]) > 100:
              raise ValueError(f"{attribute}: must be between 1 and 100 characters")
            data[attribute] : str = attributes[attribute]
          case "slowmode":
            if not isinstance(attributes[attribute], (int, None)):
              raise TypeError(f"{attribute}: must be of type <int> or <NoneType>")
            if attributes[attribute] < 0 or attributes[attribute] > 21_600:
              raise ValueError(f"{attribute}: must be between 0 and 21600")
            data[attribute] : Optional[int] = attributes[attribute]
          case "type":
            if not isinstance(attributes[attribute], ChannelType):
              raise TypeError(f"{attribute}: must be of type <ChannelType>")
            if attributes[attribute] not in [ChannelType.public_thread, ChannelType.private_thread]:
              raise ValueError(f"{attribute}: can only be specified as ChannelType.public_thread or ChannelType.private_thread")
            data[attribute] : int = attributes[attribute].value
      response : Dict[str, Any] = self.ws.post(
        POST.start_thread(self.id),
        data = data,
        reason = reason
      )
      return Constructor.channel(response)
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def delete(self, reason : Optional[str] = None) -> Self:
    try:
      response : Dict[str, Any] = self.ws.delete(
        DELETE.channel(self.id),
        reason = reason
      )
      if response.get("code"):
        match ErrorCodes(response.get("code")):
          case ErrorCodes.MissingPermissions:
            raise Constructor.exception(BotMissingPermissions, PermissionFlags.manage_channels, PermissionFlags.manage_threads)
      self : Self = Constructor.channel(response)
      return self
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def edit(self, data : Dict[str, Any], reason : Optional[str] = None) -> Self:
    try:
      response : Dict[str, Any] = self.ws.patch(
        PATCH.channel(self.id),
        data = data,
        reason = reason
      )
      if response.get("code"):
        match ErrorCodes(response.get("code")):
          case ErrorCodes.MissingPermissions:
            raise Constructor.exception(BotMissingPermissions, PermissionFlags.manage_channels)
      self : Union[GuildChannel | DMChannel] = Constructor.channel(response)
      return self
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def invites(self) -> List[Invite]:
    try:
      response : List[Dict[str, Any]] = self.ws.get(
        GET.channel_invites(self.id)
      )
      return [Constructor.invite(invite_data) for invite_data in response]
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def move(
    self,
    position : int,
    *,
    lock_permissions : Optional[bool] = False,
    parent : Optional[Union[CategoryChannel, int]] = None
  ) -> Self:
    try:
      if not isinstance(position, int): raise TypeError("GuildChannel.position must be of type <int>")
      if position < 0: raise ValueError("GuildChannel.position must be a positive integer")
      if not isinstance(lock_permissions, bool): raise TypeError("lock_permissions parameter must be of type <bool>")
      if not isinstance(parent, (CategoryChannel, int)): raise TypeError("GuildChannel.parent must be of type <CategoryChannel> or <int>")
      response : Dict[str, Any] = self.ws.patch(
        PATCH.channel_position(self.guild.id),
        data = {
          "id": self.id,
          "position": position,
          "lock_permissions": lock_permissions,
          "parent_id": int(parent) if parent else (int(self.parent) if self.parent else None)
        }
      )
      if response.get("code"):
        match ErrorCodes(response.get("code")):
          case ErrorCodes.BotMissingPermissions:
            raise Constructor.exception(BotMissingPermissions, PermissionFlags.manage_channels)
      self : Self = Constructor.channel(response)
      return self
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def pins(self) -> List[Message]:
    try:
      response : List[Dict[str, Any]] = self.ws.get(
        GET.pinned_messages(self.id)
      )
      return [Constructor.message(data) for data in response]
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def archived_threads(self, public : bool = True, joined : bool = False) -> List[Thread]:
    try:
      # check permission: read_message_history
      if not public:
        # check permission: manage_threads
        ...
      if joined:
        response : List[Dict[str, Any]] = self.ws.get(
          GET.joined_archived_threads(self.id)
        )
        return [Constructor.thread(data) for data in response]
      response : List[Dict[str, Any]] = self.ws.get(
        GET.archived_threads(self.id, "public" if public else "private")
      )
      return [Constructor.thread(data) for data in response]
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def remove_overwrites(self, target : Union[Member, Role], reason : Optional[str] = None) -> None:
    try:
      response : Dict[None] = self.ws.delete(
        DELETE.channel_permission(target.id),
        reason = reason
      )
      if response.get("code"):
        match ErrorCodes(response.get("code")):
          case ErrorCodes.BotMissingPermissions:
            raise Constructor.exception(BotMissingPermissions, PermissionFlags.manage_roles)
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def set_permissions(self, target : Union[Member, Role], overwrites : PermissionOverwrites, reason : Optional[str] = None) -> None:
    try:
      response : Dict = self.ws.put(
        PUT.channel_permissions(self.id, overwrites.id),
        data = {
          "allow": str(overwrites.allow),
          "deny": str(overwrites.deny),
          "type": 0 if isinstance(target, Role) else 1
        },
        reason = reason
      )
      if response.get("code"):
        match ErrorCodes(response.get("code")):
          case ErrorCodes.BotMissingPermissions:
            raise BotMissingPermissions(PermissionFlags.manage_roles)
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def typing(self) -> None:
    try:
      # implement: Typing
      ...
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


class AnnouncementChannel(GuildChannel):
  @property
  def auto_archive_duration(self) -> int:
    return self.get("default_auto_archive_duration", 60)

  @property
  def guild_id(self) -> int:
    # retrieve Guild object from cache
    return int(self["guild_id"])

  @property
  def id(self) -> int:
    return int(self["id"])

  @property
  def last_message_id(self) -> Optional[int]:
    return int(self["last_message_id"]) if self.get("last_message_id") is not None else None

  @property
  def last_pin_timestamp(self) -> Optional[datetime]:
    return datetime.fromisoformat(self["last_pin_timestamp"]) if self.get("last_pin_timestamp") is not None else None

  @property
  def name(self) -> str:
    return self["name"]

  @property
  def nsfw(self) -> bool:
    return self.get("nsfw", False)

  @property
  def parent_id(self) -> int:
    # retreive CategoryChannel from cache
    return int(self["parent_id"]) if self.get("parent_id") is not None else None

  @property
  def overwrites(self) -> List[PermissionOverwrites]:
    # implement: PermissionOverwrites
    raise NotImplementedError

  @property
  def permissions(self) -> Optional[str]:
    return self.get("permissions")

  @property
  def position(self) -> int:
    return int(self["position"])

  @property
  def topic(self) -> Optional[str]:
    return self.get("topic")

  @property
  def type(self) -> ChannelType:
    return ChannelType.announcement
  

  async def edit(
    self,
    **attributes
  ) -> Self:
    try:
      reason : Optional[str] = str(attributes.get("reason")) if attributes.get("reason") else None
      data : Dict[str, Any] = {}
      for attribute in attributes:
        match attribute:
          case "auto_archive_duration":
            if not isinstance(attributes[attribute], (int, None)):
              raise TypeError("auto_archive_duration: must be of type <int> or <NoneType>")
            if attributes[attribute] not in [60, 1440, 4_320, 10_080]:
              raise ValueError(f"{attribute}: must be a value of either 60, 1440, 4320, or 10080")
            data["default_auto_archive_duration"] : Optional[int] = attributes[attribute]
          case "name":
            if not isinstance(attributes[attribute], str):
              raise TypeError("name: must be of type <str>")
            if len(attributes[attribute]) < 1 or len(attributes[attribute]) > 100:
              raise ValueError("name: must be between 1 and 100 characters")
            data[attribute] : str = attributes[attribute]
          case "nsfw":
            if not isinstance(attributes[attribute], bool):
              raise TypeError("nsfw: must be of type <bool>")
            data[attribute] : bool = attributes[attribute]
          case "overwrites":
            # implement: PermissionOverwrites
            ...
          case "parent":
            if not isinstance(attributes[attribute], (CategoryChannel, int, None)):
              raise TypeError("parent: must be of type <CategoryChannel>, <int>, or <NoneType>")
            data["parent_id"] : Optional[int] = int(attributes[attribute]) if attributes[attribute] else None
          case "position":
            if not isinstance(attributes[attribute], int):
              raise TypeError("position: must be of type <int>")
            if attributes[attribute] < 0:
              raise ValueError("position: must be a positive integer")
            data[attributes] : int = attributes[attribute]
          case "topic":
            if not isinstance(attributes[attribute], (str, None)):
              raise TypeError("topic: must be of type <str> or <NoneType>")
            if len(attributes[attribute]) > 1_024:
              raise ValueError("topic: must be between 0 and 1024 characters")
            data[attributes] : Optional[str] = attributes[attribute]
          case "type":
            if not isinstance(attributes[attribute], ChannelType):
              raise TypeError("type: must be of type <ChannelType>")
            if attributes[attribute] not in [ChannelType.text, ChannelType.announcement]:
              raise ValueError("type: ChannelType.text and ChannelType.announcement are the only supported values")
            data[attribute] : int = attributes[attribute].value
      self : Self = await super().edit(data = data, reason = reason)
      return self
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def follow(self, target_channel : TextChannel, reason : Optional[str] = None) -> None:
    try:
      if not isinstance(target_channel, TextChannel):
        raise TypeError("target_channel: must be of type <TextChannel>")
      response : Dict[str, Any] = self.ws.post(
        POST.follow_announcement_channel(self.id),
        data = {
          "webhook_channel_id": str(target_channel.id)
        },
        reason = reason
      )
      if response.get("code"):
        match ErrorCodes(response.get("code")):
          case ErrorCodes.BotMissingPermissions:
            raise BotMissingPermissions(PermissionFlags.manage_webhooks)
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


class CategoryChannel(GuildChannel):
  @property
  def guild_id(self) -> int:
    # retrieve Guild object from cache
    return int(self["guild_id"])

  @property
  def id(self) -> int:
    return int(self["id"])

  @property
  def name(self) -> str:
    return self["name"]

  @property
  def overwrites(self) -> List[PermissionOverwrites]:
    # implement: PermissionOverwrites
    raise NotImplementedError

  @property
  def permissions(self) -> Optional[str]:
    return self.get("permissions")

  @property
  def position(self) -> int:
    return int(self["position"])

  @property
  def type(self) -> ChannelType:
    return ChannelType.category


  async def create_thread(self) -> None:
    try:
      raise NotImplemented("cannot create thread in a CategoryChannel")
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def edit(
    self,
    **attributes
  ) -> Self:
    try:
      reason : Optional[str] = str(attributes["reason"]) if attributes.get("reason") else None
      data : Dict[str, Any] = {}
      for attribute in attributes:
        match attribute:
          case "name":
            if not isinstance(attributes[attribute], str):
              raise TypeError("name: must be of type <str>")
            if len(attributes[attribute]) < 1 or len(attributes[attribute]) > 100:
              raise ValueError("name: must be between 1 and 100 characters")
            data[attribute] : str = attributes[attribute]
          case "overwrites":
            # implement: PermissionOverwrites
            ...
          case "position":
            if not isinstance(attributes[attribute], int):
              raise TypeError("position: must be of type <int>")
            if attributes[attribute] < 0:
              raise ValueError("position: must be a positive integer")
            data[attributes] : int = attributes[attribute]
      self : Self = await super().edit(data = data, reason = reason)
      return self
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def pins(self) -> None:
    try:
      raise NotImplemented("cannot retrieve pinned messages of a CategoryChannel")
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def archived_threads(self) -> None:
    try:
      raise NotImplemented("cannot retrieve archived threads of a CategoryChannel")
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def typing(self) -> None:
    try:
      raise NotImplemented("cannot trigger typing indicator in a CategoryChannel")
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


class Forum(GuildChannel):

  async def create_thread(self, **attributes) -> Thread:
    try:
      # check permission: send_messages
      ...
      reason : Optional[str] = str(attributes["reason"]) if attributes.get("reason") else None
      data : Dict[str, Any] = {}
      if not any([attributes.get(attribute) for attribute in ["content", "embeds", "name", "stickers", "panel", "files"]]):
        raise Constructor.exception(MissingArguments, "content", "embeds", "files", "name", "panel", "stickers", message = "at least one must be provided")
      for attribute in attributes:
        match attribute:
          case "attachments":
            # implement: uploading attachments
            ...
          case "allowed_mentions":
            allowed_mentions : Dict[str, Union[List[str], bool]] = {
              "parse": [],
              "roles": [mention[2 : -1] for mention in findall(PATTERN.role_mention, attributes["message"]["content"])],
              "users": [mention[2 : -1] for mention in findall(PATTERN.user_mention, attributes["message"]["content"])]
            }
            if allowed_mentions["roles"]: allowed_mentions["parse"].append("roles")
            if allowed_mentions["users"]: allowed_mentions["parse"].append("users")
            if any([mention in attributes["message"]["content"] for mention in ["@everyone", "@here"]]): allowed_mentions["parse"].append("everyone")
            if attributes.get("mention_author"):
              if not isinstance(attributes["mention_author"], bool):
                raise TypeError(f"mention_author: must be of type <bool>")
              allowed_mentions["replied_user"] : bool = attributes.get("mention_author", False)
            else:
              allowed_mentions["replied_user"] : bool = False
            data["message"][attribute] : Dict[str, Union[List[str], bool]] = allowed_mentions
          case "auto_archive_duration":
            if not isinstance(attributes[attribute], int):
              raise TypeError(f"{attribute}: must be of type <int>")
            if attributes[attribute] not in [60, 1440, 4_320, 10_080]:
              raise ValueError(f"{attribute}: must be a value of either 60, 1440, 4320, or 10080")
          case "content":
            if not isinstance(attributes[attribute], str):
              raise TypeError(f"{attribute}: must be of type <str>")
            if len(attributes[attribute]) > 2_000:
              raise Constructor.exception(APILimit, message = f"{attribute}: can only be up to 2000 characters")
            attributes["message"][attribute] : str = attributes[attribute]
          case "embeds":
            if isinstance(attributes[attribute], list):
              if len(attributes[attribute]) > 10:
                raise Constructor.exception(APILimit, message = f"{attribute}: can only upload up to 10 embeds (up to 6000 characters)")
              for embed in attributes[attribute]:
                if not isinstance(embed, Embed):
                  raise TypeError(f"{embed}: must contain <Embed> objects")
              data["message"][attribute] : List[Dict[str, Any]] = [embed.payload for embed in attributes[attribute]]
            elif isinstance(attributes[attribute], Embed):
              data["message"][attribute] : List[Dict[str, Any]] = [attributes[attribute].payload]
            else:
              raise TypeError(f"{attribute}: must be of type <Embed>, or list of <Embed> objects")
          case "files":
            if isinstance(attributes[attribute], list):
              if len(attributes[attribute]) > 10:
                raise Constructor.exception(APILimit, message = f"{attribute}: can only upload up to 10 files per message")
              total_size : int = 0
              for file in attributes[attribute]:
                if not isinstance(file, File):
                  raise TypeError(f"{attribute}: must be a list of <File> objects")
                total_size += Path(file.path).stat().st_size * 8
              if total_size > 26_214_400 * 8:
                raise Constructor.exception(APILimit, message = "can only upload files up to 25 MiB")
              data[attribute] : List[Dict[str, Tuple[str, bytes, str]]] = [{str(index) : (attributes[attribute][index].filename, open(attributes[attribute][index].path, "rb"), attributes[attribute][index].type)} for index in range(len(attributes[attribute]))]
            elif isinstance(attributes[attribute], File):
              data[attribute] : Dict[str, Tuple[str, bytes, str]] = {"0" : (attributes[attribute][index].filename, open(attributes[attribute][index].path, "rb"), attributes[attribute][index].type)}
            else:
              raise TypeError(f"{attribute}: must be of type <File>, or a list of <File> objects")
          case "flags":
            # implement: MessageFlag
            ...
          case "name":
            if not isinstance(attributes[attribute], str):
              raise TypeError(f"{attribute}: must be of type <str>")
            if len(attributes[attribute]) < 1 or len(attributes[attribute]) > 100:
              raise ValueError(f"{attribute}: must be between 1 and 100 characters")
            data[attribute] : str = attributes[attribute]
          case "panel":
            if not isinstance(attributes[attribute], Panel):
              raise TypeError(f"{attribute}: must be of type <Panel>")
            data[attribute] : List[Dict[str, Any]] = [component for component in attributes[attribute].children]
          case "slowmode":
            if not isinstance(attributes[attribute], (int, None)):
              raise TypeError(f"{attribute}: must be of type <int> or <NoneType>")
            if attributes[attribute] < 0 or attributes[attribute] > 21_600:
              raise ValueError(f"{attribute}: must be between 0 and 21600")
            data[attribute] : Optional[int] = attributes[attribute]
          case "stickers":
            if isinstance(attributes[attribute], list):
              if len(attributes[attribute]) > 3:
                raise Constructor.exception(APILimit, message = f"{attribute}: can only upload up to 3 stickers")
              for sticker in attributes[attribute]:
                if not isinstance(sticker, Sticker):
                  raise TypeError(f"{sticker}: must contain <Sticker> objects")
              data[attribute] : List[str] = [str(sticker.id) for sticker in attributes[attribute]]
            elif isinstance(attributes[attribute], Sticker):
              data[attribute] : List[str] = [str(attributes[attribute].id)]
            else:
              raise TypeError(f"{attribute}: must be of type <Sticker>, or a list of <Sticker> objects")
          case "tags":
            if isinstance(attributes[attribute], list):
              for tag in attributes[attribute]:
                if not isinstance(tag, ForumTag):
                  raise TypeError(f"{attribute}: must contain <ForumTag> objects")
                if tag not in self.tags:
                  raise Constructor.exception(NotFound, f"ForumTag with ID {tag.id}")
            else:
              raise TypeError(f"{attribute}: must be of type <list> containing <ForumTag> objects")
            data[attribute] : List[str] = [str(tag.id) for tag in attributes[attribute]]
      response : Dict[str, Any] = self.ws.post(
        POST.start_thread_in_forum_or_media(self.id),
        data = data,
        reason = reason
      )
      return Constructor.channel(response)
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def edit(
    self,
    **attributes
  ) -> Self:
    try:
      reason : Optional[str] = str(attributes["reason"]) if attributes.get("reason") else None
      data : Dict[str, Any] = {}
      for attribute in attributes:
        match attribute:
          case "auto_archive_duration":
            if not isinstance(attributes[attribute], (int, None)):
              raise TypeError("auto_archive_duration: must be of type <int> or <NoneType>")
            data["default_auto_archive_duration"] : Optional[int] = attributes[attribute]
          case "default_reaction_emoji":
            if not isinstance(attributes[attribute], (Emoji, str, None)):
              raise TypeError("default_reaction_emoji: must be of type <Emoji>, <str>, or <NoneType>")
            data[attribute] : Optional[Union[int, str]] = (attributes[attribute].id if isinstance(attributes[attribute], Emoji) else attributes[attribute]) if attributes[attribute] else None
          case "flags":
            if not isinstance(attributes[attribute], (ChannelFlag, None)):
              raise TypeError("flags: must be of type <ChannelFlag> or <NoneType>")
            if attributes[attribute] and attributes[attribute] != ChannelFlag.require_tag:
              raise ValueError("flags: only ChannelFlag.require_tag is supported for Forum")
            flags : int = 0
            for flag in self.flags:
              if flag != attributes[attribute]:
                flags |= flag.value
            data[attribute] : int = flags
          case "layout":
            if not isinstance(attributes[attribute], (ForumLayout, None)):
              raise TypeError("layout: must be of type <ForumLayout> or <NoneType>")
            data["default_forum_layout"] : int = attributes[attribute].value if attributes[attribute] else 0
          case "name":
            if not isinstance(attributes[attribute], str):
              raise TypeError("name: must be of type <str>")
            if len(attributes[attribute]) < 1 or len(attributes[attribute]) > 100:
              raise ValueError("name: must be between 1 and 100 characters")
            data[attribute] : str = attributes[attribute]
          case "nsfw":
            if not isinstance(attributes[attribute], bool):
              raise TypeError("nsfw: must be of type <bool>")
            data[attribute] : bool = attributes[attribute]
          case "overwrites":
            # implement: PermissionOverwrites
            ...
          case "parent":
            if not isinstance(attributes[attribute], (CategoryChannel, int, None)):
              raise TypeError("parent: must be of type <CategoryChannel>, <int>, or <NoneType>")
            data["parent_id"] : Optional[int] = int(attributes[attribute]) if attributes[attribute] else None
          case "slowmode":
            if not isinstance(attributes[attribute], (int, None)):
              raise TypeError("slowmode: must be of type <int> or <NoneType>")
            if attributes[attribute] < 0 or attributes[attribute] > 21_600:
              raise ValueError("slowmode: must be between 0 and 21600 seconds")
            data["rate_limit_per_user"] : Optional[str] = attributes[attribute]
          case "sort_order":
            if not isinstance(attributes[attribute], (ForumSortOrder, None)):
              raise TypeError("sort_order: must be of type <ForumSortOrder> or <NoneType>")
            data["default_sort_order"] : Optional[int] = attributes[attribute].value if attributes[attribute] else None
          case "tags":
            if isinstance(attributes[attribute], list):
              for tag in attributes[attribute]:
                if not isinstance(tag, ForumTag):
                  raise ValueError("tags: items must be of type <ForumTag>")
            else:
              raise TypeError("tags: must be of type <list> containing <ForumTag> objects")
            if len(attributes[attribute]) > 20:
              raise ValueError("tags: can only create up to 20 Forum tags")
            data["available_tags"] : List[Dict[str, Any]] = [tag.payload for tag in attributes[attribute]]
          case "thread_slowmode":
            if not isinstance(attributes[attribute], int):
              raise TypeError("thread_slowmode: must be of type <int>")
            if attributes[attribute] < 0 or attributes[attribute] > 21_600:
              raise ValueError("thread_slowmode: must be between 0 and 21600")
            data["default_thread_rate_limit_per_user"] : int = attributes[attribute]
          case "topic":
            if not isinstance(attributes[attribute], (str, None)):
              raise TypeError("topic: must be of type <str> or <NoneType>")
            if len(attributes[attribute]) > 4_096:
              raise ValueError("topic: must be between 0 and 4096 characters")
            data[attributes] : Optional[str] = attributes[attribute]
      self : Self = await super().edit(data = data, reason = reason)
      return self
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


class MediaChannel(GuildChannel):

  async def create_thread(self, **attributes) -> Thread:
    try:
      # check permission: send_messages
      ...
      reason : Optional[str] = str(attributes["reason"]) if attributes.get("reason") else None
      data : Dict[str, Any] = {}
      if not any([attributes.get(attribute) for attribute in ["content", "embeds", "name", "stickers", "panel", "files"]]):
        raise Constructor.exception(MissingArguments, "content", "embeds", "files", "name", "panel", "stickers", message = "at least one must be provided")
      for attribute in attributes:
        match attribute:
          case "attachments":
            # implement: uploading attachments
            ...
          case "allowed_mentions":
            allowed_mentions : Dict[str, Union[List[str], bool]] = {
              "parse": [],
              "roles": [mention[2 : -1] for mention in findall(PATTERN.role_mention, attributes["message"]["content"])],
              "users": [mention[2 : -1] for mention in findall(PATTERN.user_mention, attributes["message"]["content"])]
            }
            if allowed_mentions["roles"]: allowed_mentions["parse"].append("roles")
            if allowed_mentions["users"]: allowed_mentions["parse"].append("users")
            if any([mention in attributes["message"]["content"] for mention in ["@everyone", "@here"]]): allowed_mentions["parse"].append("everyone")
            if attributes.get("mention_author"):
              if not isinstance(attributes["mention_author"], bool):
                raise TypeError(f"mention_author: must be of type <bool>")
              allowed_mentions["replied_user"] : bool = attributes.get("mention_author", False)
            else:
              allowed_mentions["replied_user"] : bool = False
            data["message"][attribute] : Dict[str, Union[List[str], bool]] = allowed_mentions
          case "auto_archive_duration":
            if not isinstance(attributes[attribute], int):
              raise TypeError(f"{attribute}: must be of type <int>")
            if attributes[attribute] not in [60, 1440, 4_320, 10_080]:
              raise ValueError(f"{attribute}: must be a value of either 60, 1440, 4320, or 10080")
          case "content":
            if not isinstance(attributes[attribute], str):
              raise TypeError(f"{attribute}: must be of type <str>")
            if len(attributes[attribute]) > 2_000:
              raise Constructor.exception(APILimit, message = f"{attribute}: can only be up to 2000 characters")
            attributes["message"][attribute] : str = attributes[attribute]
          case "embeds":
            if isinstance(attributes[attribute], list):
              if len(attributes[attribute]) > 10:
                raise Constructor.exception(APILimit, message = f"{attribute}: can only upload up to 10 embeds (up to 6000 characters)")
              for embed in attributes[attribute]:
                if not isinstance(embed, Embed):
                  raise TypeError(f"{embed}: must contain <Embed> objects")
              data["message"][attribute] : List[Dict[str, Any]] = [embed.payload for embed in attributes[attribute]]
            elif isinstance(attributes[attribute], Embed):
              data["message"][attribute] : List[Dict[str, Any]] = [attributes[attribute].payload]
            else:
              raise TypeError(f"{attribute}: must be of type <Embed>, or list of <Embed> objects")
          case "files":
            if isinstance(attributes[attribute], list):
              if len(attributes[attribute]) > 10:
                raise Constructor.exception(APILimit, message = f"{attribute}: can only upload up to 10 files per message")
              total_size : int = 0
              for file in attributes[attribute]:
                if not isinstance(file, File):
                  raise TypeError(f"{attribute}: must be a list of <File> objects")
                total_size += Path(file.path).stat().st_size * 8
              if total_size > 26_214_400 * 8:
                raise Constructor.exception(APILimit, message = "can only upload files up to 25 MiB")
              data[attribute] : List[Dict[str, Tuple[str, bytes, str]]] = [{str(index) : (attributes[attribute][index].filename, open(attributes[attribute][index].path, "rb"), attributes[attribute][index].type)} for index in range(len(attributes[attribute]))]
            elif isinstance(attributes[attribute], File):
              data[attribute] : Dict[str, Tuple[str, bytes, str]] = {"0" : (attributes[attribute][index].filename, open(attributes[attribute][index].path, "rb"), attributes[attribute][index].type)}
            else:
              raise TypeError(f"{attribute}: must be of type <File>, or a list of <File> objects")
          case "flags":
            # implement: MessageFlag
            ...
          case "name":
            if not isinstance(attributes[attribute], str):
              raise TypeError(f"{attribute}: must be of type <str>")
            if len(attributes[attribute]) < 1 or len(attributes[attribute]) > 100:
              raise ValueError(f"{attribute}: must be between 1 and 100 characters")
            data[attribute] : str = attributes[attribute]
          case "panel":
            if not isinstance(attributes[attribute], Panel):
              raise TypeError(f"{attribute}: must be of type <Panel>")
            data[attribute] : List[Dict[str, Any]] = [component for component in attributes[attribute].children]
          case "slowmode":
            if not isinstance(attributes[attribute], (int, None)):
              raise TypeError(f"{attribute}: must be of type <int> or <NoneType>")
            if attributes[attribute] < 0 or attributes[attribute] > 21_600:
              raise ValueError(f"{attribute}: must be between 0 and 21600")
            data[attribute] : Optional[int] = attributes[attribute]
          case "stickers":
            if isinstance(attributes[attribute], list):
              if len(attributes[attribute]) > 3:
                raise Constructor.exception(APILimit, message = f"{attribute}: can only upload up to 3 stickers")
              for sticker in attributes[attribute]:
                if not isinstance(sticker, Sticker):
                  raise TypeError(f"{sticker}: must contain <Sticker> objects")
              data[attribute] : List[str] = [str(sticker.id) for sticker in attributes[attribute]]
            elif isinstance(attributes[attribute], Sticker):
              data[attribute] : List[str] = [str(attributes[attribute].id)]
            else:
              raise TypeError(f"{attribute}: must be of type <Sticker>, or a list of <Sticker> objects")
          case "tags":
            if isinstance(attributes[attribute], list):
              for tag in attributes[attribute]:
                if not isinstance(tag, ForumTag):
                  raise TypeError(f"{attribute}: must contain <ForumTag> objects")
                if tag not in self.tags:
                  raise Constructor.exception(NotFound, f"ForumTag with ID {tag.id}")
            else:
              raise TypeError(f"{attribute}: must be of type <list> containing <ForumTag> objects")
            data[attribute] : List[str] = [str(tag.id) for tag in attributes[attribute]]
      response : Dict[str, Any] = self.ws.post(
        POST.start_thread_in_forum_or_media(self.id),
        data = data,
        reason = reason
      )
      return Constructor.channel(response)
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def edit(
    self,
    **attributes
  ) -> Self:
    try:
      reason : Optional[str] = str(attributes["reason"]) if attributes.get("reason") else None
      data : Dict[str, Any] = {}
      for attribute in attributes:
        match attribute:
          case "auto_archive_duration":
            if not isinstance(attributes[attribute], (int, None)):
              raise TypeError("auto_archive_duration: must be of type <int> or <NoneType>")
            data["default_auto_archive_duration"] : Optional[int] = attributes[attribute]
          case "default_reaction_emoji":
            if not isinstance(attributes[attribute], (Emoji, str, None)):
              raise TypeError("default_reaction_emoji: must be of type <Emoji>, <str>, or <NoneType>")
            data[attribute] : Optional[Union[int, str]] = (attributes[attribute].id if isinstance(attributes[attribute], Emoji) else attributes[attribute]) if attributes[attribute] else None
          case "flags":
            if not isinstance(attributes[attribute], (ChannelFlag, None)):
              raise TypeError("flags: must be of type <ChannelFlag> or <NoneType>")
            if attributes[attribute] and attributes[attribute] not in [ChannelFlag.require_tag, ChannelFlag.hide_media_download_options]:
              raise ValueError("flags: only ChannelFlag.require_tag and ChannelFlag.hide_media_download_options are supported for Forum")
            flags : int = 0
            for flag in self.flags:
              if flag != attributes[attribute]:
                flags |= flag.value
            data[attribute] : int = flags
          case "name":
            if not isinstance(attributes[attribute], str):
              raise TypeError("name: must be of type <str>")
            if len(attributes[attribute]) < 1 or len(attributes[attribute]) > 100:
              raise ValueError("name: must be between 1 and 100 characters")
            data[attribute] : str = attributes[attribute]
          case "nsfw":
            if not isinstance(attributes[attribute], bool):
              raise TypeError("nsfw: must be of type <bool>")
            data[attribute] : bool = attributes[attribute]
          case "overwrites":
            # implement: PermissionOverwrites
            ...
          case "parent":
            if not isinstance(attributes[attribute], (CategoryChannel, int, None)):
              raise TypeError("parent: must be of type <CategoryChannel>, <int>, or <NoneType>")
            data["parent_id"] : Optional[int] = int(attributes[attribute]) if attributes[attribute] else None
          case "slowmode":
            if not isinstance(attributes[attribute], (int, None)):
              raise TypeError("slowmode: must be of type <int> or <NoneType>")
            if attributes[attribute] < 0 or attributes[attribute] > 21_600:
              raise ValueError("slowmode: must be between 0 and 21600 seconds")
            data["rate_limit_per_user"] : Optional[str] = attributes[attribute]
          case "sort_order":
            if not isinstance(attributes[attribute], (ForumSortOrder, None)):
              raise TypeError("sort_order: must be of type <ForumSortOrder> or <NoneType>")
            data["default_sort_order"] : Optional[int] = attributes[attribute].value if attributes[attribute] else None
          case "tags":
            if isinstance(attributes[attribute], list):
              for tag in attributes[attribute]:
                if not isinstance(tag, ForumTag):
                  raise ValueError("tags: items must be of type <ForumTag>")
            else:
              raise TypeError("tags: must be of type <list> containing <ForumTag> objects")
            if len(attributes[attribute]) > 20:
              raise ValueError("tags: can only create up to 20 Media tags")
            data[attribute] : List[Dict[str, Any]] = [tag.payload for tag in attributes[attribute]]
          case "thread_slowmode":
            if not isinstance(attributes[attribute], int):
              raise TypeError("thread_slowmode: must be of type <int>")
            if attributes[attribute] < 0 or attributes[attribute] > 21_600:
              raise ValueError("thread_slowmode: must be between 0 and 21600")
            data["default_thread_rate_limit_per_user"] : int = attributes[attribute]
          case "topic":
            if not isinstance(attributes[attribute], (str, None)):
              raise TypeError("topic: must be of type <str> or <NoneType>")
            if len(attributes[attribute]) > 4_096:
              raise ValueError("topic: must be between 0 and 4096 characters")
            data[attributes] : Optional[str] = attributes[attribute]
      self : Self = await super().edit(data = data, reason = reason)
      return self
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


class StageChannel(GuildChannel):

  async def edit(
    self,
    **attributes
  ) -> Self:
    try:
      reason : Optional[str] = str(attributes["reason"]) if attributes.get("reason") else None
      data : Dict[str, Any] = {}
      for attribute in attributes:
        match attribute:
          case "bitrate":
            if not isinstance(attributes[attribute], (int, None)):
              raise TypeError("bitrate: must be of type <int> or <NoneType>")
            if attributes[attribute] < 8_000:
              raise ValueError("bitrate: minimum value is 8000")
            data[attribute] : int = attributes[attribute]
          case "nsfw":
            if not isinstance(attributes[attribute], bool):
              raise TypeError("nsfw: must be of type <bool>")
            data[attribute] : bool = attributes[attribute]
          case "overwrites":
            # implement: PermissionOverwrites
            ...
          case "parent":
            if not isinstance(attributes[attribute], (CategoryChannel, int, None)):
              raise TypeError("parent: must be of type <CategoryChannel>, <int>, or <NoneType>")
            data["parent_id"] : Optional[int] = int(attributes[attribute]) if attributes[attribute] else None
          case "rtc_region":
            # implement: VoiceRegion
            ...
          case "slowmode":
            if not isinstance(attributes[attribute], (int, None)):
              raise TypeError("slowmode: must be of type <int> or <NoneType>")
            if attributes[attribute] < 0 or attributes[attribute] > 21_600:
              raise ValueError("slowmode: must be between 0 and 21600 seconds")
            data["rate_limit_per_user"] : Optional[str] = attributes[attribute]
          case "user_limit":
            if not isinstance(attributes[attribute], (int, None)):
              raise TypeError("user_limit: must be of type <int> or <NoneType>")
            if attributes[attribute] and (attributes[attribute] < 0 or attributes[attribute] > 99):
              raise ValueError("user_limit: must be between 0 and 99 users")
            data[attribute] : Optional[int] = attributes[attribute]
          case "video_quality_mode":
            if not isinstance(attributes[attribute], (VideoQualityMode, None)):
              raise TypeError("video_quality_mode: must be of type <VideoQualityMode> or <NoneType>")
            data[attribute] : Optional[int] = attributes[attribute].value if attributes[attribute] else None
      self : Self = await super().edit(data = data, reason = reason)
      return self
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


class TextChannel(GuildChannel):

  async def edit(
    self,
    **attributes
  ) -> Self:
    try:
      reason : Optional[str] = str(attributes.get("reason")) if attributes.get("reason") else None
      data : Dict[str, Any] = {}
      for attribute in attributes:
        match attribute:
          case "auto_archive_duration":
            if not isinstance(attributes[attribute], (int, None)):
              raise TypeError("auto_archive_duration: must be of type <int> or <NoneType>")
            data["default_auto_archive_duration"] : Optional[int] = attributes[attribute]
          case "name":
            if not isinstance(attributes[attribute], str):
              raise TypeError("name: must be of type <str>")
            if len(attributes[attribute]) < 1 or len(attributes[attribute]) > 100:
              raise ValueError("name: must be between 1 and 100 characters")
            data[attribute] : str = attributes[attribute]
          case "nsfw":
            if not isinstance(attributes[attribute], bool):
              raise TypeError("nsfw: must be of type <bool>")
            data[attribute] : bool = attributes[attribute]
          case "overwrites":
            # implement: PermissionOverwrites
            ...
          case "parent":
            if not isinstance(attributes[attribute], (CategoryChannel, int, None)):
              raise TypeError("parent: must be of type <CategoryChannel>, <int>, or <NoneType>")
            data["parent_id"] : Optional[int] = int(attributes[attribute]) if attributes[attribute] else None
          case "position":
            if not isinstance(attributes[attribute], int):
              raise TypeError("position: must be of type <int>")
            if attributes[attribute] < 0:
              raise ValueError("position: must be a positive integer")
            data[attributes] : int = attributes[attribute]
          case "slowmode":
            if not isinstance(attributes[attribute], (int, None)):
              raise TypeError("slowmode: must be of type <int> or <NoneType>")
            if attributes[attribute] < 0 or attributes[attribute] > 21_600:
              raise ValueError("slowmode: must be between 0 and 21600 seconds")
            data["rate_limit_per_user"] : Optional[str] = attributes[attribute]
          case "thread_slowmode":
            if not isinstance(attributes[attribute], int):
              raise TypeError("thread_slowmode: must be of type <int>")
            if attributes[attribute] < 0 or attributes[attribute] > 21_600:
              raise ValueError("thread_slowmode: must be between 0 and 21600")
            data["default_thread_rate_limit_per_user"] : int = attributes[attribute]
          case "topic":
            if not isinstance(attributes[attribute], (str, None)):
              raise TypeError("topic: must be of type <str> or <NoneType>")
            if len(attributes[attribute]) > 1_024:
              raise ValueError("topic: must be between 0 and 1024 characters")
            data[attributes] : Optional[str] = attributes[attribute]
          case "type":
            if not isinstance(attributes[attribute], ChannelType):
              raise TypeError("type: must be of type <ChannelType>")
            if attributes[attribute] not in [ChannelType.text, ChannelType.announcement]:
              raise ValueError("type: ChannelType.text and ChannelType.announcement are the only supported values")
            data[attribute] : int = attributes[attribute].value
      self : Self = await super().edit(data = data, reason = reason)
      return self
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


class Thread(GuildChannel):
  async def add_member(self, member : Member) -> None:
    try:
      if not isinstance(member, Member):
        raise TypeError("member: must be of type <Member>")
      if self.archived:
        raise Constructor.exception(DiscordException, message = "cannot add a member to an archived thread")
      response : Dict[None] = self.ws.put(
        PUT.add_thread_member(self.id, member.id)
      )
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def create_thread(self) -> None:
    try:
      raise NotImplemented("cannot create thread in a Thread")
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def edit(
    self,
    **attributes
  ) -> Self:
    try:
      reason : Optional[str] = str(attributes["reason"]) if attributes.get("reason") else None
      data : Dict[str, Any] = {}
      for attribute in attributes:
        match attribute:
          case "applied_tags":
            if isinstance(attributes[attribute], list):
              for tag in attributes[attribute]:
                if not isinstance(tag, ForumTag):
                  raise TypeError("applied_tags: items must be of type <ForumTag>")
            else:
              raise TypeError("applied_tags: must be of type <list> containing <ForumTag> objects")
            if len(attributes[attribute]) > 5:
              raise ValueError("applied_tags: can only apply up to 5 Forum tags")
            data[attribute] : List[int] = [tag.id for tag in attributes[attribute]]
          case "archived":
            if not isinstance(attributes[attribute], bool):
              raise TypeError("archived: must be of type <bool>")
            data[attribute] : bool = attributes[attribute]
          case "auto_archive_duration":
            if not isinstance(attributes[attribute], int):
              raise TypeError("auto_archive_duration: must be of type <int>")
            if attributes[attribute] not in [60, 1440, 4_320, 10_080]:
              raise ValueError("auto_archive_duration: value can only be either 60, 1440, 4320, or 10080")
            data[attribute] : int = attributes[attribute]
          case "flags":
            if not isinstance(attributes[attribute], (ChannelFlag, None)):
              raise TypeError("flags: must be of type <ChannelFlag> or <NoneType>")
            if attributes[attribute] and attributes[attribute] != ChannelFlag.pinned:
              raise ValueError("flags: only ChannelFlag.require_tag is supported for Forum")
            flags : int = 0
            for flag in self.flags:
              if flag != attributes[attribute]:
                flags |= flag.value
            data[attribute] : int = flags
          case "invitable":
            if not isinstance(attributes[attribute], bool):
              raise TypeError("invitable: must be of type <bool>")
            data[attribute] : bool = attributes[attribute]
          case "locked":
            if not isinstance(attributes[attribute], bool):
              raise TypeError("locked: must be of type <bool>")
            data[attribute] : bool = attributes[attribute]
          case "name":
            if not isinstance(attributes[attribute], str):
              raise TypeError("name: must be of type <str>")
            if len(attributes[attribute]) < 1 or len(attributes[attribute]) > 100:
              raise ValueError("name: must be between 1 and 100 characters")
            data[attribute] : str = attributes[attribute]
          case "slowmode":
            if not isinstance(attributes[attribute], (int, None)):
              raise TypeError("slowmode: must be of type <int> or <NoneType>")
            if attributes[attribute] < 0 or attributes[attribute] > 21_600:
              raise ValueError("slowmode: must be between 0 and 21600 seconds")
            data["rate_limit_per_user"] : Optional[str] = attributes[attribute]
      self : Self = await super().edit(data = data, reason = reason)
      return self
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def fetch_member(self, member_id : int) -> ThreadMember:
    try:
      if not isinstance(member_id, int):
        raise TypeError("member_id: must be of type <int>")
      response : Dict[str, Any] = self.ws.get(
        GET.thread_member(self.id, member_id)
      )
      # handle error code: 404
      return Constructor.thread_member(response)
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def fetch_members(self) -> List[ThreadMember]:
    try:
      response : List[Dict[str, Any]] = self.ws.get(
        GET.thread_members(self.id)
      )
      return [Constructor.thread_member(data) for data in response]
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def join(self) -> None:
    try:
      if self.archived:
        raise Constructor.exception(DiscordException, message = "cannot join an archived thread")
      response : Dict[None] = self.ws.put(
        PUT.join_thread(self.id)
      )
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def remove_member(self, member : Member) -> None:
    try:
      if not isinstance(member, Member):
        raise TypeError("member: must be of type <Member>")
      # check permission: manage_threads
      if self.type == ChannelType.private_thread and self.owner != self.guild.me:
        raise Constructor.exception(DiscordException, message = "cannot delete a thread you do not own")
      response : Dict[None] = self.ws.delete(
        DELETE.remove_thread_member(self.id, member.id)
      )
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def leave(self) -> None:
    try:
      if self.archived:
        raise Constructor.exception(DiscordException, message = "cannot leave an archived thread")
      response : Dict[None] = self.ws.delete(
        DELETE.leave_thread(self.id)
      )
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


class VoiceChannel(GuildChannel):

  async def edit(
    self,
    **attributes
  ) -> Self:
    try:
      reason : Optional[str] = str(attributes["reason"]) if attributes.get("reason") else None
      data : Dict[str, Any] = {}
      for attribute in attributes:
        match attribute:
          case "bitrate":
            if not isinstance(attributes[attribute], (int, None)):
              raise TypeError("bitrate: must be of type <int> or <NoneType>")
            if attributes[attribute] < 8_000:
              raise ValueError("bitrate: minimum value is 8000")
            data[attribute] : int = attributes[attribute]
          case "name":
            if not isinstance(attributes[attribute], str):
              raise TypeError("name: must be of type <str>")
            if len(attributes[attribute]) < 1 or len(attributes[attribute]) > 100:
              raise ValueError("name: must be between 1 and 100 characters")
            data[attribute] : str = attributes[attribute]
          case "nsfw":
            if not isinstance(attributes[attribute], bool):
              raise TypeError("nsfw: must be of type <bool>")
            data[attribute] : bool = attributes[attribute]
          case "overwrites":
            # implement: PermissionOverwrites
            ...
          case "parent":
            if not isinstance(attributes[attribute], (CategoryChannel, int, None)):
              raise TypeError("parent: must be of type <CategoryChannel>, <int>, or <NoneType>")
            data["parent_id"] : Optional[int] = int(attributes[attribute]) if attributes[attribute] else None
          case "position":
            if not isinstance(attributes[attribute], int):
              raise TypeError("position: must be of type <int>")
            if attributes[attribute] < 0:
              raise ValueError("position: must be a positive integer")
            data[attributes] : int = attributes[attribute]
          case "rtc_region":
            # implement: VoiceRegion
            ...
          case "slowmode":
            if not isinstance(attributes[attribute], (int, None)):
              raise TypeError("slowmode: must be of type <int> or <NoneType>")
            if attributes[attribute] < 0 or attributes[attribute] > 21_600:
              raise ValueError("slowmode: must be between 0 and 21600 seconds")
            data["rate_limit_per_user"] : Optional[str] = attributes[attribute]
          case "user_limit":
            if not isinstance(attributes[attribute], (int, None)):
              raise TypeError("user_limit: must be of type <int> or <NoneType>")
            if attributes[attribute] and (attributes[attribute] < 0 or attributes[attribute] > 99):
              raise ValueError("user_limit: must be between 0 and 99 users")
            data[attribute] : Optional[int] = attributes[attribute]
          case "video_quality_mode":
            if not isinstance(attributes[attribute], (VideoQualityMode, None)):
              raise TypeError("video_quality_mode: must be of type <VideoQualityMode> or <NoneType>")
            data[attribute] : Optional[int] = attributes[attribute].value if attributes[attribute] else None
      self : Self = await super().edit(data = data, reason = reason)
      return self
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)