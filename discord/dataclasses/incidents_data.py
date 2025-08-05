from datetime import datetime
from typing import Optional


class IncidentsData(dict):
  @property
  def dms_disabled_until(self) -> Optional[datetime]:
    return datetime.fromisoformat(self["dms_disabled_until"]) if self["dms_disabled_until"] is not None else None


  @property
  def dm_spam_detected_at(self) -> Optional[datetime]:
    return datetime.fromisoformat(self.get("dm_spam_detected_at")) if self.get("dm_spam_detected_at") is not None else None

  
  @property
  def invites_disabled_until(self) -> Optional[datetime]:
    return datetime.fromisoformat(self["invites_disabled_until"]) if self["invites_disabled_until"] is not None else None


  @property
  def raid_detected_at(self) -> Optional[datetime]:
    return datetime.fromisoformat(self.get("raid_detected_at")) if self.get("raid_detected_at") is not None else None