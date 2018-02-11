#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Description.
"""

try:
    from ..geometry import closest_pair_line
except ValueError:
    pass


def test_closest_pair_line():
    """
    Test closest pair of points in a line.
    """
    
    assert closest_pair_line([0, 2, 3, 5, 8]) == (2, 3)
    assert closest_pair_line([5, 8]) == (5, 8)
    assert closest_pair_line([0, 20, 35, 40, 60, 80, 57]) == (57, 60)
    assert closest_pair_line([50, 10, 30, 40, 20, 35, 14, 28]) == (28, 30)
    assert closest_pair_line([-20, -10, 0, 10, 20, -15, -6]) == (-10, -6)
    
    
if __name__ == "__main__":
    import pytest
    # --durations=10  <- May be used to show potentially slow tests
    pytest.main(args=['.', '--doctest-modules', '-v'])