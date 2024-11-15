from typing import *


type Payload = Dict[str, Any]


class BaseObject(dict):
  def __new__(cls, data : Payload) -> Self:
    return dict.__new__(cls)

  def __init__(cls, data : Payload) -> None:
    self.update({
      name: ((
        self.__annotations__.get(name)({
          name2: data.get(name).get(name2) if data.get(name) is not None else data.get(name)
          for name2 in self.__annotations__.get(name).__annotations__
        }))
        if issubclass(self.__annotations__.get(name), BaseObject) else
        data.get(name, self.__dict__.get(name))
      )
      for name in self.__annotations__
    })