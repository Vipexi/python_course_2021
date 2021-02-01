import task7_normal

import random

def test_normal_numbers():
    random.seed(13)
    assert task7_normal.normal_numbers() == [16,18,23,43,49]
    random.seed(43)
    assert task7_normal.normal_numbers() == [7,9,16,19,33]
