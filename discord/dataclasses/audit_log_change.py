from typing import Any, Optional


class AuditLogChange(dict):
  def __init__(self, data: dict[str, ...]) -> None:
    self.__data: dict[str, ...] = data


  @property
  def key(self) -> str:
    return self.__data["key"]


  @property
  def new_value(self) -> Optional[Any]:
    return self.__data.get("new_value")


  @property
  def old_value(self) -> Optional[Any]:
    return self.__data.get("old_value")