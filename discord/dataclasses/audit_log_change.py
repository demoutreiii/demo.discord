from typing import Any, Optional


class AuditLogChange(dict):
  @property
  def key(self) -> str:
    return self["key"]


  @property
  def new_value(self) -> Optional[Any]:
    return self.get("new_value")


  @property
  def old_value(self) -> Optional[Any]:
    return self.get("old_value")