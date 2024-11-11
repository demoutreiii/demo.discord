from ..enums import KeywordPresetType
from .base   import BaseObject
from typing  import *


class TriggerMetadataObject(BaseObject):
  allow_list                      : List[str] = []
  keyword_filter                  : List[str] = []
  mention_raid_protection_enabled : bool = False
  mention_total_limit             : int
  presets                         : List[int] = []
  regex_patterns                  : List[str] = []