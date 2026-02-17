import pytest
from src import task1

def test_output(capsys):
    task1.main()
    captured = capsys.readouterr()
    assert captured.out == "Hello World!\n"