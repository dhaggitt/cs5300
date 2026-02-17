import pytest
from src import task3

def test_output(capsys):

    # Tests the check sign function
    assert task3.check_sign(-6) is "negative"
    assert task3.check_sign(-1) is "negative"
    assert task3.check_sign(0) is "zero"
    assert task3.check_sign(5) is "positive"
    assert task3.check_sign(999999) is "positive"

    # Tests the first ten primes function
    task3.first_ten_prime()
    captured = capsys.readouterr()
    assert captured.out == "1\n2\n3\n5\n7\n11\n13\n17\n19\n23\n"

    # Tests the century_sum function
    assert task3.century_sum() == 5050