class ReactionCountDetails(dict):
  @property
  def burst(self) -> int:
    return self["burst"]


  @property
  def normal(self) -> int:
    return self["normal"]