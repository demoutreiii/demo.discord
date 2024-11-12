from ..types import ISO8601Timestamp
from .base   import BaseObject
from typing  import *


class ThreadMetadataObject(BaseObject):
  archived              : bool
  archive_timestamp     : ISO8601Timestamp
  auto_archive_duration : int
  create_timestamp      : Optional[ISO8601Timestamp]
  invitable             : Optional[bool]
  locked                : bool