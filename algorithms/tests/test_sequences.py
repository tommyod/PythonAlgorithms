#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Description.
"""

from sequences import (fibonacci_order_n)

    
def test_fibonacci_order_n():
    
    fon = fibonacci_order_n
    assert list(fon(10, terms=5)) == [1, 1, 1, 1, 1]
    assert list(fon(2, terms=5)) == [1, 1, 2, 3, 5]
    assert list(fon(3, terms=10)) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]


if __name__ == "__main__":
    import pytest
    # --durations=10  <- May be used to show potentially slow tests
    pytest.main(args=['.', '--doctest-modules', '-v'])