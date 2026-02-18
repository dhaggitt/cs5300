import pytest
import numpy as np
from src import task7

def test_output(capsys):
    # Numpy array for statistic analysis
    numbers = np.array([[85, 7, 8, 23, 61],
        [14, 78, 42, 92, 42],
        [23, 19, 47, 63, 42]])

    # Assertion to test
    stat_obj = task7.calc_stats(numbers)
    assert stat_obj["Mean"] == 43.067
    assert stat_obj["Median"] == 42
    assert stat_obj["Standard Deviation"] == 26.921