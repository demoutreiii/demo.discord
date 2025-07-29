from .activity_location import ActivityLocation
from .snowflake import Snowflake


class ActivityInstance(dict):
  def __init__(self, data: dict[str, ...]) -> None:
    self.__data: dict[str, ...] = data


  @property
  def application_id(self) -> Snowflake:
    return Snowflake(self.__data["application_id"])


  @property
  def instance_id(self) -> str:
    return self.__data["instance_id"]


  @property
  def launch_id(self) -> Snowflake:
    return Snowflake(self.__data["launch_id"])


  @property
  def location(self) -> ActivityLocation:
    return ActivityLocation(self.__data["location"])


  @property
  def users(self) -> list[Snowflake]:
    return [Snowflake(user_id) for user_id in self.__data["users"]]