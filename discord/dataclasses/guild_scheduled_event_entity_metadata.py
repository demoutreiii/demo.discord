from typing import Optional


class GuildScheduledEventEntityMetadata(dict):
  @property
  def location(self) -> Optional[str]:
    return self.get("location")