from ..types import Snowflake
from .base   import BaseObject
from typing  import *


class AutoModerationRuleObject(BaseObject):
  from .auto_moderation_action import AutoModerationActionObject
  from .trigger_metadata       import TriggerMetadataObject

  actions          : List[AutoModerationActionObject] = []
  creator_id       : Snowflake
  enabled          : bool                             = False
  event_type       : int
  exempt_channels  : List[Snowflake]                  = []
  exempt_roles     : List[Snowflake]                  = []
  guild_id         : Snowflake
  id               : Snowflake
  name             : str
  trigger_metadata : TriggerMetadataObject
  trigger_type     : int