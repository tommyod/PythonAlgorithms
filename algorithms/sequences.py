#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Description.
"""

def fib(n):
    """
    
    Examples
    --------
    >>> fib(5)
    8
    """
    if n in (0, 1):
        return 1
    
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    import pytest
    # --durations=10  <- May be used to show potentially slow tests
    pytest.main(args = ['.', '--doctest-modules', '-v'])