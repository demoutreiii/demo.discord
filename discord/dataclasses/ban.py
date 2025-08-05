from .user import User
from typing import Optional


class Ban(dict):
  @property
  def reason(self) -> Optional[str]:
    return self["reason"]


  @property
  def user(self) -> User:
    return User(self["user"])