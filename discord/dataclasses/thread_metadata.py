from typing import Optional


class ThreadMetadata(dict):
  def __init__(self, data: dict[str, ...]) -> None:
    self.__data: dict[str, ...] = data


  @property
  def archived(self) -> bool:
    return self.__data["archived"]


  @property
  def archive_tiemstamp(self) -> int:
    return self.__data["archive_timestamp"]


  @property
  def auto_archive_duration(self) -> int:
    return self.__data["auto_archive_duration"]


  @property
  def create_timestamp(self) -> Optional[int]:
    return self.__data.get("create_timestamp")


  @property
  def invitable(self) -> bool:
    return self.__data.get("invitable", False)


  @property
  def locked(self) -> bool:
    return self.__data["locked"]