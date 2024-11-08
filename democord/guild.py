from .asset       import Asset
from .channels    import (
                         GuildChannel,
                         TextChannel,
                         Thread
                         )
from .constructor import Constructor
from .emoji       import Emoji
from .enums       import (
                         ChannelType,
                         DefaultMessageNotification,
                         ExplicitContentFilter,
                         ErrorCodes,
                         GuildFeatures,
                         MFALevel,
                         NSFWLevel,
                         PermissionFlags,
                         PremiumTier,
                         VerificationLevel
                         )
from .errors      import (
                         BotMissingPermissions,
                         MissingPermissions
                         )
from .file        import File
from .flags       import (
                         SystemChannelFlags
                         )
from .locales     import Locale
from .member      import Member
from .reqs        import (
                         DELETE,
                         GET,
                         PATCH,
                         PUT
                         )
from .user        import User
from typing       import *

if TYPE_CHECKING:
  from .ws        import DiscordWebSocket


class CallableSystemChannelFlags(list):
  """
  Callable property for Guild.system_channel_flags attribute
  """

  def __call__(
    self,
    flag : SystemChannelFlags
  ) -> bool:
    """
    Checks if a certain system channel flag is found in the data


    Returns
    -------
    bool
    """

    return flag.name in self


class CallableGuildChannels(list):
  """
  Callable property for Guild.channels attribute
  """

  def __call__(
    self,
    **kwargs
  ) -> Optional[List[GuildChannel] | GuildChannel]:
    """
    Filter the returned list by the passed GuildChannel attributes


    Parameters
    ----------
    **kwargs
      Keyword arguments of ( or a subclass of ) GuildChannel attributes


    Returns
    -------
    Optional[List[GuildChannel] | GuildChannel]
    """

    if not args: return self
    matches : List[GuildChannel] = [
      guild_channel
      for guild_channel in self
      if all(
        guild_channel.__dict__[kwarg] == kwargs[kwarg]
        for kwarg in kwargs
        if guild_channel.__dict__.get(kwarg)
      )
    ]
    return (matches[0] if len(matches) == 1 else matches) if matches else None


class CallableGuildMembers(list):
  """
  Callable property for Guild.members attribute
  """

  def __call__(
    self,
    **kwargs
  ) -> Optional[List[Member] | Member]:
    """
    Filter the result by the passed Member attributes


    Parameters
    ----------
    **kwargs
      Keyword arguments that are used to filter the result


    Returns
    -------
    Optional[List[Member] | Member]
    """

    if not args: return self
    matches : list[Member] = [
      member
      for member in self
      if all(
        member.__dict__[kwarg] == kwargs[kwarg]
        for kwarg in kwargs
        if member.__dict__.get(kwarg)
      )
    ]
    return (matches[0] if len(matches) == 1 else matches) if matches else None

  
  def __contains__(self, member : Union[Member, int]) -> bool:
    if not isinstance(member, (Member, int)): raise TypeError("member: must be of type <Member> or <int>")
    return int(member) in self
  

class GuildPreview: ...


