#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Description.
"""

import collections


def fibonacci_order_n(n, terms=5):
    """
    Yields the first t terms in the generalized Fibonacci numbers of order n.
    We define the generalized Fibonacci numbers of order n by the recursion:
    F(0 ... n) = 1
    F(i) = F(i - 1) + F(i - 2) + F(i - n)
    
    Algorithmic details
    -------------------
    Memory: O(t)
    Time: O(nt)
    where n is the order and t is the number of terms.
    
    Examples
    --------
    >>> list(fibonacci_order_n(2, terms = 8))
    [1, 1, 2, 3, 5, 8, 13, 21]
    
    >>> list(fibonacci_order_n(4, terms = 10))
    [1, 1, 1, 1, 4, 7, 13, 25, 49, 94]
    
    References
    ----------
    [1] ...
    """
    
    # Initialize a partial sequence, i.e. variables to keep track of.
    # Since F(i) = F(i - 1) + F(i - 2) + F(i - n), we only keep n variables.
    partial_sequence = collections.deque([1] * n)
    
    # Yield the variables in the partial sequence
    for i, value in enumerate(partial_sequence, start=1):
        if i > terms:
            return
        yield value
    
    # Start yielding, summing and exchanging in a queue-structure
    while True:
        i += 1
        next_value = sum(partial_sequence)
        
        # Add a break criterion to help the user, making it harder to
        # generate an infinite stream of elements
        if i > terms:
            return
            
        yield next_value
        partial_sequence.popleft()
        partial_sequence.append(next_value)


if __name__ == "__main__":
    import pytest
    # --durations=10  <- May be used to show potentially slow tests
    pytest.main(args=['.', '--doctest-modules', '-v'])