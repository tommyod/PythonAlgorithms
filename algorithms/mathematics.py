#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mathematics algorithms.
"""


def prime_factors(number):
    """
    Yield the prime factors of a number.
    
    TODO: This algorithm is not very efficient. Improve it?
    
    Examples
    --------
    >>> for prime_factor in prime_factors(2*3*5*11):
    ...     print(prime_factor)
    2
    3
    5
    11
    
    >>> number = 360
    >>> factors = list(prime_factors(number))
    >>> factors
    [2, 2, 2, 3, 3, 5]
    >>> from functools import reduce
    >>> from operator import mul
    >>> reduce(mul, factors)
    360
    """

    if number <= 1:
        raise ValueError('The `number` must be >= 2.')
        
    if not isinstance(number, (int, )):
        raise ValueError('The `number` must be an integer.')
        
    # The algorithm will keep running as long as the number is >= 2
    while number >= 2:

        # If the number is divisible by 2, yield 2, divide and continue
        if number % 2 == 0:
            yield 2
            number = number // 2
            continue
            
        # Go through possible divisors 3, 5, 7, 9, ... up to sqrt(number)
        for divisor in range(3, int(number**0.5 + 1), 2):
            
            # If a divisor is found, yield it, divide and continue
            if number % divisor == 0:
                yield divisor
                number = number // divisor
                break
        # If no `break` was performed, the number must be prime, yield it
        else:
            yield number
            number = 1


if __name__ == "__main__":
    import pytest
    # --durations=10  <- May be used to show potentially slow tests
    pytest.main(args=['.', '--doctest-modules', '-v'])
    
