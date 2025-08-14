from ..enums import PollLayoutType
from .poll_answer import PollAnswer
from .poll_media import PollMedia
from .poll_result import PollResult
from datetime import datetime
from typing import Optional


class Poll(dict):
  @property
  def allow_multiselect(self) -> bool:
    return self["allow_multiselect"]
  
  
  @property
  def answers(self) -> list[PollAnswer]:
    return [PollAnswer(data) for data in self["answers"]]


  @property
  def expiry(self) -> Optional[datetime]:
    return datetime.fromisotimestamp(self["expiry"]) if self["expiry"] is not None else None


  @property
  def layout_type(self) -> PollLayoutType:
    return PollLayoutType(self["layout_type"])
  
  
  @property
  def question(self) -> PollMedia:
    return PollMedia(self["question"])


  @property
  def results(self) -> Optional[PollResult]:
    return PollResult(self["results"]) if "results" in self else None