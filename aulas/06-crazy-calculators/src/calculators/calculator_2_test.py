from typing import Dict, List
from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

class MockDriverHandler:
  def standard_derivation(self, numbers: List[float]) -> float:
    return 3

def test_calculate_integration():
  mock_request = MockRequest(body={ "numbers": [2.12, 4.62, 1.32] })

  driver = NumpyHandler()
  calculator_2 = Calculator2(driver)
  formated_response = calculator_2.calculate(mock_request)

  assert isinstance(formated_response, dict)
  assert formated_response == {'data': {'Calculator': 2, 'result': 0.08}}

def test_calculate():
  mock_request = MockRequest(body={ "numbers": [2.12, 4.62, 1.32] })

  driver = MockDriverHandler()
  calculator_2 = Calculator2(driver)
  formated_response = calculator_2.calculate(mock_request)

  assert isinstance(formated_response, dict)
  assert formated_response == {'data': {'Calculator': 2, 'result': 0.33}}