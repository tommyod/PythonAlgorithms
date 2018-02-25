#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test mathematics algorithms.
"""

import operator
import functools

try:
    from ..mathematics import (prime_factors)
except ValueError:
    pass


def test_prime_factors():
    """
    Test longest consequtive increasing subsequence.
    """
    
    number = 2
    factors = list(prime_factors(number))
    assert number == functools.reduce(operator.mul, factors)
    
    number = 2 * 2 * 3 * 7 * 5
    factors = list(prime_factors(number))
    assert number == functools.reduce(operator.mul, factors)
    
    number = 2 * 2 * 3 * 7 * 5
    factors = list(prime_factors(number))
    assert set(factors) == {2, 2, 3, 5, 7}
    
    number = 2 * 2 * 2
    factors = list(prime_factors(number))
    assert set(factors) == {2, 2, 2}


if __name__ == "__main__":
    import pytest
    # --durations=10  <- May be used to show potentially slow tests
    pytest.main(args=['.', '--doctest-modules', '-v'])