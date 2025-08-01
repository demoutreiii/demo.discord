from .activity_location import ActivityLocation
from .snowflake import Snowflake


class ActivityInstance(dict):
  @property
  def application_id(self) -> Snowflake:
    return Snowflake(self["application_id"])


  @property
  def instance_id(self) -> str:
    return self["instance_id"]


  @property
  def launch_id(self) -> Snowflake:
    return Snowflake(self["launch_id"])


  @property
  def location(self) -> ActivityLocation:
    return ActivityLocation(self["location"])


  @property
  def users(self) -> list[Snowflake]:
    return [Snowflake(user_id) for user_id in self["users"]]