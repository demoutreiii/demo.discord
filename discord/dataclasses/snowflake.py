from datetime import datetime
from typing import Self, Union


class Snowflake(int):
  def __init__(self, value: Union[str, int]) -> None:
    self.__value: int = int(value)
    self._DISCORD_EPOCH: int = 1420070400000


  @property
  def created_at(self) -> datetime:
    return datetime.fromtimestamp((self.__value >> 22) + self._DISCORD_EPOCH)


  @classmethod
  def from_timestamp(cls: Self, timestamp: Union[int, float]) -> Self:
    return cls((timestamp - 1420070400000) << 22)


  @property
  def _increment(self) -> int:
    return self.__value & 0xFFF


  @property
  def _internal_process_id(self) -> int:
    return (self.__value & 0x1F000) >> 12


  @property
  def _internal_worker_id(self) -> int:
    return (self.__value & 0x3E0000) >> 17