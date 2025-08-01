from .install_params import InstallParams
from typing import Optional


class ApplicationIntegrationTypeConfiguration(dict):
  @property
  def oauth2_install_params(self) -> Optional[InstallParams]:
    return InstallParams(self["oauth2_install_params"]) if "oauth2_install_params" in self else None