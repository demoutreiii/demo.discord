from ..enums import KeywordPresetType


class AutoModerationRuleTriggerMetadata(dict):
  @property
  def allow_list(self) -> list[str]:
    return self["allow_list"]


  @property
  def keyword_filter(self) -> list[str]:
    return self["keyword_filter"]


  @property
  def mention_raid_protection_enabled(self) -> bool:
    return self["mention_raid_protection_enabled"]


  @property
  def mention_total_limit(self) -> int:
    return self["mention_total_limit"]


  @property
  def presets(self) -> list[KeywordPresetType]:
    return [KeywordPresetType(value) for value in self["presets"]]


  @property
  def regex_patterns(self) -> list[str]:
    return self["regex_patterns"]