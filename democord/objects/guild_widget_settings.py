from ..types import Snowflake
from .base   import BaseObject
from typing  import *


class GuildWidgetSettingsObject(BaseObject):
  channel_id : Optional[Snowflake]
  enabled    : bool