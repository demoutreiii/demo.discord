from .base  import BaseObject
from typing import *


class ApplicationIntegrationTypeConfigObject(BaseObject):
  from .install_params import InstallParamsObject

  oauth2_install_params : Optional[InstallParamsObject]