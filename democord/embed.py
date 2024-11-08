from .color       import Color
from .constructor import Constructor
from .enums       import EmbedType
from .errors      import APILimit
from .logger      import Logger
from .types       import ObjectPayload
from datetime     import datetime
from typing       import *

if TYPE_CHECKING:
  from .objects   import (
                         EmbedAuthorObject,
                         EmbedFieldObject,
                         EmbedFooterObject,
                         EmbedImageObject,
                         EmbedProviderObject,
                         EmbedThumbnailObject,
                         EmbedVideoObject,
                         EmbedObject
                         )


class EmbedAuthor:
  @property
  def icon_url(self) -> Optional[str]:
    return self["icon_url"]

  @property
  def name(self) -> Optional[str]:
    return self["name"]

  @property
  def proxy_icon(self) -> Optional[str]:
    return self["proxy_icon_url"]

  @property
  def url(self) -> Optional[str]:
    return self["url"]


class EmbedField:
  @property
  def inline(self) -> bool:
    return self["inline"]

  @property
  def name(self) -> str:
    return self["name"]

  @property
  def value(self) -> str:
    return self["value"]


class EmbedFooter:
  @property
  def text(self) -> Optional[str]:
    return self["text"]

  @property
  def icon_url(self) -> Optional[str]:
    return self["icon_url"]

  @property
  def proxy_icon(self) -> Optional[str]:
    return self["proxy_icon_url"]


class EmbedImage:
  @property
  def height(self) -> int:
    return self["height"]

  @property
  def proxy_url(self) -> Optional[str]:
    return self["proxy_url"]

  @property
  def url(self) -> str:
    return self["url"]

  @property
  def width(self) -> int:
    return self["width"]


class EmbedProvider:
  @property
  def name(self) -> str:
    return self["name"]

  @property
  def url(self) -> str:
    return self["url"]


class EmbedThumbnail:
  @property
  def height(self) -> int:
    return self["height"]

  @property
  def proxy_url(self) -> Optional[str]:
    return self["proxy_url"]

  @property
  def url(self) -> str:
    return self["url"]

  @property
  def width(self) -> int:
    return self["width"]


class EmbedVideo:
  @property
  def height(self) -> int:
    return self["height"]

  @property
  def proxy_url(self) -> Optional[str]:
    return self["proxy_url"]

  @property
  def url(self) -> str:
    return self["url"]

  @property
  def width(self) -> int:
    return self["width"]


class EmbedMeta(type):
  def __instancecheck__(cls, instance : Any) -> bool:
    from .objects import EmbedObject
    return instance.__class__ == EmbedObject


