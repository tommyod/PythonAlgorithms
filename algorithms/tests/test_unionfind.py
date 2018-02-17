#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for the union find data structure.
"""

try:
    from ..unionfind import UnionFind
except ValueError:
    pass


def test_unionfind_basics():
    """
    Test the basic properties of unionfind.
    """
    
    u = UnionFind([1, 2, 3])
    assert u.in_same_set(1, 2) is False
    assert u.in_same_set(2, 3) is False
    
    u.union(1, 3)
    assert u.in_same_set(1, 2) is False
    assert u.in_same_set(3, 1)
    assert u.get_root(1) == u.get_root(3)


def test_unionfind_adding_elements():
    """
    Test adding operations, mostly syntactic sugar.
    """
    
    u = UnionFind([1, 2])
    u.add(['a', 'b'])
    
    assert 1 in u
    assert 'a' in u


def test_unionfind_example():
    """
    Test on a slightly more invovled example.
    """
    
    u = UnionFind([1, 2, 3, 4, 5])
    u.union(1, 3)
    u.union(2, 4)
    
    assert u.in_same_set(1, 3)
    assert u.in_same_set(4, 2)
    
    assert not u.in_same_set(2, 5)
    assert not u.in_same_set(2, 1)
    assert not u.in_same_set(1, 4)
    
    u.union(5, 1)
    assert u.in_same_set(3, 5)


def test_unionfind_several():
    """
    Test that we can take union of more than two elements.
    """
    
    u = UnionFind([1, 2, 3, 4, 5, 6, 7, 8])
    u.union([1, 2, 3])
    u.union([4, 5, 6])
    u.union([7, 8])
    
    assert u.in_same_set(1, 3)
    assert u.in_same_set(6, 4)
    assert u.in_same_set(7, 8)
    
    assert not u.in_same_set(2, 5)
    assert not u.in_same_set(4, 8)

    
if __name__ == "__main__":
    import pytest
    # --durations=10  <- May be used to show potentially slow tests
    pytest.main(args=['.', '--doctest-modules', '-v'])