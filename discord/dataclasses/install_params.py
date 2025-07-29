class InstallParams(dict):
  def __init__(self, data: dict[str, ...]) -> None:
    self.__data: dict[str, ...] = data


  @property
  def permissions(self) -> str:
    return self.__data["permissions"]


  @property
  def scopes(self) -> list[str]:
    return self.__data["scopes"]