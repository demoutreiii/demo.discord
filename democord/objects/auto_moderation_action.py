from .base   import BaseObject
from typing  import *


class AutoModerationActionObject(BaseObject):
  from .auto_moderation_action_metadata import AutoModerationActionMetadataObject

  type     : int
  metadata : Optional[AutoModerationActionMetadataObject]