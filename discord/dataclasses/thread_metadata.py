from typing import Optional


class ThreadMetadata(dict):
  @property
  def archived(self) -> bool:
    return self["archived"]


  @property
  def archive_tiemstamp(self) -> int:
    return self["archive_timestamp"]


  @property
  def auto_archive_duration(self) -> int:
    return self["auto_archive_duration"]


  @property
  def create_timestamp(self) -> Optional[int]:
    return self.get("create_timestamp")


  @property
  def invitable(self) -> bool:
    return self.get("invitable", False)


  @property
  def locked(self) -> bool:
    return self["locked"]