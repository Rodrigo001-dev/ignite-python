from abc import ABC, abstractmethod

class Client(ABC):

  @abstractmethod
  def withdraw_money(self, quantia):
    pass

  @abstractmethod
  def perform_extract(self, pessoa):
    pass