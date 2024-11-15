from ..types import Snowflake
from .base   import BaseObject
from typing  import *


class WelcomeScreenChannelObject(BaseObject):
  channel_id  : Snowflake
  description : str
  emoji_id    : Optional[Snowflake]
  emoji_name  : Optional[str]