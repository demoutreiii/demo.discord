from ..enums import AuditLogEvent
from .audit_log_change import AuditLogChange
from .optional_audit_entry_info import OptionalAuditEntryInfo
from .snowflake import Snowflake
from typing import Optional


class AuditLogEntry(dict):
  def __init__(self, data: dict[str, ...]) -> None:
    self.__data: dict[str, ...] = data

  @property
  def action_type(self) -> AuditLogEvent:
    return AuditLogEvent(self.__data["action_type"])


  @property
  def changes(self) -> list[AuditLogChange]:
    return [AuditLogChange(audit_log_change_data) for audit_log_change_data in self.__data.get("changes", list())]


  @property
  def id(self) -> Snowflake:
    return Snowflake(self.__data["id"])


  @property
  def options(self) -> Optional[OptionalAuditEntryInfo]:
    return OptionalAuditEntryInfo(self.__data["options"]) if "options" in self.__data else None


  @property
  def reason(self) -> Optional[str]:
    return self.__data.get("reason")


  @property
  def target_id(self) -> Optional[str]:
    return self.__data["target_id"]


  @property
  def user_id(self) -> Optional[Snowflake]:
    return Snowflake(self.__data["user_id"]) if self.__data["user_id"] is not None else None