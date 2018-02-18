#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class for the union find algorithm.
"""

from collections.abc import Container
import functools


class UnionFind(Container):
    
    def __init__(self, iterable):
        """
        Initialize a collection of sets from an iterable object.
        
        The union–find data structure implements three primary methods, namely
        initialization, get_root and union. This data structure is used in 
        algorithms such as Kruskals algorithm for finding minimum spanning
        trees. See https://en.wikipedia.org/wiki/Disjoint-set_data_structure.
        
        Parameters
        ----------
        iterable : iterable
            An iterable containing hashable objects.
            
        Examples
        --------
        >>> unionfind = UnionFind(['a', 'b', 'c', 'd'])
        >>> unionfind.in_same_set('a', 'b')
        False
        >>> new_root = unionfind.union('a', 'b')
        >>> unionfind.in_same_set('a', 'b')
        True
        >>> new_root = unionfind.union('c', 'd')
        >>> unionfind.in_same_set('d', 'c')
        True
        >>> unionfind.in_same_set('a', 'c')
        False
        """
        self._parent = dict()
        self._rank = dict()
        
        for item in iterable:
            self._parent[item] = item
            self._rank[item] = 0
            
    def __contains__(self, item):
        """
        Whether an item is in the data structure.
        
        Examples
        --------
        >>> unionfind = UnionFind(['a', 'b'])
        >>> 'a' in unionfind
        True
        >>> 'd' in unionfind
        False
        """
        try:
            # If no errors are raised, it's in the data structure
            self._parent[item]
            self._rank[item]
            return True
        # If a KeyError is raised, then it was not found
        except KeyError:
            return False
    
    def add(self, iterable):
        """
        Add more items to the collection.
        
        Examples
        --------
        >>> unionfind = UnionFind(['a', 'b'])
        >>> 'c' in unionfind
        False
        >>> unionfind.add(['c', 'd'])
        >>> ('c' in unionfind) and ('d' in unionfind)
        True
        """
        for item in iterable:
            self._parent[item] = item
            self._rank[item] = 0

    def get_root(self, x):
        """
        Return the root of element `x`. Applies path compression along the way.
        
        Examples
        --------
        >>> elements = [1, 2, 3]
        >>> unionfind = UnionFind(elements)
        >>> unionfind.get_root(1)
        1
        >>> new_root = unionfind.union(1, 2)
        >>> unionfind.get_root(2)
        1
        >>> # The rank of 1 was increased, since it's a root for 2
        >>> [unionfind._rank[e] for e in elements]
        [1, 0, 0]
        >>> new_root = unionfind.union(2, 3)
        >>> unionfind.in_same_set(1, 3)
        True
        """
        
        # Initialize a chain of elements in the tree for which we will apply
        # path compression later on - speeing up subsequent lookups
        chain = set()
        
        # Get the parent of x. While it parent is not x, we are not at the root
        parent = self._parent[x]
        while x != parent:
            
            # Add `x` to the chain for processing later
            chain.add(x)
            x, parent = parent, self._parent[parent]
            
        # Apply path compression for every item encountered while looping
        # upwards to the root node
        for item in chain:
            self._parent[item] = x
        return x
    
    def in_same_set(self, x, y):
        """
        Whether or not two elements are in the same set.
        
        Examples
        --------
        >>> elements = ['A', 'Z']
        >>> unionfind = UnionFind(elements)
        >>> unionfind.in_same_set('A', 'Z')
        False
        >>> new_root = unionfind.union('A', 'Z')
        >>> unionfind.in_same_set('A', 'Z')
        True
        """
        return self.get_root(x) == self.get_root(y)
    
    def union(self, x, y=None):
        """
        Union of the sets containing x and y.
        
        Examples
        --------
        >>> elements = [1, 2, 3, 4, 5]
        >>> unionfind = UnionFind(elements)
        >>> new_root = unionfind.union([1, 2, 3])
        >>> unionfind.in_same_set(1, 3)
        True
        >>> new_root = unionfind.union(4, 5)
        >>> unionfind.in_same_set(1, 4)
        False
        >>> new_root = unionfind.union(1, 5)
        >>> unionfind.in_same_set(1, 4)
        True
        """
        # If an iterable was passed as the only argument, reduce it
        if y is None:
            return functools.reduce(self.union, x)
        
        # Two arguments were passed, apply the standard binary union algorithm
        root_x = self.get_root(x)
        root_y = self.get_root(y)
        
        # If the roots are equal, do nothing - the items are in the same set
        if root_x == root_y:
            return root_x
        
        # If the tree of x is of smaller rank than the tree of y, x should be
        # a sub tree of y
        if self._rank[root_x] < self._rank[root_y]:
            self._parent[root_x] = root_y
            return root_y
        # Opposite of the condition above
        elif self._rank[root_x] > self._rank[root_y]:
            self._parent[root_y] = root_x
            return root_x
        # The trees are of the same rank, choose y as a sub-tree of x randomly.
        # X is now of higher rank than before, so increment the counter.
        else:
            self._parent[root_y] = root_x
            self._rank[x] += 1
            return root_x


if __name__ == "__main__":
    import pytest
    # --durations=10  <- May be used to show potentially slow tests
    pytest.main(args=['.', '--doctest-modules', '-v'])
    
    