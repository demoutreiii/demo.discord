from .appinfo     import (
                         AppInfo,
                         AppInfoFlags
                         )
from .asset       import Asset
from .channels    import (
                         AnnouncementChannel,
                         CategoryChannel,
                         DMChannel,
                         Forum,
                         GuildChannel,
                         MediaChannel,
                         StageChannel,
                         TextChannel,
                         Thread,
                         VoiceChannel
                         )
from .emoji       import Emoji
from .enums       import (
                         ChannelType,
                         DefaultMessageNotification,
                         ExplicitContentFilter,
                         ForumLayout,
                         ForumSortOrder,
                         InviteTargetType,
                         InviteType,
                         MFALevel,
                         NSFWLevel,
                         PermissionFlags,
                         PremiumTier,
                         VerificationLevel
                         )
from .errors      import (
                         APILimit,
                         BotMissingPermissions,
                         DiscordException,
                         Forbidden,
                         MissingArguments,
                         MissingPermissions,
                         NotFound
                         )
from .file        import File
from .flags       import ChannelFlags
from .guild       import (
                         CallableGuildChannels,
                         CallableSystemChannelFlags,
                         Guild,
                         GuildPreview
                         )
from .invite      import (
                         Invite,
                         InviteTarget
                         )
from .member      import Member
from .message     import Message
from .metaclasses import (
                         BasePayload,
                         ThreadMemberPayload
                         )
from .permissions import PermissionOverwrites
from .sticker     import Sticker
from .types       import ObjectPayload
from .user        import User
from datetime     import datetime
from typing       import *

if TYPE_CHECKING:
  from .ws        import DiscordWebSocket


