#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test knapsack algorithms.
"""

try:
    from ..knapsack import (knapsack_without_repetition)
except ValueError:
    pass


def test_knapsack_without_repetition():
    """
    Test longest consequtive increasing subsequence.
    """
    kwr = knapsack_without_repetition
    
    assert kwr(0, [1, 2, 3], [4, 5, 6]) == (0, [])
    assert kwr(100, [], []) == (0, [])
    assert kwr(0, [], []) == (0, [])
    
    # Example from the book Algorithms by Dasgupta (in different orders)
    assert kwr(10, [9, 16, 14, 30], [2, 4, 3, 6]) == (46, [1, 3])
    assert kwr(10, [9, 14, 16, 30], [2, 3, 4, 6]) == (46, [2, 3])


if __name__ == '__main__':
    import pytest
    # --durations=10  <- May be used to show potentially slow tests
    pytest.main(args=['.', '--doctest-modules', '-v'])