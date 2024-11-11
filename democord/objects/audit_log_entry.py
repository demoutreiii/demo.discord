from ..enums import AuditLogEvent
from ..types import Snowflake
from .base   import BaseObject
from typing  import *


class AuditLogEntryObject(BaseObject):
  from .audit_log_change import AuditLogChangeObject
  from .audit_entry_info import OptionalAuditEntryInfoObject
  
  action_type : int
  changes     : List[AuditLogChangeObject] = []
  id          : Snowflake
  options     : Optional[OptionalAuditEntryInfoObject]
  reason      : Optional[str]
  target_id   : Optional[str]
  user_id     : Optional[Snowflake]