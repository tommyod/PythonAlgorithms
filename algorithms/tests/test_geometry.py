#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test geometry algorithms.
"""

try:
    from ..geometry import (closest_pair_line,
                            elements_of_maxnorm)
except ValueError:
    pass


def test_closest_pair_line():
    """
    Test closest pair of points in a line.
    """
    
    assert closest_pair_line([0, 2, 3, 5, 8]) == (1, 2)
    assert closest_pair_line([5, 8]) == (0, 1)
    assert closest_pair_line([0, 20, 35, 40, 60, 80, 57]) == (4, 6)
    assert closest_pair_line([50, 10, 30, 40, 20, 35, 14, 28]) == (2, 7)
    assert closest_pair_line([-20, -10, 0, 10, 20, -15, -6]) == (1, 6)
    
    
def test_elements_of_maxnorm():
    """
    Test generation of group elements in Z^n by max norm.
    """
    
    eom = elements_of_maxnorm  # (free_rank, maxnorm_value)
    
    assert set(eom(0, maxnorm_value=1)) == set()  # Free rank 0, no items
    assert set(eom(3, maxnorm_value=0)) == {(0, 0, 0)}  # Norm 0 in Z^3
    
    assert set(eom(1, maxnorm_value=1)) == {(-1, ), (1, )}  # Free rank 1
    assert set(eom(1, maxnorm_value=2)) == {(-2, ), (2, )}  # Free rank 1
    
    answer = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
              (1, -1), (1, 0), (1, 1)}
    assert set(eom(2, maxnorm_value=1)) == answer  # Free rank 2
    
    answer = {(0, 1, 1), (1, -1, -1), (1, 0, 0), (1, 0, 1), (-1, -1, -1),
              (-1, 1, -1), (1, 1, -1), (0, -1, -1), (0, 0, -1), (-1, 0, 1),
              (-1, 0, 0), (-1, 0, -1), (0, 0, 1), (0, -1, 1), (0, -1, 0),
              (1, 1, 1), (-1, 1, 0), (1, 1, 0), (-1, 1, 1), (-1, -1, 1),
              (1, -1, 0), (-1, -1, 0), (1, 0, -1), (1, -1, 1), (0, 1, 0),
              (0, 1, -1)}
    
    assert set(eom(3, maxnorm_value=1)) == answer  # Free rank 2

    
if __name__ == "__main__":
    import pytest
    # --durations=10  <- May be used to show potentially slow tests
    pytest.main(args=['.', '--doctest-modules', '-v'])