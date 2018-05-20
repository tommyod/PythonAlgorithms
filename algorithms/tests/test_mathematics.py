#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test mathematics algorithms.
"""

import operator
import functools

try:
    from ..mathematics import (prime_factors, prime_sieve)
except ValueError:
    pass


def test_prime_sieve():
    """
    Test prime sieve.
    """
    assert prime_sieve(3) == [2, 3]
    
    assert prime_sieve(4) == [2, 3]
    
    assert prime_sieve(5) == [2, 3, 5]
    
    assert prime_sieve(6) == [2, 3, 5]
    
    assert prime_sieve(7) == [2, 3, 5, 7]
    
    assert prime_sieve(8) == [2, 3, 5, 7]
    
    assert prime_sieve(9) == [2, 3, 5, 7]
    
    assert prime_sieve(10) == [2, 3, 5, 7]
    
    assert prime_sieve(11) == [2, 3, 5, 7, 11]
    


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