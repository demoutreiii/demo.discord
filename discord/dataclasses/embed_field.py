class EmbedField(dict):
  @property
  def inline(self) -> bool:
    return self.get("inline", False)
  
  
  @property
  def name(self) -> str:
    return self["name"]


  @property
  def value(self) -> str:
    return self["value"]