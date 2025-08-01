from datetime import datetime
from typing import Self, Union


class Snowflake(int):
  @property
  def created_at(self) -> datetime:
    return datetime.fromtimestamp(((self >> 22) + 1420070400000) // 1_000)


  @classmethod
  def from_timestamp(cls: Self, timestamp: Union[int, float]) -> Self:
    return cls(((int(timestamp) * 1_000) - 1420070400000) << 22)


  @property
  def _increment(self) -> int:
    return self & 0xFFF


  @property
  def _internal_process_id(self) -> int:
    return (self & 0x1F000) >> 12


  @property
  def _internal_worker_id(self) -> int:
    return (self & 0x3E0000) >> 17