from typing import Dict, List
from .calculator_02 import Calculator2
from src.drivers.numpy_handler import NumpyHandler
class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler:
    def standard_derivation(self, numbers: List[float]) -> float:
        return 3

# Integração entre NumpyHandler e Calculator2
def test_calculate_integration():
    mock_request = MockRequest({ "numbers": [2.12, 5.23, 1.32] })

    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)
    formated_response = calculator_2.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 2, 'result': 0.07}}

def test_calculate():
    mock_request = MockRequest({ "numbers": [2.12, 5.23, 1.32] })

    driver = MockDriverHandler()
    calculator_2 = Calculator2(driver)
    formated_response = calculator_2.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 2, 'result': 0.33}}