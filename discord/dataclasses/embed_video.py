from typing import Optional


class EmbedVideo(dict):
  @property
  def height(self) -> Optional[int]:
    return self["height"] if "height" in self else None
  
  
  @property
  def proxy_url(self) -> Optional[str]:
    return self["proxy_url"] if "proxy_url" in self else None
  
  
  @property
  def url(self) -> Optional[str]:
    return self["url"] if "url" in self else None


  @url.setter
  def url(self, value: Optional[str]) -> Optional[str]:
    if value is None and self.url is not None: del self["url"]
    else: self["url"]: Optional[str] = value
    return self.url


  @property
  def width(self) -> Optional[int]:
    return self["width"] if "width" in self else None