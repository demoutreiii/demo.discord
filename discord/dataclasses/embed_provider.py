from typing import Optional


class EmbedProvider(dict):
  @property
  def name(self) -> Optional[str]:
    return self["name"] if "name" in self else None


  @property
  def url(self) -> Optional[str]:
    return self["url"] if "url" in self else None