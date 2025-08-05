from ..enums import OnboardingPromptType
from .prompt_option import PromptOption
from .snowflake import Snowflake


class OnboardingPrompt(dict):
  @property
  def id(self) -> Snowflake:
    return Snowflake(self["id"])


  @property
  def in_onboarding(self) -> bool:
    return self["in_onboarding"]


  @property
  def options(self) -> list[PromptOption]:
    return [PromptOption(data) for data in self["options"]]


  @property
  def required(self) -> bool:
    return self["required"]


  @property
  def single_select(self) -> bool:
    return self["single_select"]


  @property
  def title(self) -> str:
    return self["title"]


  @property
  def type(self) -> OnboardingPromptType:
    return OnboardingPromptType(self["type"])