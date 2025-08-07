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
  
  
  @property
  def color(self) -> Optional[int]:
    return self["color"] if "color" in self else None
  
  
  @property
  def description(self) -> Optional[str]:
    return self["description"] if "description" in self else None


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
  
  
  @property
  def title(self) -> Optional[str]:
    return self["title"] if "title" in self else None


  @property
  def type(self) -> EmbedType:
    return EmbedType(self["type"]) if "type" in self else None


  @property
  def url(self) -> Optional[str]:
    return self["url"] if "url" in self else None


  @property
  def video(self) -> EmbedVideo:
    return EmbedVideo(self["video"] if "video" in self else {})


  @author.setter
  def icon_url(self, value: Optional[str]) -> Optional[str]:
    if value is None and self.author.icon_url is not None: del self["author"]["icon_url"]
    else:
      assert isinstance(value, str), f"Author Icon URL must be of a string, not {value.__class__.__name__}"
      self["author"]["icon_url"]: Optional[str] = value
    return self.author.icon_url


  @author.setter
  def name(self, value: Optional[str]) -> str:
    if value is not None and isinstance(value, str) and 256 < len(value): raise DiscordLimitExceeded("Embed.author.name: Maximum of 256 characters.")
    self["author"]["name"]: str = value if value is not None and isinstance(value, str) else str()
    return self.author.name


  @author.setter
  def url(self, value: Optional[str]) -> Optional[str]:
    if value is None and self.author.url is not None: del self["author"]["url"]
    else:
      assert isinstance(value, str), f"Author URL must be of a string, not {value.__class__.__name__}"
      self["author"]["url"]: Optional[str] = value
    return self.author.url


  @color.setter
  def color(self, value: Optional[int]) -> Optional[int]:
    if value is not None: assert isinstance(value, int), f"Color must be of a string, not {value.__class__.__name__}"
    self["color"]: Optional[int] = value
    return self.color


  @description.setter
  def description(self, value: Optional[str]) -> Optional[str]:
    if value is not None:
      assert isinstance(value, str), f"Description must be of a string, not {value.__class__.__name__}"
      if 4_096 < len(value): raise DiscordLimitExceeded("Embed.description: Maximum of 4,096 characters.")
    self["description"]: Optional[str] = value
    return self.description


  @footer.setter
  def icon_url(self, value: Optional[str]) -> Optional[str]:
    if value is None and self.footer.icon_url is not None: del self["footer"]["icon_url"]
    else:
      assert isinstance(value, str), f"Footer Icon URL must be of a string, not {value.__class__.__name__}"
      self["footer"]["icon_url"]: Optional[str] = value
    return self.footer.icon_url


  @footer.setter
  def text(self, value: Optional[str]) -> str:
    if text is not None:
      assert isinstance(value, str), f"Footer text must be of a string, not {value.__class__.__name__}"
      if 2_048 < len(value): raise DiscordLimitExceeded("Embed.footer.text: Maximum of 2,048 characters.")
    self["footer"]["text"]: str = value if value is not None else str()
    return self.footer.text


  @image.setter
  def url(self, value: Optional[str]) -> str:
    self["image"]["url"]: str = value if value is not None and isinstance(value, str) else str()
    return self.image.url


  @thumbnail.setter
  def url(self, value: Optional[str]) -> str:
    self["thumbnail"]["url"]: str = value if value is not None and isinstance(value, str) else str()
    return self.thumbnail.url


  @timestamp.setter
  def timestamp(self, value: Optional[datetime]) -> Optional[datetime]:
    if value is not None:
      assert isinstance(value, datetime), f"Timestamp must be of a datetime.datetime object, not {value.__class__.__name__}"
      self["timestamp"]: Optional[str] = value.isoformat()
    else: self["timestamp"]: Optional[str] = None
    return self.timestamp


  @title.setter
  def title(self, value: Optional[str]) -> Optional[str]:
    if value is not None:
      assert isinstance(value, str), f"Title must be of a string, not {value.__class__.__name__}"
      if 256 < len(value): raise DiscordLimitExceeded("Embed.title: Maximum of 256 characters.")
    self["title"]: Optional[str] = value
    return self.title


  @url.setter
  def url(self, value: Optional[str]) -> Optional[str]:
    if value is not None:
      assert isinstance(value, str), f"URL must be of a string, not {value.__class__.__name__}"
    self["url"]: Optional[str] = value
    return self.url


  @video.setter
  def url(self, value: Optional[str]) -> Optional[str]:
    if value is None and self.video.url is not None: del self["video"]["url"]
    else:
      assert isinstance(value, str), f"Video URL must be of a string, not {value.__class__.__name__}"
      self["video"]["url"]: Optional[str] = value
    return self.video.url


  def add_field(self, *, name: str, value: str, inline: Optional[bool] = False) -> Self:
    if len(self.fields) == 25:
      raise DiscordLimitExceeded("Maximum of 25 fields per embed.")
    assert isinstance(name, str), f"Field name must be of a string, not {name.__class__.__name__}"
    assert isinstance(value, str), f"Field value must be of a string, not {value.__class__.__name__}"
    assert isinstance(inline, bool), f"Field inline must be of a boolean, not {inline.__class__.__name__}"
    if 256 < len(name): raise DiscordLimitExceeded(f"Embed.fields[{len(self.fields)}].name: Maximum of 256 characters.")
    if 1_024 < len(value): raise DiscordLimitExceeded(f"Embed.fields[{len(self.fields)}].value: Maximum of 1,024 characters.")
    field_data: dict[str, Union[str, bool]] = {
      "name": name,
      "value": value,
      "inline": inline
    }
    if "fields" not in self: self["fields"]: list[dict[str, Union[str, bool]]] = []
    self["fields"].append(field_data)
    return self


  def edit_field(self, index: int, *, name: str = ..., value: str = ..., inline: Optional[bool] = ...) -> Self:
    if (index < 0 and abs(index) > len(self.fields)) or (0 <= index and len(self.fields) <= index): raise IndexError("list index out of range.")
    assert any(argument for argument in [name, value, inline] if argument is not Ellipsis), "One of 'name', 'value', and 'inline' arguments must be passed and specified."
    if name is not Ellipsis:
      assert isinstance(name, str), f"Field name must be of a string, not {name.__class__.__name__}"
      if 256 < len(name): raise DiscordLimitExceeded(f"Embed.fields[{len(self.fields)}].name: Maximum of 256 characters.")
      self["fields"][index]["name"]: str = name
    if value is not Ellipsis:
      assert isinstance(value, str), f"Field value must be of a string, not {value.__class__.__name__}"
      if 1_024 < len(value): raise DiscordLimitExceeded(f"Embed.fields[{len(self.fields)}].value: Maximum of 1,024 characters.")
      self["fields"][index]["value"]: str = value
    if inline is not Ellipsis:
      assert isinstance(inline, bool), f"Field inline must be of a boolean, not {inline.__class__.__name__}"
      self["fields"][index]["inline"]: bool = inline
    return self


  def insert_field(self, index: int, *, name: str, value: str, inline: Optional[bool] = False) -> Self:
    if len(self.fields) == 25:
      raise DiscordLimitExceeded("Maximum of 25 fields per embed.")
    assert isinstance(name, str), f"Field name must be of a string, not {name.__class__.__name__}"
    assert isinstance(value, str), f"Field value must be of a string, not {value.__class__.__name__}"
    assert isinstance(inline, bool), f"Field inline must be of a boolean, not {inline.__class__.__name__}"
    if 256 < len(name): raise DiscordLimitExceeded(f"Embed.fields[{len(self.fields)}].name: Maximum of 256 characters.")
    if 1_024 < len(value): raise DiscordLimitExceeded(f"Embed.fields[{len(self.fields)}].value: Maximum of 1,024 characters.")
    field_data: dict[str, Union[str, bool]] = {
      "name": name,
      "value": value,
      "inline": inline
    }
    if "fields" not in self: self["fields"]: list[dict[str, Union[str, bool]]] = []
    self["fields"].insert(index, field_data)
    return self
  
  
  def remove_field(self, index: int = -1) -> Self:
    if len(self["fields"]) == 0: raise IndexError("Empty fields list")
    assert isinstance(index, int), f"Index must be of an integer, not {index.__class__.__name__}"
    if len(self["fields"]) == 1: del self["fields"]
    else: self["fields"].remove(index)
    return self