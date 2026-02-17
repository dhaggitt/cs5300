import pytest
from src import task1

def test_output(capsys):
    # Declare captured object
    task1.main()
    captured = capsys.readouterr()

    # Assertions for testing
    assert captured.out == "Hello World!\n"