from ..types import Snowflake
from .base   import BaseObject
from typing  import *


class OverwriteObject(BaseObject):
  allow : str
  deny  : str
  id    : Snowflake
  type  : int