from ..embed import (
                    Embed,
                    EmbedAuthor,
                    EmbedField,
                    EmbedFooter,
                    EmbedImage,
                    EmbedProvider,
                    EmbedThumbnail,
                    EmbedVideo
                    )
from ..types import (
                    ISO8601Timestamp,
                    Snowflake
                    )
from .base   import BaseObject
from typing  import *


class EmbedAuthorObject(BaseObject, EmbedAuthor):
  icon_url       : str
  name           : str
  proxy_icon_url : str
  url            : str


class EmbedFieldObject(BaseObject, EmbedField):
  inline : bool = False
  name   : str
  value  : str


class EmbedFooterObject(BaseObject, EmbedFooter):
  text           : str
  icon_url       : str
  proxy_icon_url : str


class EmbedImageObject(BaseObject, EmbedImage):
  height    : int
  proxy_url : str
  url       : str
  width     : int


class EmbedProviderObject(BaseObject, EmbedProvider):
  name : str
  url  : str


class EmbedThumbnailObject(BaseObject, EmbedThumbnail):
  height    : int
  proxy_url : str
  url       : str
  width     : int


class EmbedVideoObject(BaseObject, EmbedVideo):
  height    : int
  proxy_url : str
  url       : str
  width     : int


class EmbedObject(BaseObject, Embed):
  author      : EmbedAuthorObject
  color       : int                    = 0
  description : str
  fields      : List[EmbedFieldObject] = []
  footer      : EmbedFooterObject
  image       : EmbedImageObject
  provider    : EmbedProviderObject
  thumbnail   : EmbedThumbnailObject
  timestamp   : ISO8601Timestamp
  title       : str
  type        : str                    = "rich"
  url         : str
  video       : EmbedVideoObject