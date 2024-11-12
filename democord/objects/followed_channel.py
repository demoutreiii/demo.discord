from ..types import Snowflake
from .base   import BaseObject
from typing  import *


class FollowedChannelObject(BaseObject):
  channel_id : Snowflake
  webhook_id : Snowflake