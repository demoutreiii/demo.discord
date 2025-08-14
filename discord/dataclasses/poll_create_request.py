from ..enums import PollLayoutType
from .poll_answer import PollAnswer
from .poll_media import PollMedia
from datetime import timedelta
from typing import Optional


class PollCreateRequest(dict):
  @property
  def allow_multiselect(self) -> bool:
    return self.get("allow_multiselect", False)


  @allow_multiselect.setter
  def allow_multiselect(self, value: bool) -> bool:
    if not isinstance(value, bool): raise TypeError(f"Poll.allow_multiselect must be of type 'bool', not {value.__class__.__name__}")
    self["allow_multiselect"]: bool = value
    return self.allow_multiselect
  
  
  @property
  def answers(self) -> list[PollAnswer]:
    return [PollAnswer(data) for data in self["answers"]]


  @property
  def duration(self) -> timedelta:
    return timedelta(hours = self.get("duration", 24))


  @duration.setter
  def duration(self, value: timedelta) -> timedelta:
    if not isinstance(value, timedelta): raise TypeError(f"Poll.duration must be of type 'datetime.timedelta', not {value.__class__.__name__}.")
    self["duration"]: int = value.hours
    return self.duration


  @property
  def layout_type(self) -> PollLayoutType:
    return PollLayoutType(self["layout_type"]) if "layout_type" in self else PollLayoutType.DEFAULT


  @layout_type.setter
  def layout_type(self, value: PollLayoutType) -> PollLayoutType:
    if not isinstance(value, PollLayoutType): raise TypeError(f"Poll.layout_type must be of type 'PollLayoutType', not {value.__class__.__name__}.")
    self["layout_type"]: int = value
    return self.layout_type
  
  
  @property
  def question(self) -> PollMedia:
    return PollMedia(self["question"])