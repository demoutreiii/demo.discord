from ..enums import EmbedType
from .embed_author import EmbedAuthor
from .embed_field import EmbedField
from .embed_footer import EmbedFooter
from .embed_image import EmbedImage
from .embed_thumbnail import EmbedThumbnail
from .embed_provider import EmbedProvider
from .embed_video import EmbedVideo
from datetime import datetime
from typing import Optional


class Embed(dict):
  @property
  def author(self) -> EmbedAuthor:
    return EmbedAuthor(self["author"] if "author" in self else {})
  
  
  @property
  def color(self) -> Optional[int]:
    return self["color"] if "color" in self else None


  @color.setter
  def color(self, value: Optional[int]) -> Optional[int]:
    self["color"]: Optional[int] = value
    return self.color
  
  
  @property
  def description(self) -> Optional[str]:
    return self["description"] if "description" in self else None


  @description.setter
  def description(self, value: Optional[str]) -> Optional[str]:
    self["description"]: Optional[str] = value
    return self.description


  @property
  def fields(self) -> list[EmbedField]:
    return [EmbedField(data) for data in (self["fields"] if "fields" in self else [])]


  @property
  def footer(self) -> EmbedFooter:
    return EmbedFooter(self["footer"] if "footer" in self else {})


  @property
  def image(self) -> EmbedImage:
    return EmbedImage(self["image"] if "image" in self else {})


  @property
  def provider(self) -> EmbedProvider:
    return EmbedProvider(self["provider"] if "provider" in self else {})
  
  
  @property
  def thumbnail(self) -> EmbedThumbnail:
    return EmbedThumbnail(self["thumbnail"] if "thumbnail" in self else {})
  
  
  @property
  def timestamp(self) -> Optional[datetime]:
    return datetime.fromisoformat(self["timestamp"]) if "timestamp" in self else None


  @timestamp.setter
  def timestamp(self, value: Optional[datetime]) -> Optional[datetime]:
    self["timestamp"]: Optional[str] = value.isoformat() if value is not None else None
    return self.timestamp
  
  
  @property
  def title(self) -> Optional[str]:
    return self["title"] if "title" in self else None


  @title.setter
  def title(self, value: Optional[str]) -> Optional[str]:
    self["title"]: Optional[str] = value
    return self.title


  @property
  def type(self) -> EmbedType:
    return EmbedType(self["type"]) if "type" in self else None


  @property
  def url(self) -> Optional[str]:
    return self["url"] if "url" in self else None


  @url.setter
  def url(self, value: Optional[str]) -> Optional[str]:
    self["url"]: Optional[str] = value
    return self.url


  @property
  def video(self) -> EmbedVideo:
    return EmbedVideo(self["video"] if "video" in self else {})