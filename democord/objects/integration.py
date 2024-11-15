from ..types import (
                    ISO8601Timestamp,
                    Snowflake
                    )
from .base   import BaseObject
from typing  import *


class IntegrationObject(BaseObject):
  from .integration_account     import IntegrationAccountObject
  from .integration_application import IntegrationApplicationObject
  from .user                    import UserObject

  account             : IntegrationAccountObject
  application         : Optional[IntegrationApplicationObject]
  enabled             : bool
  enable_emoticons    : Optional[bool]
  expire_behavior     : Optional[int]
  expire_grace_period : Optional[int]
  id                  : Snowflake
  name                : str
  revoked             : Optional[bool]
  role_id             : Optional[Snowflake]
  scopes              : List[str]                              = []
  subscriber_count    : Optional[int]
  synced_at           : Optional[ISO8601Timestamp]
  syncing             : Optional[bool]
  type                : str
  user                : Optional[UserObject]