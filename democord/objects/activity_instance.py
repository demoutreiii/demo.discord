from ..types import Snowflake
from .base   import BaseObject
from typing  import *


class ActivityInstanceObject(BaseObject):
  from .activity_location import ActivityLocationObject

  application_id : Snowflake
  instance_id    : str
  launch_id      : Snowflake
  location       : ActivityLocationObject
  users          : List[Snowflake]        = []