import pytest
from src import task4

def test_output():
    # Tests a multitude of price and discounts
    assert task4.calculate_discount(180000, 3) == 174600.00
    assert task4.calculate_discount(125, 25) == 93.75
    assert task4.calculate_discount(6.5, 50) == 3.25
    assert task4.calculate_discount(84.50, 12.625) == 73.83
    assert task4.calculate_discount(80, 6.5) == 74.80
    assert task4.calculate_discount(12.95, 51.5) == 6.28
    assert task4.calculate_discount(180, 180) == -144.00
    assert task4.calculate_discount(40, -20) == 48.00