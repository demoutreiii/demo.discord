from .snowflake import Snowflake


class FollowedChannel(dict):
  @property
  def channel_id(self) -> Snowflake:
    return Snowflake(self["channel_id"])


  @property
  def webhook_id(self) -> Snowflake:
    return Snowflake(self["webhook_id"])