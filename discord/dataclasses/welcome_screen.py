from .welcome_screen_channel import WelcomeScreenChannel
from typing import Optional


class WelcomeScreen(dict):
  @property
  def description(self) -> Optional[str]:
    return self["description"]


  @property
  def welcome_channels(self) -> list[WelcomeScreenChannel]:
    return [WelcomeScreenChannel(data) for data in self["welcome_channels"]]