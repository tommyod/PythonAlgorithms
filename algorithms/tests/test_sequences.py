#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Description.
"""

from ..sequences import fib


def test_fib():
    
    assert fib(0) == 1
    assert fib(2) == 2


if __name__ == "__main__":
    import pytest
    # --durations=10  <- May be used to show potentially slow tests
    pytest.main(args=['.', '--doctest-modules', '-v'])