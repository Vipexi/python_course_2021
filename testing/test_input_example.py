import input_example
import mock

def test_ask_from_user():
    with mock.patch('builtins.input', return_value="yes"):
        assert input_example.ask_from_user() == True
    with mock.patch('builtins.input', return_value="anything"):
        assert input_example.ask_from_user() == False