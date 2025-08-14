from .snowflake import Snowflake


class RoleSubscriptionData(dict):
  @property
  def is_renewal(self) -> bool:
    return self["is_renewal"]
  
  
  @property
  def role_subscription_listing_id(self) -> Snowflake:
    return Snowflake(self["role_subscription_listing_id"])


  @property
  def tier_name(self) -> str:
    return self["tier_name"]


  @property
  def total_months_subscribed(self) -> int:
    return self["total_months_subscribed"]