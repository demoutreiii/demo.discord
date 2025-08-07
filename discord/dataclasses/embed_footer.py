from typing import Optional


class EmbedFooter(dict):
  @property
  def icon_url(self) -> Optional[str]:
    return self["icon_url"] if "icon_url" in self else None


  @property
  def proxy_icon_url(self) -> Optional[str]:
    return self["proxy_icon_url"] if "proxy_icon_url" in self else None
  
  
  @property
  def text(self) -> str:
    return self["text"]