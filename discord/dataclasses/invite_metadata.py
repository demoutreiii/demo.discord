from datetime import datetime


class InviteMetadata(dict):
  @property
  def created_at(self) -> datetime:
    return datetime.fromisoformat(self["created_at"])
  
  
  @property
  def max_age(self) -> int:
    return self["max_age"]
  
  
  @property
  def max_uses(self) -> int:
    return self["max_uses"]


  @property
  def temporary(self) -> bool:
    return self["temporary"]
  
  
  @property
  def uses(self) -> int:
    return self["uses"]