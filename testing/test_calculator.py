import calculator

def test_simple_calculator():
    assert calculator.simple_calculator("add", 1, 1) == 2
    
    assert calculator.simple_calculator("multiply",1 ,1) == 1

    assert calculator.simple_calculator("anything", 1 ,1) == ""
