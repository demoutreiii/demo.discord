from enum   import Enum
from typing import *


class ApplicationEventWebhookStatus(Enum):
  disabled            = 1
  enabled             = 2
  disabled_by_discord = 3


class ApplicationIntegrationType(Enum):
  guild_install = 0
  user_intall   = 1