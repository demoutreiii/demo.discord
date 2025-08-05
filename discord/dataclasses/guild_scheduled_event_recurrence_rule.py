from ..enums import GuildScheduledEventRecurrenceRuleFrequency, GuildScheduledEventRecurrenceRuleMonth, GuildScheduledEventRecurrenceRuleNWeekday, GuildScheduledEventRecurrenceRuleWeekday
from datetime import datetime
from typing import Optional


class GuildScheduledEventRecurrenceRule(dict):
  @property
  def by_month(self) -> Optional[list[GuildScheduledEventRecurrenceRuleMonth]]:
    return [GuildScheduledEventRecurrenceRuleMonth(value) for value in self["by_month"]] if self["by_month"] is not None else None


  @property
  def by_month_day(self) -> Optional[list[int]]:
    return self["by_month_day"]


  @property
  def by_n_weekday(self) -> Optional[list[GuildScheduledEventRecurrenceRuleNWeekday]]:
    return [GuildScheduledEventRecurrenceRuleNWeekday(value) for value in self["by_n_weekday"]] if self["by_n_weekday"] is not None else None
  
  
  @property
  def by_weekday(self) -> Optional[list[GuildScheduledEventRecurrenceRuleWeekday]]:
    return [GuildScheduledEventRecurrenceRuleWeekday(value) for value in self["by_weekday"]] if self["by_weekday"] is not None else None


  @property
  def by_year_day(self) -> Optional[list[int]]:
    return self["by_year_day"]


  @property
  def count(self) -> Optional[int]:
    return self["count"]
  
  
  @property
  def end(self) -> Optional[datetime]:
    return datetime.fromisoformat(self["end"]) if self["end"] is not None else None


  @property
  def frequency(self) -> GuildScheduledEventRecurrenceRuleFrequency:
    return GuildScheduledEventRecurrenceRuleFrequency(self["frequency"])


  @property
  def interval(self) -> int:
    return self["interval"]
  
  
  @property
  def start(self) -> datetime:
    return datetime.fromisoformat(self["start"])