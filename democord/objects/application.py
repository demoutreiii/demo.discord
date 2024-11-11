from ..application import Application
from ..enums       import ApplicationIntegrationType
from ..types       import Snowflake
from .base         import BaseObject
from typing        import *


class ApplicationObject(BaseObject, Application):
  from .integration_type_config import ApplicationIntegrationTypeConfigObject
  from .guild                   import GuildObject
  from .install_params          import InstallParamsObject
  from .team                    import TeamObject
  from .user                    import UserObject

  approximate_user_install_count    : Optional[int]                                                            = 0
  approximate_guild_count           : Optional[int]                                                            = 0
  bot                               : Optional[UserObject]
  bot_require_code_grant            : bool                                                                     = False
  cover_image                       : Optional[str]
  custom_install_url                : Optional[str]
  description                       : str
  event_webhook_status              : Literal[1, 2, 3]                                                         = 1
  event_webhooks_types              : List[str]                                                                = []
  event_webhooks_url                : Optional[str]
  flags                             : Optional[int]                                                            = 0
  guild                             : Optional[GuildObject]
  guild_id                          : Optional[Snowflake]
  icon                              : Optional[str]
  id                                : Snowflake
  install_params                    : Optional[InstallParamsObject]
  integration_types_config          : Dict[ApplicationIntegrationType, ApplicationIntegrationTypeConfigObject]
  interactions_endpoint_url         : Optional[str]
  name                              : str
  owner                             : Optional[UserObject]
  primary_sku_id                    : Optional[Snowflake]
  privacy_policy_url                : Optional[str]
  redirect_uris                     : List[str]                                                                = []
  role_connections_verification_url : Optional[str]
  rpc_origins                       : List[str]                                                                = []
  slug                              : Optional[str]
  tags                              : List[str]                                                                = []
  team                              : Optional[TeamObject]
  terms_of_service_url              : Optional[str]
  verify_key                        : str