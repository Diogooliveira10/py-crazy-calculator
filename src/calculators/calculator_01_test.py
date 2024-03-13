from typing import Dict
from pytest import raises
from .calculator_01 import Calculator1

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={ "number": 1 })
    calculator_01 = Calculator1()

    response = calculator_01.calculate(mock_request)
    
    # response format
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    # assertiveness of the response
    assert response["data"]["result"] == 14.25
    assert response["data"]["Calculator"] == 1

def test_calculate_with_body_error():
    mock_request = MockRequest(body={ "something": 1 })
    calculator_01 = Calculator1()

    with raises(Exception) as excinfo:
        calculator_01.calculate(mock_request)

    assert str(excinfo.value) == 'Poorly formatted body!'