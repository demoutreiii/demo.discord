from ..types import Snowflake
from .base   import BaseObject
from typing  import *


class GuildOnboardingObject(BaseObject):
  from .onboarding_prompt import OnboardingPromptObject

  default_channel_ids : List[Snowflake]              = []
  enabled             : bool
  guild_id            : Snowflake
  mode                : int
  prompts             : List[OnboardingPromptObject] = []