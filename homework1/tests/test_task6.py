import pytest
from src import task6
from pathlib import Path

def test_output(capsys):
    # Retrieve the word count from txt file
    filename = "task6_read_me.txt"
    file_path = Path.cwd() / filename

    # Assertion to test
    assert task6.count_words(file_path) == 104