from ..enums import AutoModerationActionType
from .auto_moderation_action_metadata import AutoModerationActionMetadata
from typing import Optional


class AutoModerationAction(dict):
  @property
  def metadata(self) -> Optional[AutoModerationActionMetadata]:
    return AutoModerationActionMetadata(self["metadata"]) if "metadata" in self else None


  @property
  def type(self) -> AutoModerationActionType:
    return AutoModerationActionType(self["type"])