class Constructor:
  ws : DiscordWebSocket = None


  @staticmethod
  def channel(data : Dict[str, Any]) -> Union[DMChannel. GuildChannel]:
    from .objects import (
                         AnnouncementChannelObject,
                         CategoryChannelObject,
                         DMChannelObject,
                         ForumObject,
                         MediaChannelObject,
                         StageChannelObject,
                         TextChannelObject,
                         ThreadObject,
                         VoiceChannelObject
                         )
    try:
      channel_objects : Dict[ChannelType, Union[DMChannel, GuildChannel]] = {
        ChannelType.announcement        : AnnouncementChannelObject,
        ChannelType.announcement_thread : ThreadObject,
        ChannelType.category            : CategoryChannelObject,
        ChannelType.dm                  : DMChannelObject,
        ChannelType.forum               : ForumObject,
        ChannelType.group_dm            : DMChannelObject,
        ChannelType.media               : MediaChannelObject,
        ChannelType.private_thread      : ThreadObject,
        ChannelType.public_thread       : ThreadObject,
        ChannelType.stage               : StageChannelObject,
        ChannelType.text                : TextChannelObject,
        ChannelType.voice               : VoiceChannelObject
      }
      channel : Union[DMChannel, GuildChannel] = channel_objects[ChannelType(data["type"])](data)
      channel.__dict__["ws"] : DiscordWebSocket = Constructor.ws
      return channel
    except Exception as error:
      if ws.app.logger: ws.app.logger.error(error)


  @staticmethod
  def embed(data : ObjectPayload) -> Embed:
    from .objects import EmbedObject
    return EmbedObject(data)


  @staticmethod
  def emoji(data : Dict[str, Any]) -> Emoji:
    from .objects import EmojiObject
    emoji : Emoji = EmojiObject(data)
    return emoji


  @staticmethod
  def exception(err_cls : Exception, *data : Any, message : Optional[str] = None) -> Exception:
    error : Exception = err_cls(message)
    error.message : str = message
    match error:
      case BotMissingPermissions | MissingPermissions:
        error.missing_permissions : List[PermissionFlags] = [permission for permission in data if isinstance(permission, PermissionFlags)]
      case MissingArguments:
        error.missing_arguments : List[str] = [argument for argument in data]
      case NotFound:
        error.missing : List[str] = list(data)
    return error


  @staticmethod
  def guild(data : Dict[str, Any]) -> Guild:
    from .objects import GuildObject
    guild : Guild = GuildObject(data)
    guild.channels : CallableGuildChannels = CallableGuildChannels()
    return guild


  @staticmethod
  def guild_asset(asset_type : str, data : Dict[str, Any]) -> Asset:
    asset : Asset = Asset()
    asset.key : str = data[asset_type]
    match asset_type:
      case "discovery_splash": endpoint : str = "discovery_splashes"
      case "icon": endpoint : str = "icons"
      case "splash": endpoint : str = "splashes"
    asset.url : str = f"https://cdn.discordapp.com/{endpoint}/{data["id"]}/{asset.key}.{"gif" if asset.key.startswith("a_") else "png"}"
    return asset

  
  @staticmethod
  def guild_preview(data : Dict[str, Any]) -> GuildPreview:
    preview : GuildPreview = GuildPreview()
    for attribute in data:
      match attribute:
        case "id": preview.id : int = data[attribute]
        case "name": preview.name : str = data[attribute]
        case "icon" | "splash" | "discovery_splash": preview.icon : Asset = Constructor.guild_asset(attribute, data)
        case "emojis": preview.emojis : List[Emoji] = [Emoji.from_data(emoji) for emoji in data[attribute]]
        case "features": preview.features : List[str] = data[attribute]
        case "approximate_member_count": preview.approximate_member_count : int = data[attribute]
        case "approximate_presence_count": preview.approximate_presence_count : int = data[attribute]
        case "description": preview.description : str = data[attribute]
        case "stickers": preview.stickers : List[Sticker] = [Sticker.from_data(sticker) for sticker in data[attribute]]
    return preview



  @staticmethod
  def info(data : Dict[str, Any]) -> AppInfo:
    from .objects import ApplicatonObject
    return ApplicationObject(data)


  @staticmethod
  def invite(data : Dict[str, Any]) -> Invite:
    from .objects import InviteObject
    invite : Invite = InviteObject(data)
    return invite


  @staticmethod
  def member(data : Dict[str, Any]) -> Member:
    from .objects import MemberObject
    member : Member = MemberObject(data)
    return member


  @staticmethod
  def message(data : Dict[str, Any]) -> Message:
    from .objects import MessageObject
    return MessageObject(data)


  @staticmethod
  def payload(cls : BasePayload, data : Dict[str, Any]) -> BasePayload:
    payload : BasePayload = cls()
    for attribute in data:
      payload.__dict__[attribute] = data[attribute]
    return payload


  @staticmethod
  def sticker(data : Dict[str, Any]) -> Sticker:
    sticker : Sticker = Sticker()
    return sticker


  @staticmethod
  def thread_member(payload : ThreadMemberPayload) -> ThreadMember:
    thread_member : ThreadMember = ThreadMember()
    thread_member.__payload = payload
    return thread_member

  
  @staticmethod
  def user_asset(asset_type : str, data : Dict[str, Any]) -> Asset:
    asset : Asset = Asset()
    asset.key : str = data[asset_type]
    match asset_type:
      case "avatar": endpoint : str = "avatars"
      case "banner": endpoint : str = "banners"
    asset.url : str = f"https://cdn.discordapp.com/{endpoint}/{data["id"]}/{asset.key}.{"gif" if asset.key.startswith("a_") else "png"}"
    return asset


  @staticmethod
  def user(data : Union[Dict[str, Any], int]) -> User:
    user : User = None
    user.__dict__["ws"] = self.ws
    match type(data):
      case dict:
        user : User = User()
        for attribute in data:
          match attribute:
            case "id" | "discriminator": user.__dict__[attribute] : int = int(data[attribute])
            case "global_name":
              if not data[attribute]: user.__dict__[attribute] : str = data["username"]
              else:                   user.__dict__[attribute] : str = data[attribute]
            case "banner": user.__dict__[attribute] : Asset = Constructor.user_asset(attribute, data) if data[attribute] else None
            case "avatar":
              user.__dict__[attribute] : str = CallableAvatar(f"https://cdn.discordapp.com/avatars/{data["id"]}/{data["avatar"]}.{"gif" if data["avatar"].startswith("a_") else "png"}") if data[attribute] else ""
              user.default_avatar      : str = f"https://cdn.discordapp.com/embed/avatars/{(int(data["id"]) >> 22) % 6 if int(data["discriminator"]) == 0 else int(data["discriminator"]) % 5}.png"
              user.avatar_decoration   : str = f"https://cdn.discordapp.com/avatar-decoration-presets/{data["avatar_decoration_data"]["asset"]}.png" if data.get("avatar_decoration_data") else ""
            case "accent_color": user.__dict__[attribute]     : Color       = Color.from_int(data[attribute])
            case "locale":       user.__dict__[attribute]     : Locale      = Locale._value2member_map_[data[attribute]]
            case "flags":        user.__dict__[attribute]     : List[str]   = [name for name, flag in UserFlags._member_map_.items() if (data[attribute] & flag.value) == flag.value]
            case "public_flags": user.__dict__["user_flags"]  : List[str]   = [name for name, flag in UserFlags._member_map_.items() if (data[attribute] & flag.value) == flag.value]
            case "premium_type": user.__dict__[attribute]     : PremiumType = PremiumType._value2member_map_[data[attribute]]
            case _:              user.__dict__[attribute]     : Any         = data[attribute]
      case int:
        if ws.app.users(id = user_id): return ws.app.users(id = user_id)
        user : User = Constructor.user(ws.get(f"/users/{user_id}"))
        ws.app.users.append(user)
    return user