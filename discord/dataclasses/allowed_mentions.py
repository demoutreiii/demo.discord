from ..enums import AllowedMentionType
from .member import Member
from .role import Role
from .snowflake import Snowflake
from .user import User
from typing import Optional


class AllowedMentions(dict):
  @property
  def parse(self) -> Optional[list[AllowedMentionType]]:
    return [AllowedMentionType(data) for data in self["parse"]] if "parse" in self else None


  @property
  def replied_user(self) -> bool:
    return self.get("replied_user", False)


  @property
  def roles(self) -> Optional[list[Snowflake]]:
    return [Snowflake(data) for data in self["roles"]] if "roles" in self else None


  @property
  def users(self) -> Optional[list[Snowflake]]:
    return [Snowflake(data) for data in self["users"]] if "users" in self else None


  @parse.setter
  def parse(self, value: Optional[list[AllowedMentionType]]) -> Optional[list[AllowedMentionType]]:
    if value is None and self.parse is not None: del self["parse"]
    else:
      if not isinstance(value, list): raise TypeError("Must be a list of AllowedMentionType enum")
      if not all(isinstance(element, AllowedMentionType) for element in value): raise ValueError("Must be a list of AllowedMentionType enum")
      self["parse"]: list[str] = [element.value for element in value]
    return self.parse


  @replied_user.setter
  def replied_user(self, value: bool) -> bool:
    assert isinstance(value, bool), "Must be a boolean value"
    self["replied_user"]: bool = value
    return self.replied_user


  @roles.setter
  def roles(self, value: Optional[list[Union[Role, Snowflake, int]]]) -> Optional[list[Snowflake]]:
    if value is None and self.roles is not None: del self["roles"]
    else:
      if not isinstance(value, list): raise TypeError("Must be a list of union of Role, Snowflake, or integer objects")
      if not all(isinstance(element, (Role, Snowflake, int)) for element in value): raise ValueError("Must be a list of union of Role, Snowflake, or integer objects")
      self["roles"]: list[int] = [element.id if isinstance(element, Role) else element for element in value]
    return self.roles


  @users.setter
  def users(self, value: Optional[list[Union[User, Member, Snowflake, int]]]) -> Optional[list[Snowflake]]:
    if value is None and self.users is not None: del self["users"]
    else:
      if not isinstance(value, list): raise TypeError("Must be a list of union of User, Member, Snowflake, or integer objects")
      if not all(isinstance(element, (User, Member, Snowflake, int)) for element in value): raise ValueError("Must be a list of union of User, Member, Snowflake, or integer objects")
      self["users"]: list[int] = [element.id if isinstance(element, (User, Member)) else element for element in value]
    return self.users