from ..message import Message
from ..types   import (
                      ISO8601Timestamp,
                      Snowflake
                      )
from .base     import BaseObject


class MessageObject(BaseObject, Message):
  from .application            import ApplicationObject
  from .attachment             import AttachmentObject
  from .channel                import ChannelObject
  from .channel_mention        import ChannelMentionObject
  from .component              import ComponentObject
  from .embed                  import EmbedObject
  from .interaction_metadata   import MessageInteractionMetadataObject
  from .message_activity       import MessageActivityObject
  from .message_call           import MessageCallObject
  from .message_reference      import MessageReferenceObject
  from .message_snapshot       import MessageSnapshotObject
  from .poll                   import PollObject
  from .reaction               import ReactionObject
  from .role                   import RoleObject
  from .sticker_item           import StickerItemObject
  from .resolved               import ResolvedObject
  from .role_subscription_data import RoleSubscriptionDataObject
  from .user                   import UserObject

  application            : Optional[ApplicationObject]
  application_id         : Optional[Snowflake]
  attachments            : List[AttachmentObject]                     = []
  author                 : UserObject
  call                   : Optional[MessageCallObject]
  channel_id             : Snowflake
  components             : List[ComponentObject]                      = []
  content                : str
  edited_timestamp       : Optional[ISO8601Timestamp]
  embeds                 : List[EmbedObject]                          = []
  flags                  : int                                        = 0
  id                     : Snowflake
  interaction_metadata   : Optional[MessageInteractionMetadataObject]
  message_activity       : Optional[MessageActivityObject]
  mention_channels       : List[ChannelMentionObject]                 = []
  mention_everyone       : bool                                       = False
  mention_roles          : List[RoleObject]                           = []
  mentions               : List[UserObject]                           = []
  message_reference      : Optional[MessageReferenceObject]
  message_snapshots      : List[MessageSnapshotObject]                = []
  nonce                  : Optional[Union[int, str]]
  pinned                 : bool                                       = False
  poll                   : Optional[PollObject]
  position               : Optional[int]
  reactions              : List[ReactionObject]                       = []
  referenced_message     : Optional[MessageObject]
  resolved               : Optional[ResolvedObject]
  role_subscription_data : Optional[RoleSubscriptionDataObject]
  sticker_items          : List[StickerItem]                          = []
  thread                 : Optional[ChannelObject]
  timestamp              : ISO8601Timestamp
  tts                    : bool                                       = False
  type                   : int
  webhook_id             : Optional[Snowflake]