class Guild:
  """
  Represents a Discord guild, called " servers " in the UI
  """

  members : list = CallableGuildMembers()

  def __eq__(
    self,
    guild : Self
  ) -> bool:
    """
    Compares whether 2 Guild objects are equal


    Parameters
    ----------
    guild : Guild
      Guild object to compare with


    Returns
    -------
    bool
    """

    assert isinstance(guild, (Guild, int)), f"Must be of type <Guild> or <int>, not {type(guild)}"
    if isinstance(guild, Guild): return self.id == guild.id
    if isinstance(guild, int):   return self.id == guild


  def __int__(
    self
  ) -> int:
    """
    Utilizes the built-in int() function and returns the ID of the guild


    Returns
    -------
    int
    """

    return self.id


  def __ne__(
    self,
    guild : Self
  ) -> bool:
    """
    Compares whether 2 Guild objects are not equal


    Parameters
    ----------
    guild : Guild
      Guild object to compare with


    Returns
    -------
    bool
    """

    assert isinstance(guild, (Guild, int)), f"Must be of type Guild or int, not {type(guild)}"
    if isinstance(guild, Guild): return self.id != guild.id
    if isinstance(guild, int):   return self.id != guild


  def __str__(
    self
  ) -> str:
    """
    Utilizes the built-in str() function and returns the name of the guild


    Returns
    -------
    str
    """

    return self.name

  @property
  def afk_channel_id(self) -> Optional[int]:
    if self["afk_channel_id"] is None: return None
    return int(self["afk_channel_id"])

  @property
  def afk_timeout(self) -> int:
    return self["afk_timeout"]

  @property
  def application_id(self) -> Optional[int]:
    if self["application_id"] is None: return None
    return int(self["application_id"])

  @property
  def approximate_member_count(self) -> int:
    return self["approximate_member_count"]

  @property
  def approximate_presence_count(self) -> int:
    return self["approximate_presence_count"]

  @property
  def banner(self) -> Optional[Asset]:
    # implement: Asset[GuildBanner]
    raise NotImplementedError

  @property
  def default_message_notifications(self) -> str:
    return DefaultMessageNotification(self["default_message_notifications"]).name

  @property
  def description(self) -> Optional[str]:
    return self["description"]

  @property
  def discovery_splash(self) -> Optional[Asset]:
    # implement: Asset[GuildDiscoverySplash]
    raise NotImplementedError

  @property
  def emojis(self) -> List[Emoji]:
    # implement: Emoji
    raise NotImplementedError

  @property
  def explicit_content_filter(self) -> str:
    return ExplicitContentFilter(self["explicit_content_filter"]).name

  @property
  def features(self) -> List[str]:
    return self["features"]

  @property
  def icon(self) -> Optional[Asset]:
    # implement: Asset[GuildIcon]
    raise NotImplementedError

  @property
  def id(self) -> int:
    return int(self["id"])

  @property
  def is_owner(self) -> bool:
    return self["owner"]

  @property
  def max_members(self) -> int:
    return self["max_members"]

  @property
  def max_presences(self) -> Optional[int]:
    return self["max_presences"]

  @property
  def max_stage_users(self) -> int:
    return self["max_stage_video_channel_users"]

  @property
  def max_video_users(self) -> int:
    return self["max_video_channel_users"]

  @property
  def me(self) -> Optional[Member]:
    # retrieve MemberObject from cache
    raise NotImplementedError

  @property
  def mfa_level(self) -> str:
    return MFALevel(self["mfa_level"]).name

  @property
  def name(self) -> str:
    return self["name"]

  @property
  def nsfw_level(self) -> str:
    return NSFWLevel(self["nsfw_level"]).name

  @property
  def owner(self) -> User:
    # implement: UserObject
    # retrieve from cache
    raise NotImplementedError

  @property
  def permissions(self) -> Permissions:
    # implement: Permissions
    raise NotImplementedError

  @property
  def preferred_locale(self) -> str:
    return self["preferred_locale"]

  @property
  def premium_progress_bar_enabled(self) -> bool:
    return self["premium_progress_bar_enabled"]

  @property
  def premium_subscription_count(self) -> int:
    return self["premium_subscription_count"]

  @property
  def premium_tier(self) -> int:
    return self["premium_tier"]

  @property
  def public_updates_channel_id(self) -> Optional[int]:
    if self["public_updates_channel_id"] is None: return None
    return int(self["public_updates_channel_id"])

  @property
  def splash(self) -> Optional[Asset]:
    # implement: Asset[GuildSplash]
    raise NotImplementedError

  @property
  def stickers(self) -> List[Sticker]:
    # implement: StickerObject
    raise NotImplementedError

  @property
  def system_channel_flags(self) -> List[str]:
    return [
      flag.name
      for flag in SystemChannelFlags
      if (self["system_channel_flags"] & flag.value) == flag.value
    ]

  @property
  def system_channel_id(self) -> Optional[int]:
    if self["system_channel_id"] is None: return None
    return int(self["system_channel_id"])

  @property
  def vanity_url_code(self) -> Optional[str]:
    return self["vanity_url_code"]

  @property
  def verification_level(self) -> str:
    return VerificationLevel(self["verification_level"]).name

  @property
  def welcome_screen(self) -> WelcomeScreen:
    # implement: WelcomeScreen
    raise NotImplementedError

  @property
  def widget_channel_id(self) -> Optional[int]:
    if self["widget_channel_id"] is None: return None
    return int(self["widget_channel_id"])

  @property
  def widget_enabled(self) -> bool:
    return self["widget_enabled"]


  async def add_member(
    self,
    user : User,
    access_token : str,
    *,
    nick : Optional[str] = None,
    roles : Optional[List[Role]] = [],
    mute : Optional[bool] = False,
    deaf : Optional[bool] = False
  ) -> Member:
    try:
      if not isinstance(access_token, str): raise TypeError("access_token: must be of type <str>")
      if nick and not isinstance(nick, str): raise TypeError("nick: must be of type <str>")
      if isinstance(roles, list):
        for role in roles:
          if not isinstance(role, Role): raise ValueError("roles: must contain <Role> objects")
      else: raise TypeError("roles: must be of type <list> containing <Role> objects")
      if not isinstance(mute, bool): raise TypeError("mute: must be of type <bool>")
      if not isinstance(deaf, bool): raise TypeError("deaf: must be of type <bool>")
      response : Dict[str, Any] = self.ws.put(
        PUT.member(self.id, user.id),
        data = {
          "access_token": access_token,
          "nick": nick,
          "roles": [role.id for role in roles],
          "mute": mute,
          "deaf": deaf
        }
      )
      return Member.from_data(self.ws, response)
      if response.get("code"):
        match ErrorCodes(response.get("code")):
          case ErrorCodes.MissingPermissions:
            raise BotMissingPermissions(PermissionFlags.create_instant_invite)
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def delete(self) -> None:
    try:
      if self.id != self.ws.app.appinfo.id:
        raise BotMissingPermissions("Bot must be the guild owner in order to delete the guild.")
      self.ws.delete(DELETE.guild(self.id))
      self.ws.app.guilds.remove(self.ws.app.guilds(id = self.id)[0])
      return None
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def edit(
    self,
    **attributes
  ) -> Self:
    """
    Modify the guild with the new attributes


    Parameters
    ----------
    afk_channel : Union[GuildChannel, int]
      New afk_channel of the guild. Pass ` None ` to remove

    afk_timeout : int
      Set the AFK timeout from the following values: 60, 300, 900, 1_800, 3_600

    default_message_notifications : DefaultMessageNotification
      New default message notifications level

    description : Optional[str]
      New guild description. Pass ` None ` to remove the existing description

    explicit_content_filter : ExplicitContentFilter
      New explicit content filter level

    icon : Optional[File]
      New guild icon. Pass ` None ` to remove

    name : str
      New guild name

    owner : User
      New guild owner. The application must be the current guild owner in order to execute this action

    verification_level : VerificationLevel
      New verification level
    """

    try:
      if not attributes: raise MissingArguments("Arguments are required to be filled in this method")
      data : Dict[str, Union[str, int, None]] = {}

      for attribute in attributes:
        match attribute:
          case "afk_channel":
            if not isinstance(attributes[attribute], (GuildChannel, int, None)):
              raise TypeError("Guild.afk_channel must either be a <GuildChannel> or <int>, or <NoneType> to remove")
            data[attribute] : int = int(attributes[attribute])
          
          case "afk_timeout":
            if not isinstance(attributes[attribute], int): raise TypeError("Guild.afk_timeout must be of type <int>")
            if attributes[attribute] not in [60, 300, 900, 1_800, 3_600]: raise ValueError("Guild.afk_timeout must be of one of the values: 60, 300, 900, 1800, 3600")
            data[attribute] : int = attributes[attribute]

          case "banner":
            if not isinstance(attributes[attribute], (File, None)):
              raise TypeError("Guild.banner must be of type <File>")
            if attributes[attribute]:
              if "BANNER" not in self.features:
                raise ValueError("Guild is not eligible for guild banners")
              if attributes[attribute].filename.endswith(".gif") and "ANIMATED_ICON" not in self.features:
                raise ValueError("Guild is not eligible for animated banners")
            data[attribute] : str = attributes[attribute].data if attributes[attribute] else None

          case "default_message_notifications":
            if not isinstance(attributes[attribute], DefaultMessageNotification):
              raise TypeError("Guild.default_message_notifications must be of type <DefaultMessagenotification[Enum]>")
            data[attribute] : int = attributes[attribute].value
          
          case "description":
            if not isinstance(attributes[attribute], (str, None)):
              raise TypeError("Guild.description must be of type <str> or <NoneType>")
            data[attribute] : str = attributes[attribute]
          
          case "explicit_content_filter":
            if not isinstance(attributes[attribute], ExplicitContentFilter):
              raise TypeError("Guild.explicit_content_filter must be of type <ExplicitContentFilter[Enum]>")
            data[attribute] : int = attributes[attribute].value

          case "features":
            if not isinstance(attributes[attribute], list):
              raise TypeError("Guild.features must be a list of type <str>")
            valid_features : List[str] = [
              feature.capitalize()
              for feature in attributes[attribute]
              if feature.capitalize() in GuildFeatures._value2member_map_
            ]
            if valid_features:
              data[attribute] : List[str] = valid_features
          
          case "icon":
            if not isinstance(attributes[attribute], (File, None)): raise TypeError("Guild.icon must be of type <File>")
            if attributes[attribute]:
              if attributes[attribute].filename.endswith(".gif") and "ANIMATED_ICON" not in self.features: raise ValueError("Guild is not eligible for animated icons")
            data[attribute] : str = attributes[attribute].data if attributes[attribute] else None

          case "name":
            if not isinstance(attributes[attribute], str):
              raise TypeError("Guild.name must be of type <str>")
            data[attribute] : str = attributes[attribute]
          
          case "owner":
            if not isinstance(attributes[attribute], User): raise TypeError("Guild.owner must be of type <User>")
            data[attribute] : int = attributes[attribute].id

          case "preferred_locale":
            if not isinstance(attributes[attribute], Locale):
              raise TypeError("Guild.preferred_locale must be of type <Locale>")
            data[attribute] : str = attributes[attribute].name

          case "premium_progress_bar":
            if not isinstance(attributes[attribute], bool):
              raise TypeError("Guild.premium_progress_bar must be of type <bool>")
            data[attribute] : bool = attributes[attribute]

          case "public_updates_channel":
            if not isinstance(attributes[attribute], (GuildChannel, None)):
              raise TypeError("Guild.public_updates_channel must be of type <GuildChannel> or <NoneType>")
            data[attribute] : int | None = int(attributes[attribute]) if attributes[attribute] else None

          case "rules_channel":
            if not isinstance(attributes[attribute], (GuildChannel, None)):
              raise TypeError("Guild.rules_channel must be of type <GuildChannel> or <NoneType>")
            data[attribute] : int | None = int(attributes[attribute]) if attributes[attribute] else None

          case "safety_alerts_channel":
            if not isinstance(attributes[attribute], (GuildChannel, None)):
              raise TypeError("Guild.safety_alerts_channel must be of type <GuildChannel> or <NoneType>")
            data[attribute] : int | None = int(attributes[attribute]) if attributes[attribute] else None

          case "system_channel":
            if not isinstance(attributes[attribute], (GuildChannel, None)):
              raise TypeError("Guild.system_channel must be of type <GuildChannel> or <NoneType>")
            data[attribute] : int | None = int(attributes[attribute]) if attributes[attribute] else None

          case "system_channel_flags":
            if not isinstance(attributes[attribute], List[SystemChannelFlags]):
              raise TypeError("Guild.system_channel_flags must be a list of type <SystemChannelFlags>")
            for flag in attributes[attribute]:
              if isinstance(flag, SystemChannelFlags):
                data[attribute] |= flag.value

          case "verification_level":
            if not isinstance(attributes[attribute], VerificationLevel):
              raise TypeError("Guild.verification_level must be of type <VerificationLevel[Enum]>")
            data[attribute] : int = attributes[attribute].value

      reason : str = str(attributes.get("reason"))
      response : dict = self.ws.patch(
        PATCH.guild(self.id),
        data   = data,
        reason = reason
      )
      if response.get("code"):
        match ErrorCodes(response.get("code")):
          case ErrorCodes.MissingPermissions:
            raise Constructor.exception(BotMissingPermissions, PermissionFlags.manage_guild)
      return Constructor.guild(response)
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def fetch_member(
    self,
    member_id : int
  ) -> Member:
    try:
      response : Dict[str, Any] = self.ws.get(GET.member(self.id, member_id))
      return Member.from_data(self.ws, response)
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def fetch_members(
    self,
    limit : Optional[int] = 1_000,
    after : Optional[int] = 0
  ) -> List[Member]:
    try:
      if not isinstance(limit, int): raise TypeError("limit: must be of type <int>")
      if limit < 0 or limit > 1_000: raise ValueError("limit: must be between 0 and 1,000")
      if not isinstance(after, int): raise TypeError("after: must be of type <int>")
      if after < 0: raise ValueError("after: must be 0 or greater")
      response : Dict[str, Any] = self.ws.get(GET.members(self.id, limit, after))
      return [Member.from_data(data) for data in response]
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def kick(
    self,
    member_id : int,
    reason : Optional[str] = None
  ) -> None:
    try:
      if member_id not in self.members: raise ValueError(f"No member with an ID: {member_id}")
      # check permission: kick_members
      response : Dict[str, Any] = self.ws.delete(
        DELETE.member(self.id, member_id),
        reason = reason
      )
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)


  async def preview(self) -> GuildPreview:
    try:
      return Constructor.guild_preview(self.ws.get(GET.guild_preview(self.id)))
    except Exception as error:
      if self.ws.app.logger: self.ws.app.logger.error(error)