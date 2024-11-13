from ..types import Snowflake
from .base   import BaseObject
from typing  import *


class UnavailableGuildObject(BaseObject):
  id          : Snowflake
  unavailable : bool = True