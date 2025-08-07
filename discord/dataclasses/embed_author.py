from typing import Optional


class EmbedAuthor(dict):
  @property
  def icon_url(self) -> Optional[str]:
    return self["icon_url"] if "icon_url" in self else None


  @icon_url.setter
  def icon_url(self, value: Optional[str]) -> Optional[str]:
    if value is None and self.icon_url is not None: del self["icon_url"]
    else: self["icon_url"]: Optional[str] = value
    return self.icon_url
  
  
  @property
  def name(self) -> str:
    return self["name"]


  @name.setter
  def name(self, value: Optional[str]) -> str:
    self["name"]: str = value if value is not None else str()
    return self.name


  @property
  def proxy_icon_url(self) -> Optional[str]:
    return self["proxy_icon_url"] if "proxy_icon_url" in self else None


  @property
  def url(self) -> Optional[str]:
    return self["url"] if "url" in self else None


  @url.setter
  def url(self, value: Optional[str]) -> Optional[str]:
    if value is None and self.url is not None: del self["url"]
    else: self["url"]: Optional[str] = value
    return self.url