from ..enums import ApplicationIntegrationType, ApplicationWebhookStatus
from .application_integration_type_configuration import ApplicationIntegrationTypeConfiguration
from .asset import Asset
from .guild import Guild
from .install_params import InstallParams
from .snowflake import Snowflake
from .team import Team
from .user import User
from typing import Optional


class Application(dict):
  @property
  def approximate_guild_count(self) -> Optional[int]:
    return self.get("approximate_guild_count")


  @property
  def approximate_user_install_count(self) -> Optional[int]:
    return self.get("approximate_user_install_count")


  @property
  def bot(self) -> Optional[User]:
    return User(self["bot"]) if "bot" in self else None


  @property
  def bot_public(self) -> bool:
    return self["bot_public"]


  @property
  def bot_require_code_grant(self) -> bool:
    return self["bot_require_code_grant"]


  @property
  def cover_image(self) -> Optional[Asset]:
    return Asset(self["cover_image"]) if "cover_image" in self else None


  @property
  def custom_install_url(self) -> Optional[str]:
    return self.get("custom_install_url")


  @property
  def description(self) -> str:
    return self["description"]


  @property
  def event_webhook_status(self) -> ApplicationEventWebhookStatus:
    return ApplicationEventWebhookStatus(self["event_webhook_status"])


  @property
  def event_webhooks_types(self) -> list[str]:
    return self.get("event_webhooks_types", list())


  @property
  def event_webhooks_url(self) -> Optional[str]:
    return self.get("event_webhooks_url")


  @property
  def flags(self) -> int:
    return self.get("flags", 0)


  @property
  def guild(self) -> Optional[Guild]:
    return Guild(self["guild"]) if "guild" in self else None


  @property
  def guild_id(self) -> Optional[Snowflake]:
    return Snowflake(self["guild_id"]) if "guild_id" in self else None


  @property
  def icon(self) -> Optional[Asset]:
    return Asset(self["icon"]) if self["icon"] is not None else None


  @property
  def id(self) -> Snowflake:
    return Snowflake(self["id"])


  @property
  def install_params(self) -> Optional[InstallParams]:
    return InstallParams(self["install_params"]) if "install_params" in self else None


  @property
  def integration_types_config(self) -> Optional[dict[ApplicationIntegrationType, ApplicationIntegrationTypeConfiguration]]:
    return { integration_type: ApplicationIntegrationTypeConfiguration(integration_type_config) for integration_type, integration_type_config in self.__data["integration_types_config"].items() } if "integration_types_config" in self else None


  @property
  def interactions_endpoint_url(self) -> Optional[str]:
    return self.get("interactions_endpoint_url")


  @property
  def name(self) -> str:
    return self["name"]


  @property
  def owner(self) -> Optional[User]:
    return User(self["owner"]) if "owner" in self else None


  @property
  def primary_sku_id(self) -> Optional[Snowflake]:
    return Snowflake(self["primary_sku_id"]) if "primary_sku_id" in self else None


  @property
  def privacy_policy_url(self) -> Optional[str]:
    return self.get("privacy_policy_url")


  @property
  def redirect_uris(self) -> list[str]:
    return self.get("redirect_uris", list())


  @property
  def role_connections_verification_url(self) -> Optional[str]:
    return self.get("role_connections_verification_url")


  @property
  def rpc_origins(self) -> list[str]:
    return self.get("rpc_origins", list())


  @property
  def slug(self) -> Optional[str]:
    return self.get("slug")


  @property
  def tags(self) -> list[str]:
    return self.get("tags", list())


  @property
  def team(self) -> Optional[Team]:
    return Team(self["team"]) if self["team"] is not None else None


  @property
  def terms_of_service_url(self) -> Optional[str]:
    return self.get("terms_of_service_url")


  @property
  def verify_key(self) -> str:
    return self["verify_key"]