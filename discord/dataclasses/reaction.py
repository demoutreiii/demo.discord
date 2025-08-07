from .emoji import Emoji
from .reaction_count_details import ReactionCountDetails


class Reaction(dict):
  @property
  def burst_colors(self) -> list[str]:
    return self["burst_colors"]
  
  
  @property
  def count(self) -> int:
    return self["count"]


  @property
  def count_details(self) -> ReactionCountDetails:
    return ReactionCountDetails(self["count_details"])


  @property
  def emoji(self) -> Emoji:
    return Emoji(self["emoji"])


  @property
  def me(self) -> bool:
    return self["me"]


  @property
  def me_burst(self) -> bool:
    return self["me_burst"]