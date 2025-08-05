from datetime import datetime
from typing import Optional


class ThreadMetadata(dict):
  @property
  def archived(self) -> bool:
    return self["archived"]


  @property
  def archive_tiemstamp(self) -> datetime:
    return datetime.fromisoformat(self["archive_timestamp"])


  @property
  def auto_archive_duration(self) -> int:
    return self["auto_archive_duration"]


  @property
  def create_timestamp(self) -> Optional[datetime]:
    return datetime.fromisoformat(self.get("create_timestamp")) if self.get("create_timestamp") is not None else None


  @property
  def invitable(self) -> bool:
    return self.get("invitable", False)


  @property
  def locked(self) -> bool:
    return self["locked"]