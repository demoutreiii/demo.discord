from ..appinfo import AppInfo
from ..types   import Snowflake
from .base     import BaseObject
from typing    import *


class ApplicationObject(BaseObject, AppInfo):
  from .guild          import GuildObject
  from .install_params import InstallParamsObject
  from .team           import TeamObject
  from .user           import UserObject


  approximate_guild_count           : int                 = 0
  approximate_user_install_count    : int                 = 0
  bot                               : UserObject          = None
  bot_public                        : bool                = True
  bot_require_code_grant            : bool                = False
  cover_image                       : Optional[str]
  custom_install_url                : Optional[str]
  description                       : Optional[str]
  event_webhooks_status             : Literal[1, 2, 3]    = 1
  event_webhooks_types              : List[str]           = []
  flags                             : Optional[int]
  guild                             : GuildObject         = None
  guild_id                          : Snowflake           = None
  icon                              : Optional[str]
  id                                : Snowflake
  install_params                    : InstallParamsObject
  integration_types_config          : Dict[str, Any]
  interactions_endpoint_url         : Optional[str]
  name                              : str
  owner                             : UserObject          = None
  primary_sku_id                    : Snowflake
  privacy_policy_url                : Optional[str]
  redirect_uris                     : List[str]           = []
  role_connections_verification_url : Optional[str]
  rpc_origins                       : List[str]           = []
  slug                              : Optional[str]
  tags                              : List[str]           = []
  team                              : TeamObject          = None
  terms_of_service_url              : Optional[str]
  verify_key                        : str