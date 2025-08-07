from typing import Optional


class EmbedImage(dict):
  @property
  def height(self) -> Optional[int]:
    return self["height"] if "height" in self else None
  
  
  @property
  def proxy_url(self) -> Optional[str]:
    return self["proxy_url"] if "proxy_url" in self else None
  
  
  @property
  def url(self) -> str:
    return self["url"]


  @url.setter
  def url(self, value: Optional[str]) -> str:
    self["url"]: str = value if value is not None else str()
    return self.url


  @property
  def width(self) -> Optional[int]:
    return self["width"] if "width" in self else None