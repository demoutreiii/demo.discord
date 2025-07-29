from ..enums import ApplicationRoleConnectionMetadataType


class ApplicationRoleConnectionMetadata(dict):
  def __init__(self, data: dict[str, ...]) -> None:
    self.__data: dict[str, ...] = data


  @property
  def description(self) -> str:
    return self.__data["description"]


  @property
  def description_localizations(self) -> dict[str, str]:
    return self.__data.get("description_localizations", dict())


  @property
  def key(self) -> str:
    return self.__data["key"]


  @property
  def name(self) -> str:
    return self.__data["name"]


  @property
  def name_localizations(self) -> dict[str, str]:
    return self.__data.get("name_localizations", dict())


  @property
  def type(self) -> ApplicationRoleConnectionMetadataType:
    return ApplicationRoleConnectionMetadataType(self.__data["type"])