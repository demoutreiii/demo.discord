from ..enums import AuditLogEvent
from .audit_log_change import AuditLogChange
from .optional_audit_entry_info import OptionalAuditEntryInfo
from .snowflake import Snowflake
from typing import Optional


class AuditLogEntry(dict):
  @property
  def action_type(self) -> AuditLogEvent:
    return AuditLogEvent(self["action_type"])


  @property
  def changes(self) -> list[AuditLogChange]:
    return [AuditLogChange(audit_log_change_data) for audit_log_change_data in self.get("changes", list())]


  @property
  def id(self) -> Snowflake:
    return Snowflake(self["id"])


  @property
  def options(self) -> Optional[OptionalAuditEntryInfo]:
    return OptionalAuditEntryInfo(self["options"]) if "options" in self else None


  @property
  def reason(self) -> Optional[str]:
    return self.get("reason")


  @property
  def target_id(self) -> Optional[str]:
    return self["target_id"]


  @property
  def user_id(self) -> Optional[Snowflake]:
    return Snowflake(self["user_id"]) if self["user_id"] is not None else None