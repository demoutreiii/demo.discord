from .flags  import  (
                     ApplicationFlags
                     )
from typing  import *

if TYPE_CHECKING:
  from .asset import Asset
  from .guild import Guild
  from .user  import User


class AppInfoFlags(int):
  def __call__(self) -> List[str]:
    return [
      name
      for name, flag in ApplicationFlags._member_map_.items()
      if ( self & flag.value ) == flag.value
    ]

  def __int__(self) -> int:
    return self


class AppInfo(dict):
  @property
  def approximate_guild_count(self) -> int:
    return self.get("approximate_guild_count", 0)

  @property
  def approximate_user_install_count(self) -> int:
    return self.get("approximate_user_install_guild_count", 0)

  @property
  def bot(self) -> Optional["User"]:
    from .constructor import Constructor
    return Constructor.user(self["user"]) if self.get("user", None) else None

  @property
  def cover_image(self) -> Optional[str]:
    return self.get("cover_image")

  @property
  def custom_install_url(self) -> Optional[str]:
    return self.get("custom_install_url")

  @property
  def description(self) -> Optional[str]:
    return self.get("description")

  @property
  def event_webhooks_status(self) -> str:
    statuses : Dict[int, str] = {
      1 : "disabled",
      2 : "enabled",
      3 : "disabled_by_discord"
    }
    return statuses[self.get("event_webhooks_status", 1)]

  @property
  def event_webhooks_types(self) -> List[str]:
    return self.get("event_webhooks_types", [])

  @property
  def flags(self) -> AppInfoFlags:
    return AppInfoFlags(self.get("flags", 0))

  @property
  def guild(self) -> Optional["Guild"]:
    from .constructor import Constructor
    return Constructor.guild(self["guild"]) if self.get("guild") else None

  @property
  def icon(self) -> Optional["Asset"]:
    from .constructor import Constructor
    return Constructor.user_asset(self["icon"]) if self.get("icon") else None

  @property
  def id(self) -> int:
    return int(self.get("id", 0))

  @property
  def install_parameters(self) -> None:
    raise NotImplemented("install_parameters: incomplete implementation")

  @property
  def integration_types_config(self) -> None:
    raise NotImplemented("integration_types_config: incomplete implementation")

  @property
  def interactions_endpoint_url(self) -> Optional[str]:
    return self.get("interactions_endpoint_url")

  @property
  def name(self) -> str:
    return self.get("name", "")

  @property
  def owner(self) -> Optional["User"]:
    from .constructor import Constructor
    return Constructor.user(self["user"]) if self.get("user") else None

  @property
  def primary_sku_id(self) -> Optional[int]:
    return int(self["primary_sku_id"]) if self.get("primary_sku_id") else None

  @property
  def privacy_policy_url(self) -> Optional[str]:
    return sefl.get("privacy_policy_url")

  @property
  def public(self) -> bool:
    return self.get("bot_public", False)

  @property
  def redirect_uris(self) -> List[str]:
    return self.get("redirect_uris", [])

  @property
  def require_code_grant(self) -> bool:
    return self.get("bot_require_code_grant", False)

  @property
  def role_connections_verification_url(self) -> Optional[str]:
    return self.get("role_connections_verification_url")

  @property
  def rpc_regions(self) -> List[str]:
    return self.get("rpc_regions", [])

  @property
  def slug(self) -> Optional[str]:
    return self.get("slug")

  @property
  def tags(self) -> List[str]:
    return self.get("tags", [])

  @property
  def team(self) -> None:
    raise NotImplemented("team: incomplete implementation")

  @property
  def tos_url(self) -> Optional[str]:
    return self.get("terms_of_service_url")

  @property
  def verify_key(self) -> str:
    return self.get("verify_key")