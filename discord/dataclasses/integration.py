from ..enums import IntegrationExpireBehavior, OAuth2Scope
from .integration_account import IntegrationAccount
from .integration_application import IntegrationApplication
from .snowflake import Snowflake
from .user import User
from datetime import datetime
from typing import Optional


class Integration(dict):
  @property
  def account(self) -> IntegrationAccount:
    return IntegrationAccount(self["account"])


  @property
  def application(self) -> IntegrationApplication:
    return IntegrationApplication(self["application"]) if "application" in self else None
  
  
  @property
  def enabled(self) -> bool:
    return self["enabled"]
  
  
  @property
  def enabled_emoticons(self) -> Optional[bool]:
    return self.get("enabled_emoticons")


  @property
  def expire_behavior(self) -> Optional[IntegrationExpireBehavior]:
    return IntegrationExpireBehavior(self["expire_behavior"]) if "expire_behavior" in self else None


  @property
  def expire_grace_period(self) -> Optional[int]:
    return self.get("expire_grace_period")
  
  
  @property
  def id(self) -> Snowflake:
    return Snowflake(self["id"])


  @property
  def name(self) -> str:
    return self["name"]


  @property
  def revoked(self) -> Optional[bool]:
    return self.get("revoked")


  @property
  def role_id(self) -> Optional[Snowflake]:
    return Snowflake(self["role_id"]) if "role_id" in self else None


  @property
  def scopes(self) -> Optional[list[OAuth2Scope]]:
    return [OAuth2Scope(name) for name in self["scopes"]] if "scopes" in self else None


  @property
  def subscriber_count(self) -> Optional[int]:
    return self.get("subscriber_count")


  @property
  def synced_at(self) -> Optional[datetime]:
    return datetime.fromisoformat(self["synced_at"]) if "synced_at" in self else None


  @property
  def syncing(self) -> Optional[bool]:
    return self.get("syncing")


  @property
  def type(self) -> str:
    return self["type"]


  @property
  def user(self) -> Optional[User]:
    return User(self["user"]) if "user" in self else None