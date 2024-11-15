from .base  import BaseObject
from typing import *


class WelcomeScreenObject(BaseObject):
  from .welcome_screen_channel import WelcomeScreenChannelObject

  description      : Optional[str]
  welcome_channels : List[WelcomeScreenChannelObject] = []