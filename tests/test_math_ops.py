import pytest
from src.math_ops import factorial

def test_factorial_standard_values():
    # Test typical positive integers
    assert factorial(4) == 24
    assert factorial(5) == 120

def test_factorial_edge_cases():
    # Test the boundary values
    assert factorial(0) == 1
    assert factorial(1) == 1

def test_factorial_negative_raises_error():
    # Verify that the function correctly throws an error for negative numbers
    with pytest.raises(ValueError):
        factorial(-5)
