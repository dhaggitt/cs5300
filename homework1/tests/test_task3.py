import pytest
from src import task3

def test_output(capsys):

    # Tests the check sign function
    assert task3.check_sign(-6) is "negative"
    assert task3.check_sign(-1) is "negative"
    assert task3.check_sign(0) is "zero"
    assert task3.check_sign(5) is "positive"
    assert task3.check_sign(999999) is "positive"