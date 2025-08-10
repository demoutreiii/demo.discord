from ..flags import AttachmentFlag
from .snowflake import Snowflake
from typing import Optional


class Attachment(dict):
  @property
  def content_type(self) -> Optional[str]:
    return self["content_type"] if "content_type" in self else None
  
  
  @property
  def description(self) -> Optional[str]:
    return self["description"] if "description" in self else None
  
  
  @property
  def duration_secs(self) -> Optional[float]:
    return self["duration_secs"] if "duration_secs" in self else None
  
  
  @property
  def ephemeral(self) -> Optional[bool]:
    return self["ephemeral"] if "ephemeral" in self else None
  
  
  @property
  def filename(self) -> str:
    return self["filename"]


  @property
  def flags(self) -> Optional[AttachmentFlag]:
    return AttachmentFlag(self["flags"]) if "flags" in self else None
  
  
  @property
  def height(self) -> Optional[int]:
    return self.get("height")
  
  
  @property
  def id(self) -> Snowflake:
    return Snowflake(self["id"])


  @property
  def proxy_url(self) -> str:
    return self["proxy_url"]


  @property
  def size(self) -> int:
    return self["size"]


  @property
  def title(self) -> Optional[str]:
    return self["title"] if "title" in self else None


  @property
  def url(self) -> str:
    return self["url"]


  @property
  def waveform(self) -> Optional[str]:
    return self["waveform"] if "waveform" in self else None


  @property
  def width(self) -> Optional[int]:
    return self.get("width")