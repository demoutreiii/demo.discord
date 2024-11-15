from ..types import Snowflake
from .base   import BaseObject
from typing  import *


class GuildPreviewObject(BaseObject):
  from .emoji   import EmojiObject
  from .sticker import StickerObject

  approximate_member_count   : int
  approximate_presence_count : int
  description                : Optional[str]
  discovery_splash           : Optional[str]
  emojis                     : List[EmojiObject]   = []
  features                   : List[str]           = []
  icon                       : Optional[str]
  id                         : Snowflake
  name                       : str
  splash                     : Optional[str]
  stickers                   : List[StickerObject] = []