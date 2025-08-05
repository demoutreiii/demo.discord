from ..enums import OnboardingMode
from .onboarding_prompt import OnboardingPrompt
from .snowflake import Snowflake


class GuildOnboarding(dict):
  @property
  def default_channel_ids(self) -> list[Snowflake]:
    return [Snowflake(data) for data in self["default_channel_ids"]]


  @property
  def enabled(self) -> bool:
    return self["enabled"]
  
  
  @property
  def guild_id(self) -> Snowflake:
    return Snowflake(self["guild_id"])


  @property
  def mode(self) -> OnboardingMode:
    return OnboardingMode(self["mode"])


  @property
  def prompts(self) -> list[OnboardingPrompt]:
    return [OnboardingPrompt(data) for data in self["prompts"]]