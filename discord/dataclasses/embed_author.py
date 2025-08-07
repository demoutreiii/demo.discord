from typing import Optional


class EmbedAuthor(dict):
  @property
  def icon_url(self) -> Optional[str]:
    return self["icon_url"] if "icon_url" in self else None
  
  
  @property
  def name(self) -> str:
    return self["name"]


  @property
  def proxy_icon_url(self) -> Optional[str]:
    return self["proxy_icon_url"] if "proxy_icon_url" in self else None


  @property
  def url(self) -> Optional[str]:
    return self["url"] if "url" in self else None