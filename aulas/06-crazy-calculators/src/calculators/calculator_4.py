from flask import request as FlaskRequest
from typing import Dict, List
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:
  def calculate_average(self, request: FlaskRequest) -> dict:
    body = request.json
    numbers = self.__validate_body(body)

    average = sum(numbers) / len(numbers)
    response = self.__format_response(average)

    return response
  
  def __validate_body(self, body: Dict) -> List[float]:
    if "numbers" not in body:
      raise HttpUnprocessableEntityError("body mal formatado!")
    
    numbers = body["numbers"]
    
    if not numbers or not all(isinstance(num, (int, float)) for num in numbers):
      raise HttpUnprocessableEntityError("Lista de números não fornecida ou mal formatada!")

    return numbers

  def __format_response(self, average: float) -> dict:
    return {
      "data": {
        "Calculator": 4,
        "average": round(average, 2)
      }
    }