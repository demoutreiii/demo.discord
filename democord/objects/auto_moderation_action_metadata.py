from ..types import Snowflake
from .base   import BaseObject
from typing  import *


class AutoModerationActionMetadataObject(BaseObject):
  channel_id       : Snowflake
  custom_message   : Optional[str]
  duration_seconds : int