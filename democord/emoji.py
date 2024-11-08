from typing import *


class EmojiMeta(type):
  def __instancecheck__(cls, instance : Any) -> bool:
    from .objects import EmojiObject
    return instance.__class__ == EmojiObject


class Emoji(metaclass = EmojiMeta):
  @property
  def animated(self) -> bool:
    return self["animated"]

  @property
  def available(self) -> bool:
    return self["available"]

  @property
  def id(self) -> Optional[int]:
    return int(self["id"]) if self["id"] is not None else None

  @property
  def managed(self) -> bool:
    return self["managed"]

  @property
  def name(self) -> Optional[str]:
    return self["name"]

  @property
  def require_colons(self) -> bool:
    return self["require_colons"]

  @property
  def roles(self) -> List["Role"]:
    # implement: Constructor.role(data : RoleObject)
    return [Constructor.role(role_data) for role_data in self["roles"]]

  @property
  def user(self) -> Optional[str]:
    # implement: Constructor.user(data : UserObject)
    return Constructor.user(self["user"]) if self["user"] is not None else None