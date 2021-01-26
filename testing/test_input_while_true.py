import input_while_true
import mock

def test_ask_number_from_user():
    with mock.patch('builtins.input', side_effect=['two','no','1']):
        assert input_while_true.ask_number_from_user() == 1
