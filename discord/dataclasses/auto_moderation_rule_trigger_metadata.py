from ..enums import KeywordPresetType


class AutoModerationRuleTriggerMetadata(dict):
  def __init__(self, data: dict[str, ...]) -> None:
    self.__data: dict[str, ...] = data


  @property
  def allow_list(self) -> list[str]:
    return self.__data["allow_list"]


  @property
  def keyword_filter(self) -> list[str]:
    return self.__data["keyword_filter"]


  @property
  def mention_raid_protection_enabled(self) -> bool:
    return self.__data["mention_raid_protection_enabled"]


  @property
  def mention_total_limit(self) -> int:
    return self.__data["mention_total_limit"]


  @property
  def presets(self) -> list[KeywordPresetType]:
    return [KeywordPresetType(value) for value in self.__data["presets"]]


  @property
  def regex_patterns(self) -> list[str]:
    return self.__data["regex_patterns"]