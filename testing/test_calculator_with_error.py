import calculator_with_error
import pytest

def test_simple_calculator():
    with pytest.raises(NameError):
        calculator_with_error.simple_calculator("ad",100,0)
