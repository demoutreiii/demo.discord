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
  def __init__(self, data: dict[str, ...]) -> None:
    self.__data: dict[str, ...] = data


  @property
  def approximate_guild_count(self) -> Optional[int]:
    return self.__data.get("approximate_guild_count")


  @property
  def approximate_user_install_count(self) -> Optional[int]:
    return self.__data.get("approximate_user_install_count")


  @property
  def bot(self) -> Optional[User]:
    return User(self.__data["bot"]) if "bot" in self.__data else None


  @property
  def bot_public(self) -> bool:
    return self.__data["bot_public"]


  @property
  def bot_require_code_grant(self) -> bool:
    return self.__data["bot_require_code_grant"]


  @property
  def cover_image(self) -> Optional[Asset]:
    return Asset(self.__data["cover_image"]) if "cover_image" in self.__data else None


  @property
  def custom_install_url(self) -> Optional[str]:
    return self.__data.get("custom_install_url")


  @property
  def description(self) -> str:
    return self.__data["description"]


  @property
  def event_webhook_status(self) -> ApplicationEventWebhookStatus:
    return ApplicationEventWebhookStatus(self.__data["event_webhook_status"])


  @property
  def event_webhooks_types(self) -> list[str]:
    return self.__data.get("event_webhooks_types", list())


  @property
  def event_webhooks_url(self) -> Optional[str]:
    return self.__data.get("event_webhooks_url")


  @property
  def flags(self) -> int:
    return self.__data.get("flags", 0)


  @property
  def guild(self) -> Optional[Guild]:
    return Guild(self.__data["guild"]) if "guild" in self.__data else None


  @property
  def guild_id(self) -> Optional[Snowflake]:
    return Snowflake(self.__data["guild_id"]) if "guild_id" in self.__data else None


  @property
  def icon(self) -> Optional[Asset]:
    return Asset(self.__data["icon"]) if self.__data["icon"] is not None else None


  @property
  def id(self) -> Snowflake:
    return Snowflake(self.__data["id"])


  @property
  def install_params(self) -> Optional[InstallParams]:
    return InstallParams(self.__data["install_params"]) if "install_params" in self.__data else None


  @property
  def integration_types_config(self) -> Optional[dict[ApplicationIntegrationType, ApplicationIntegrationTypeConfiguration]]:
    return { integration_type: ApplicationIntegrationTypeConfiguration(integration_type_config) for integration_type, integration_type_config in self.__data["integration_types_config"].items() } if "integration_types_config" in self.__data else None


  @property
  def interactions_endpoint_url(self) -> Optional[str]:
    return self.__data.get("interactions_endpoint_url")


  @property
  def name(self) -> str:
    return self.__data["name"]


  @property
  def owner(self) -> Optional[User]:
    return User(self.__data["owner"]) if "owner" in self.__data else None


  @property
  def primary_sku_id(self) -> Optional[Snowflake]:
    return Snowflake(self.__data["primary_sku_id"]) if "primary_sku_id" in self.__data else None


  @property
  def privacy_policy_url(self) -> Optional[str]:
    return self.__data.get("privacy_policy_url")


  @property
  def redirect_uris(self) -> list[str]:
    return self.__data.get("redirect_uris", list())


  @property
  def role_connections_verification_url(self) -> Optional[str]:
    return self.__data.get("role_connections_verification_url")


  @property
  def rpc_origins(self) -> list[str]:
    return self.__data.get("rpc_origins", list())


  @property
  def slug(self) -> Optional[str]:
    return self.__data.get("slug")


  @property
  def tags(self) -> list[str]:
    return self.__data.get("tags", list())


  @property
  def team(self) -> Optional[Team]:
    return Team(self.__data["team"]) if self.__data["team"] is not None else None


  @property
  def terms_of_service_url(self) -> Optional[str]:
    return self.__data.get("terms_of_service_url")


  @property
  def verify_key(self) -> str:
    return self.__data["verify_key"]