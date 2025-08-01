from ..enums import ApplicationRoleConnectionMetadataType


class ApplicationRoleConnectionMetadata(dict):
  @property
  def description(self) -> str:
    return self["description"]


  @property
  def description_localizations(self) -> dict[str, str]:
    return self.get("description_localizations", dict())


  @property
  def key(self) -> str:
    return self["key"]


  @property
  def name(self) -> str:
    return self["name"]


  @property
  def name_localizations(self) -> dict[str, str]:
    return self.get("name_localizations", dict())


  @property
  def type(self) -> ApplicationRoleConnectionMetadataType:
    return ApplicationRoleConnectionMetadataType(self["type"])