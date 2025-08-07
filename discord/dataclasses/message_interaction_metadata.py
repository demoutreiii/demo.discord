from ..enums import ApplicationIntegrationType, InteractionType
from .snowflake import Snowflake
from .user import User
from typing import Optional, Self


class MessageInteractionMetadata(dict):
  @property
  def authorizing_integration_owners(self) -> dict[ApplicationIntegrationType, str]:
    return {ApplicationIntegrationType(key): value for key, value in self["authorizing_integration_owners"].items()}
  
  
  @property
  def id(self) -> Snowflake:
    return Snowflake(self["id"])


  @property
  def interacted_message_id(self) -> Snowflake:
    if self.type != Interaction.MESSAGE_COMPONENT:
      raise AttributeError("'interacted_message_id' attribute is only available for InteractionType.MESSAGE_COMPONENT interactions.")
    return Snowflake(self["interacted_message_id"])


  @property
  def original_response_message_id(self) -> Optional[Snowflake]:
    return Snowflake(self["original_response_message_id"]) if "original_response_message_id" in self else None


  @property
  def target_message_id(self) -> Optional[Snowflake]:
    if self.type != InteractionType.APPLICATION_COMMAND:
      raise AttributeError("'target_message_id' attribute is only available for InteractionType.APPLICATION_COMMAND interactions.")
    return Snowflake(self["target_message_id"]) if "target_message_id" in self else None


  @property
  def target_user(self) -> Optional[User]:
    if self.type != InteractionType.APPLICATION_COMMAND:
      raise AttributeError("'target_user' attribute is only available for InteractionType.APPLICATION_COMMAND interactions.")
    return User(self["target_user"]) if "target_user" in self else None


  @property
  def triggering_interaction_metadata(self) -> Self:
    if self.type != InteractionType.MODAL_SUBMIT:
      raise AttributeError("'triggering_interaction_metadata' attribute is only available for InteractionType.MODAL_SUBMIT interactions.")
    return MessageInteractionMetadata(self["triggering_interaction_metadata"])


  @property
  def type(self) -> InteractionType:
    return InteractionType(self["type"])


  @property
  def user(self) -> User:
    return User(self["user"])