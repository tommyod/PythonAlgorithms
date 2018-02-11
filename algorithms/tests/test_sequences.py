#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Description.
"""

try:
    from ..sequences import (longest_conseq_inc_subsequence,
                             maximums_from_left,
                             fibonacci_order_n,
                             running_average)
except ValueError:
    pass


def test_longest_conseq_inc_subsequence():
    """
    Test longest consequtive increasing subsequence.
    """
    seq = [4, 6, 8, 0, 2, 0, 2, 0, 4]
    lcis = longest_conseq_inc_subsequence
    assert lcis(seq, True) == 3
    assert lcis(seq, False) == [4, 6, 8]
    
    assert lcis(iter([3, 2, 1]), True) == 1
    assert lcis(iter([3, 2, 1]), False) == [3]
    
    assert lcis(iter([3]), False) == [3]
    assert lcis(iter([1]), True) == 1
    
    seq = [4, 5, 6, 5, 6, 7, 8, 9, 1, 2, 3]
    assert lcis(seq, True) == 5
    assert lcis(seq, False) == [5, 6, 7, 8, 9]


def test_maximums_from_left():
    """
    Test the number of maximums from the left.
    """
    seq = (-5, -4, -3, -2)
    mfl = maximums_from_left
    assert list(mfl(seq)) == [(0, -5), (1, -4), (2, -3), (3, -2)]
    
    seq = (i for i in [5, 4, 3, 7, 6, 5, 9, 8, 10])
    assert list(mfl(seq)) == [(0, 5), (3, 7), (6, 9), (8, 10)]
    
    seq = iter([0, 2, 4])
    assert list(mfl(seq)) == [(0, 0), (1, 2), (2, 4)]
    
    seq = iter([6])
    assert list(mfl(seq)) == [(0, 6)]


def test_fibonacci_order_n():
    """
    Test order n Fibonacci orders.
    """
    
    fon = fibonacci_order_n
    assert list(fon(10, terms=5)) == [1, 1, 1, 1, 1]
    assert list(fon(2, terms=5)) == [1, 1, 2, 3, 5]
    assert list(fon(3, terms=10)) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
    
    
def test_running_average():
    """
    Test the running average.
    """
    
    # Test the function on list inputs
    ra = running_average
    assert list(ra([1, 1, 1])) == [1, 1, 1]
    assert list(ra([2, 1, 1])) == [2, 3 / 2, 4 / 3]
    assert list(ra([])) == []
    assert list(ra(iter([1, 2, 3, 4, 5]))) == [1, 3 / 2, 6 / 3, 10 / 4, 15 / 5]
    
    # Make sure the function works when an iterable is passed
    iterable = (1, 1, 1)
    assert list(ra(iterable)) == [1, 1, 1]


if __name__ == "__main__":
    import pytest
    # --durations=10  <- May be used to show potentially slow tests
    pytest.main(args=['.', '--doctest-modules', '-v'])