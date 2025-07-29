from .install_params import InstallParams
from typing import Optional


class ApplicationIntegrationTypeConfiguration(dict):
  def __init__(self, data: dict[str, ...]) -> None:
    self.__data: dict[str, ...] = data


  @property
  def oauth2_install_params(self) -> Optional[InstallParams]:
    return InstallParams(self.__data["oauth2_install_params"]) if "oauth2_install_params" in self.__data else None