class IntegrationAccount(dict):
  @property
  def id(self) -> str:
    return self["id"]


  @property
  def name(self) -> str:
    return self["name"]