from ..message import Message
from ..types   import (
                      ISO8601Timestamp,
                      Snowflake
                      )
from .base     import BaseObject


class MessageObject(BaseObject, Message):
  id : Snowflake