import pytest
from src import task2

def test_output(capsys):
    # Variables declared for efficiency
    x = task2.return_integer()
    y = task2.return_float()
    z = task2.return_bool()
    s = task2.return_string()

    # Assertions for testing
    assert isinstance(x, int)
    assert isinstance(y, float)
    assert isinstance(z, bool)
    assert isinstance(s, str)