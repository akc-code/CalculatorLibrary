"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:
    def test_addition(self) -> None:
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self) -> None:
        assert 2 == calculator.subtract(4, 2)

    def test_multiply(self) -> None:
        assert 4 == calculator.multiply(2, 2)
