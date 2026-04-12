import pytest
from pyospackage_agastya.example import add_numbers, calculate_latency

def test_add_numbers():
    """Test that the add_numbers function works."""
    assert add_numbers(2, 2) == 4

def test_calculate_latency():
    """Test that the latency calculation is correct."""
    # 0.5 seconds difference should equal 500.0 milliseconds
    assert calculate_latency(1712930000.0, 1712930000.5) == 500.0

def test_calculate_latency_error():
    """Test that a ValueError is raised if receive time is before transmit time."""
    with pytest.raises(ValueError):
        calculate_latency(1712930000.5, 1712930000.0)