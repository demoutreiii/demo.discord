from ..enums import EmbedType
from ..exceptions import DiscordLimitExceeded
from .embed_author import EmbedAuthor
from .embed_field import EmbedField
from .embed_footer import EmbedFooter
from .embed_image import EmbedImage
from .embed_thumbnail import EmbedThumbnail
from .embed_provider import EmbedProvider
from .embed_video import EmbedVideo
from datetime import datetime
from typing import Optional, Self


class Embed(dict):
  @property
  def author(self) -> EmbedAuthor:
    return EmbedAuthor(self["author"] if "author" in self else {})


  @author.setter
  def icon_url(self, value: Optional[str]) -> Optional[str]:
    if value is None and self.author.icon_url is not None: del self["author"]["icon_url"]
    else: self["author"]["icon_url"]: Optional[str] = value if isinstance(value, str) else self.author.icon_url
    return self.author.icon_url


  @author.setter
  def name(self, value: Optional[str]) -> str:
    self["author"]["name"]: str = value if value is not None and isinstance(value, str) else str()
    return self.author.name


  @author.setter
  def url(self, value: Optional[str]) -> Optional[str]:
    if value is None and self.author.url is not None: del self["author"]["url"]
    else: self["author"]["url"]: Optional[str] = value if isinstance(value, str) else self.author.url
    return self.author.url
  
  
  @property
  def color(self) -> Optional[int]:
    return self["color"] if "color" in self else None


  @color.setter
  def color(self, value: Optional[int]) -> Optional[int]:
    self["color"]: Optional[int] = value if isinstance(value, int) else self.color
    return self.color
  
  
  @property
  def description(self) -> Optional[str]:
    return self["description"] if "description" in self else None


  @description.setter
  def description(self, value: Optional[str]) -> Optional[str]:
    self["description"]: Optional[str] = value if isinstance(value, str) else self.description
    return self.description


  @property
  def fields(self) -> list[EmbedField]:
    return [EmbedField(data) for data in (self["fields"] if "fields" in self else [])]


  @property
  def footer(self) -> EmbedFooter:
    return EmbedFooter(self["footer"] if "footer" in self else {})


  @footer.setter
  def icon_url(self, value: Optional[str]) -> Optional[str]:
    if value is None and self.footer.icon_url is not None: del self["footer"]["icon_url"]
    else: self["footer"]["icon_url"]: Optional[str] = value if isinstance(value, str) else self.footer.icon_url
    return self.footer.icon_url


  @footer.setter
  def text(self, value: str) -> str:
    self["footer"]["text"]: str = value if isinstance(value, str) else self.footer.text
    return self.footer.text


  @property
  def image(self) -> EmbedImage:
    return EmbedImage(self["image"] if "image" in self else {})


  @image.setter
  def url(self, value: Optional[str]) -> str:
    self["image"]["url"]: str = value if value is not None and isinstance(value, str) else str()
    return self.image.url


  @property
  def provider(self) -> EmbedProvider:
    return EmbedProvider(self["provider"] if "provider" in self else {})
  
  
  @property
  def thumbnail(self) -> EmbedThumbnail:
    return EmbedThumbnail(self["thumbnail"] if "thumbnail" in self else {})


  @thumbnail.setter
  def url(self, value: Optional[str]) -> str:
    self["thumbnail"]["url"]: str = value if value is not None and isinstance(value, str) else str()
    return self.thumbnail.url
  
  
  @property
  def timestamp(self) -> Optional[datetime]:
    return datetime.fromisoformat(self["timestamp"]) if "timestamp" in self else None


  @timestamp.setter
  def timestamp(self, value: Optional[datetime]) -> Optional[datetime]:
    self["timestamp"]: Optional[str] = value.isoformat() if value is not None and isinstance(value, datetime) else None
    return self.timestamp
  
  
  @property
  def title(self) -> Optional[str]:
    return self["title"] if "title" in self else None


  @title.setter
  def title(self, value: Optional[str]) -> Optional[str]:
    self["title"]: Optional[str] = value if isinstance(value, str) else self.title
    return self.title


  @property
  def type(self) -> EmbedType:
    return EmbedType(self["type"]) if "type" in self else None


  @property
  def url(self) -> Optional[str]:
    return self["url"] if "url" in self else None


  @url.setter
  def url(self, value: Optional[str]) -> Optional[str]:
    self["url"]: Optional[str] = value if isinstance(value, str) else self.url
    return self.url


  @property
  def video(self) -> EmbedVideo:
    return EmbedVideo(self["video"] if "video" in self else {})


  @video.setter
  def url(self, value: Optional[str]) -> Optional[str]:
    if value is None and self.video.url is not None: del self["video"]["url"]
    else: self["video"]["url"]: Optional[str] = value if isinstance(value, str) else None
    return self.video.url