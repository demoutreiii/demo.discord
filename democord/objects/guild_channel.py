from ..channels import GuildChannel
from ..types    import Snowflake
from .base      import BaseObject
from typing     import *


class GuildChannelObject(BaseObject, GuildChannel):
  from .overwrite import OverwriteObject

  guild_id              : Snowflake             = None
  id                    : Snowflake
  name                  : Optional[str]
  permission_overwrites : List[OverwriteObject] = []
  permissions           : str                   = None
  position              : int                   = None
  type                  : int