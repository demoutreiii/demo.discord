from ..types import Snowflake
from .base   import BaseObject
from typing  import *


class OptionalAuditEntryInfoObject(BaseObject):
  application_id                    : Snowflake
  auto_moderation_rule_name         : str
  auto_moderation_rule_trigger_type : str
  channel_id                        : Snowflake
  count                             : str
  delete_member_days                : str
  id                                : Snowflake
  members_removed                   : str
  message_id                        : Snowflake
  role_name                         : str
  type                              : str
  integration_type                  : str