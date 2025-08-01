class InstallParams(dict):
  @property
  def permissions(self) -> str:
    return self["permissions"]


  @property
  def scopes(self) -> list[str]:
    return self["scopes"]