#!/usr/bin/env python3
"""
Basic unit tests for add_numbers.py
This ensures the GitHub Actions pipeline has tests to run
"""

import sys
import os

# Add the current directory to Python path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import add_numbers


def test_add_numbers_positive():
    """Test addition with positive numbers"""
    result = add_numbers.add_numbers(5, 3)
    assert result == 8, f"Expected 8, got {result}"


def test_add_numbers_negative():
    """Test addition with negative numbers"""
    result = add_numbers.add_numbers(-5, -3)
    assert result == -8, f"Expected -8, got {result}"


def test_add_numbers_mixed():
    """Test addition with mixed positive and negative numbers"""
    result = add_numbers.add_numbers(-5, 3)
    assert result == -2, f"Expected -2, got {result}"


def test_add_numbers_zero():
    """Test addition with zero"""
    result = add_numbers.add_numbers(0, 5)
    assert result == 5, f"Expected 5, got {result}"


def test_add_numbers_decimals():
    """Test addition with decimal numbers"""
    result = add_numbers.add_numbers(3.5, 2.5)
    assert result == 6.0, f"Expected 6.0, got {result}"


if __name__ == "__main__":
    # Run all tests
    print("Running basic tests for add_numbers.py...")
    
    test_add_numbers_positive()
    print("✓ Positive numbers test passed")
    
    test_add_numbers_negative()
    print("✓ Negative numbers test passed")
    
    test_add_numbers_mixed()
    print("✓ Mixed numbers test passed")
    
    test_add_numbers_zero()
    print("✓ Zero test passed")
    
    test_add_numbers_decimals()
    print("✓ Decimal numbers test passed")
    
    print("\n🎉 All tests passed successfully!")
