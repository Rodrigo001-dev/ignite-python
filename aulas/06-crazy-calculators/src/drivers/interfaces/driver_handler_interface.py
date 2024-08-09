from abc import ABC, abstractclassmethod
from typing import List

class DriverHandlerInterface(ABC):

  @abstractclassmethod
  def standard_derivation(self, numbers : List[float]) -> float:
    pass