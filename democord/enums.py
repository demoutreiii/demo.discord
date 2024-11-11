from enum   import (
                   auto,
                   Enum,
                   StrEnum
                   )
from typing import *


class ActivityLocationKind(StrEnum):
  gc = auto()
  pc = auto()


class ApplicationEventWebhookStatus(Enum):
  disabled            = 1
  enabled             = 2
  disabled_by_discord = 3


class ApplicationIntegrationType(Enum):
  guild_install = 0
  user_intall   = 1