class Embed(metaclass = EmbedMeta):
  def __new__(
    cls,
    color       : Optional[Union[Color, str, int]] = 0,
    description : Optional[str]                    = None,
    timestamp   : Optional[datetime]               = None,
    title       : Optional[str]                    = None,
    url         : Optional[str]                    = None
  ) -> Self:
    from .objects import EmbedObject
    return dict.__new__(EmbedObject)

  def __init__(
    self,
    color       : Optional[Union[Color, int]] = 0,
    description : Optional[str]                    = None,
    timestamp   : Optional[datetime]               = None,
    title       : Optional[str]                    = None,
    url         : Optional[str]                    = None
  ) -> NoReturn:
    from .constructor import Constructor
    logger = Constructor.ws.app.logger
    try:
      if not isinstance(timestamp, datetime):
        raise TypeError("timestamp: must be of type <datetime.datetime> object")
      if not isinstance(color, (Color, int)):
        raise TypeError("color: must be of type <Color> or <int>")
      data : ObjectPayload = {
        "color"       : int(color),
        "description" : str(description),
        "timestamp"   : timestamp.isoformat(),
        "title"       : str(title),
        "url"         : str(url)
      }
      self.update(Constructor.embed(data))
    except Exception as error:
      if logger: logger.error(error)

  @property
  def author(self) -> "EmbedAuthorObject":
    return self["author"]

  @property
  def color(self) -> Color:
    return Color.from_int(self["color"])

  @property
  def description(self) -> Optional[str]:
    return self["description"]

  @property
  def fields(self) -> List["EmbedFieldObject"]:
    return self["fields"]

  @property
  def footer(self) -> Optional["EmbedFooterObject"]:
    return self["footer"]

  @property
  def image(self) -> Optional["EmbedImageObject"]:
    return self["image"]

  @property
  def provider(self) -> Optional["EmbedProviderObject"]:
    return self["provider"]

  @property
  def thumbnail(self) -> Optional["EmbedThumbnailObject"]:
    return self["thumbnail"]

  @property
  def timestamp(self) -> Optional[datetime]:
    if not self["timestamp"]: return None
    return datetime.fromisoformat(self["timestamp"])

  @property
  def title(self) -> Optional[str]:
    return self["title"]

  @property
  def type(self) -> EmbedType:
    return EmbedType(self["type"])

  @property
  def url(self) -> Optional[str]:
    return self["url"]

  @property
  def video(self) -> Optional["EmbedVideoObject"]:
    return self["video"]

  async def add_field(
    self,
    *,
    name   : str,
    value  : str,
    inline : Optional[bool] = False
  ) -> NoReturn:
    from .objects import EmbedFIeldObject
    try:
      if len(self.fields) == 25:
        raise Constructor.exception(APILimit, message = "can only append 25 fields per embed")
      if not isinstance(inline, bool):
        raise TypeError("inline: must be of type <bool>")
      self.fields.append(
        EmbedFieldObject(
          {
            "name"   : str(name),
            "value"  : str(value),
            "inline" : inline
          }
        )
      )
    except Exception as error:
      if Logger.initiated: Logger.error(error)

  async def clear_fields(self) -> NoReturn:
    try:
      self.fields.clear()
    except Exception as error:
      if Logger.initiated: Logger.error(error)

  async def copy(self) -> "EmbedObject":
    return self.copy()

  async def insert_field(
    self,
    index  : int,
    *,
    name   : str,
    value  : str,
    inline : Optional[bool] = False
  ) -> NoReturn:
    from .objects import EmbedFieldObject
    try:
      if len(self.fields) == 25:
        raise Constructor.exception(APILimit, message = "can only append 25 fields per embed")
      if not isinstance(index, int):
        raise TypeError("index: must be of type <int>")
      if not isinstance(inline, bool):
        raise TypeError("inline: must be of type <bool>")
      self.fields.insert(
        index,
        EmbedFieldObject(
          {
            "name"   : name,
            "value"  : value,
            "inline" : inline
          }
        )
      )
    except Exception as error:
      if Logger.initiated: Logger.error(error)

  async def remove_author(self) -> NoReturn:
    from .objects import EmbedAuthorObject
    try:
      self["author"] : ObjectPayload = EmbedAuthorObject()
    except Exception as error:
      if Logger.initiated: Logger.error(error)

  async def remove_field(
    self,
    index : int = -1
  ) -> NoReturn:
    try:
      if not isinstance(index, int):
        raise TypeError("index: must be of type <int>")
      if (index < 0 and -index > len(self.fields)) or (index >= 0 and index + 1 > len(self.fields)):
        raise ValueError(f"index: must be between {-len(self.fields)} and {len(self.fields)}")
      self.fields.pop(index)
    except Exception as error:
      if Logger.initiated: Logger.error(error)

  async def remove_footer(self) -> NoReturn:
    from .objects import EmbedFooterObject
    try:
      self["footer"] : ObjectPayload = EmbedFooterObject()
    except Exception as error:
      if Logger.initiated: Logger.error(error)

  async def remove_image(self) -> NoReturn:
    from .objects import EmbedImageObject
    try:
      self["image"] : ObjectPayload = EmbedImageObject()
    except Exception as error:
      if Logger.initiated: Logger.error(error)

  async def remove_thumbnail(self) -> NoReturn:
    from .objects import EmbedThumbnailObject
    try:
      self["thumbnail"] = ObjectPayload = EmbedThumbnailObject()
    except Exception as error:
      if Logger.initiated: Logger.error(error)

  async def set_author(
    self,
    *,
    name       : str,
    icon_url   : Optional[str] = None,
    url        : Optional[str] = None
  ) -> NoReturn:
    try:
      self["author"].update(
        {
          "icon_url"       : str(icon_url),
          "name"           : str(name),
          "url"            : str(url)
        }
      )
    except Exception as error:
      if Logger.initiated: Logger.error(error)

  async def set_field(
    self,
    index  : int,
    *,
    name   : Optional[int]  = None,
    value  : Optional[int]  = None,
    inline : Optional[bool] = None
  ) -> NoReturn:
    try:
      if not isinstance(index, int):
        raise TypeError("index: must be of type <int>")
      if (index < 0 and -index > len(self.fields)) or (index >= 0 and index + 1 > len(self.fields)):
        raise ValueError(f"index: must be between {-len(self.fields)} and {len(self.fields)}")
      sample[index] : ObjectPayload = {
        "name"   : name if name is not None else self.fields[index].name,
        "value"  : value if value is not None else self.fields[index].value,
        "inline" : inline if inline is not None else self.fields[index].inline
      }
    except Exception as error:
      if Logger.initiated: Logger.error(error)

  async def set_footer(
    self,
    *,
    text       : str,
    icon_url   : str
  ) -> NoReturn:
    try:
      self["footer"].update(
        {
          "text"           : str(text),
          "icon_url"       : str(icon_url)
        }
      )
    except Exception as error:
      if Logger.initiated: Logger.error(error)

  async def set_image(
    self,
    *,
    url : str
  ) -> NoReturn:
    try:
      self["image"].update(
        {
          "url" : url
        }
      )
    except Exception as error:
      if Logger.initiated: Logger.error(error)

  async def set_thumbnail(
    self,
    *,
    url : str
  ) -> NoReturn:
    try:
      self.thumbnail.update(
        {
          "url" : str(url)
        }
      )
    except Exception as error:
      if Logger.initiated: Logger.error(error)