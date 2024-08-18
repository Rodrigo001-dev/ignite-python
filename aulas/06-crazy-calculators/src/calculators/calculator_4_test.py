from .calculator_4 import Calculator4
from typing import Dict

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

def test_calculate():
  mock_request = MockRequest({"numbers": [10, 10, 10, 10, 10]})
  calculator_4 = Calculator4()

  response = calculator_4.calculate_average(mock_request)

  assert response == {'data': {'Calculator': 4, 'average': 10}}