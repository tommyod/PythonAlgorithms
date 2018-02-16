#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test undirected graphs.
"""

import pytest

try:
    from ..graph_undirected import UndirectedGraph
except ValueError:
    pass


def test_initialization_of_graphs():
    """
    Test initialization of graphs.
    """
    g = UndirectedGraph([('A', 2), (2, 'B'), ('B', 'C')])
    h = UndirectedGraph([('A', 2), ('B', 'C'), (2, 'B')])
    assert g == h
    
    # Raises ValueError since there are too few weights
    with pytest.raises(ValueError):
        g = UndirectedGraph([('A', 2), (2, 'B'), ('B', 'C')], [1, 2])
        
    g = UndirectedGraph([('A', 2), ('B', 'C'), ('B', 'C')], [1, 2, 2])
    assert g.weight(('B', 'C')) == 2


def test_minimum_spanning_tree():
    """
    Test minimum spanning tree implementation on simple examples.
    """
    
    # A very simple graph
    g = UndirectedGraph([('A', 'B'), ('B', 'D'), ('D', 'C'), ('A', 'C')], 
                        weights=[7, 6, 2, 3])
    mst = g.minimum_spanning_tree('A')
    assert mst == UndirectedGraph([('B', 'D'), ('D', 'C'), ('A', 'C')], 
                                  weights=[6, 2, 3])
    
    # A slightly more complicated graph
    g = UndirectedGraph([('A', 'B'), ('B', 'D'), ('D', 'C'), ('A', 'C'),
                         ('C', 'B'), ('A', 'D')], 
                        weights=[7, 6, 2, 3, 2, 1])
    mst = g.minimum_spanning_tree('A')
    assert mst == UndirectedGraph([('D', 'C'), ('C', 'B'), ('A', 'D')], 
                                  weights=[2, 2, 1])
    

if __name__ == "__main__":
    import pytest
    # --durations=10  <- May be used to show potentially slow tests
    pytest.main(args=['.', '--doctest-modules', '-v'])
    