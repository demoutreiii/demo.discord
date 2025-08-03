from ..enums import DefaultMessageNotificationLevel, ExplicitContentFilterLevel, GuildFeature, GuildNSFWLevel, Locale, MFALevel, VerificationLevel
from ..flags import SystemChannelFlag
from .asset import Asset
from .emoji import Emoji
from .incidents_data import IncidentsData
from .role import Role
from .snowflake import Snowflake
from .sticker import Sticker
from .welcome_screen import WelcomeScreen
from typing import Optional


class Guild(dict):
  @property
  def afk_channel_id(self) -> Optional[Snowflake]:
    return Snowflake(self["afk_channel_id"]) if self["afk_channel_id"] is not None else None


  @property
  def afk_timeout(self) -> int:
    return self["afk_timeout"]


  @property
  def application_id(self) -> Optional[Snowflake]:
    return Snowflake(self["application_id"]) if self["application_id"] is not None else None


  @property
  def approximate_member_count(self) -> Optional[int]:
    return self.get("approximate_member_count")


  @property
  def approximate_presence_count(self) -> Optional[int]:
    return self.get("approximate_presence_count")
  
  
  @property
  def banner(self) -> Optional[Asset]:
    return Asset(self["banner"]) if self["banner"] is not None else None
  
  
  @property
  def description(self) -> Optional[str]:
    return self["description"]
  
  
  @property
  def default_message_notifications(self) -> DefaultMessageNotificationLevel:
    return DefaultMessageNotificationLevel(self["default_message_notifications"])
  
  
  @property
  def discovery_splash(self) -> Optional[Asset]:
    return Asset(self["discovery_splash"]) if self["discovery_splash"] is not None else None


  @property
  def emojis(self) -> list[Emoji]:
    return [Emoji(data) for data in self["emojis"]]


  @property
  def explicit_content_filter(self) -> ExplicitContentFilterLevel:
    return ExplicitContentFilterLevel(self["explicit_content_filter"])


  @property
  def features(self) -> list[GuildFeature]:
    return [GuildFeature(name) for name in self["features"]]
  
  
  @property
  def icon(self) -> Optional[Asset]:
    return Asset(self["icon"]) if self["icon"] is not None else None


  @property
  def icon_hash(self) -> Optional[str]:
    return self.get("icon_hash")
  
  
  @property
  def id(self) -> Snowflake:
    return Snowflake(self["id"])


  @property
  def incidents_data(self) -> Optional[IncidentsData]:
    return IncidentsData(self["incidents_data"]) if self["incidents_data"] is not None else None


  @property
  def max_members(self) -> Optional[int]:
    return self["max_members"] if "max_members" in self else None


  @property
  def max_presences(self) -> Optional[int]:
    return self.get("max_presences")


  @property
  def max_stage_video_channel_users(self) -> Optional[int]:
    return self.get("max_stage_video_channel_users")


  @property
  def max_video_channel_users(self) -> Optional[int]:
    return self.get("max_video_channel_users")


  @property
  def mfa_level(self) -> MFALevel:
    return MFALevel(self["mfa_level"])


  @property
  def name(self) -> str:
    return self["name"]


  @property
  def nsfw_level(self) -> GuildNSFWLevel:
    return GuildNSFWLevel(self["nsfw_level"])


  @property
  def owner(self) -> bool:
    return self.get("owner", False)


  @property
  def owner_id(self) -> Snowflake:
    return Snowflake(self["owner_id"])


  @property
  def permissions(self) -> Optional[str]:
    return self.get("permissions")


  @property
  def preferred_locale(self) -> Locale:
    return Locale(self["preferred_locale"])


  @property
  def premium_progress_bar_enabled(self) -> bool:
    return self["premium_progress_bar_enabled"]


  @property
  def premium_subscription_count(self) -> int:
    return self.get("premium_subscription_count", 0)


  @property
  def premium_tier(self) -> int:
    return self["premium_tier"]


  @property
  def public_updates_channel_id(self) -> Optional[Snowflake]:
    return Snowflake(self["public_updates_channel_id"]) if self["public_updates_channel_id"] is not None else None


  @property
  def region(self) -> Optional[str]:
    return self.get("region")


  @property
  def roles(self) -> list[Role]:
    return [Role(data) for data in self["roles"]]


  @property
  def rules_channel_id(self) -> Optional[Snowflake]:
    return Snowflake(self["rules_channel_id"]) if self["rules_channel_id"] is not None else None


  @property
  def safety_alerts_channel_id(self) -> Optional[Snowflake]:
    return Snowflake(self["safety_alerts_channel_id"]) if self["safety_alerts_channel_id"] is not None else None


  @property
  def splash(self) -> Optional[Asset]:
    return Asset(self["splash"]) if self["splash"] is not None else None


  @property
  def stickers(self) -> Optional[list[Sticker]]:
    return [Sticker(data) for data in self["stickers"]] if "stickers" in self else None


  @property
  def system_channel_flags(self) -> SystemChannelFlag:
    return SystemChannelFlag(self["system_channel_flags"])


  @property
  def system_channel_id(self) -> Optional[Snowflake]:
    return Snowflake(self["system_channel_id"]) if self["system_channel_id"] is not None else None


  @property
  def unavailable(self) -> bool:
    return self.get("unavailable", False)


  @property
  def vanity_url_code(self) -> Optional[str]:
    return self["vanity_url_code"]


  @property
  def verification_level(self) -> VerificationLevel:
    return VerificationLevel(self["verification_level"])


  @property
  def welcome_screen(self) -> Optional[WelcomeScreen]:
    return WelcomeScreen(self["welcome_screen"]) if "welcome_screen" in self else None


  @property
  def widget_channel_id(self) -> Optional[Snowflake]:
    return Snowflake(self["widget_channel_id"]) if self.get("widget_channel_id") is not None else None


  @property
  def widget_enabled(self) -> bool:
    return self.get("widget_enabled", False)