#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementation of a range query tree.
This data structure allows fast queries about min/max/sum over a range.
"""

import operator
import math


class RQT(object):
    
    def __init__(self, sequence, function=operator.add, function_identity=0):
        """
        Data structure for efficient range queries.
        
        This data structure allows efficient ...
        
        Examples
        --------
        >>> # Range query tree with sums over a range (default behaviour)
        >>> rqt = RQT([6, 2, 4, 9])
        >>> rqt
        [6, 2, 4, 9]
        >>> rqt.query(0, 1)
        8
        >>> rqt.query(2, 3)
        13
        
        >>> # Range query tree with maximums over a range
        >>> rqt = RQT([6, 2, 4, 9], lambda i, j: max(i, j), -float('inf'))
        >>> rqt.query(0, 1)
        6
        >>> rqt.query(1, 3)
        9
        """
        # Store input information
        self._function = function
        self._identity = function_identity
        self._original_length = len(sequence)
    
        # Create an internal list to represent the tree. The length must be
        # enough to accomodate the parent nodes, and the tree is padded so that
        # it's length is a power of two. The default values are the identity.
        self.tree_size = 2**(math.ceil(math.log2(self._original_length)) + 1)
        self.seq = [self._identity for i in range(self.tree_size)]
        
        # Set the last elements equal to the sequence provided by the user
        slice_obj = slice(self.tree_size // 2, 
                          self.tree_size // 2 + self._original_length)
        self.seq[slice_obj] = sequence
        
        # Apply the input function to fill the parent nodes (first half)
        for i in range(self.tree_size // 2 - 1, -1, -1):
            self.seq[i] = self._function(*self._children(i))
            
    def _parent(self, i):
        """
        Return the index of the parent in the internal sequence.
        """
        return math.floor(i / 2)
            
    def update(self, index, value):
        """
        Update a value in the range query tree.
        
        Examples
        --------
        >>> rqt = RQT([6, 2, 4, 9])
        >>> rqt
        [6, 2, 4, 9]
        >>> rqt.update(1, 10)
        >>> rqt
        [6, 10, 4, 9]
        >>> # Indices must be withing range
        >>> rqt.update(4, 10)
        Traceback (most recent call last):
        ...
        IndexError: list assignment index out of range
        """
        if not (0 <= index < self._original_length):
            raise IndexError('list assignment index out of range')
        i = self._internal_index(index)
        
        # Update the node
        self.seq[i] = value
        p_i = self._parent(i)
        
        # Go up the tree and update the parents
        while p_i != 0:
            children = self._children(p_i)
            self.seq[p_i] = self._function(*children)
            p_i = self._parent(p_i)
            
    def __setitem__(self, index, value):
        self.update(index, value)
        
    def __getitem__(self, index):
        return self.seq[self._internal_index(index)]
            
    def query(self, i, j):
        """
        Query for the function over seq[i:j+1].
        
        Examples
        --------
        >>> rqt = RQT([6, 2, 4, 9])
        >>> rqt.query(0, 1)
        8
        >>> rqt.query(1, 2)
        6
        """
        
        # Perform an input check
        if not (0 <= i < self._original_length):
            raise IndexError('list index out of range')
            
        if not (0 <= j < self._original_length):
            raise IndexError('list index out of range')
            
        if j < i:
            raise IndexError('start index cannot be greater than end index')
            
        # Query the top node
        return self._query_node(1, i, j)
        
    def _node_info(self, i):
        """
        Return information about node number i.
        """
        # The level of the tree. The root is level 0, it's 2 children are
        # located at level 1, grandchildren at level 3, and so forth
        level = math.floor(math.log2(i))
        
        # The right-most range covered by the left-most node at each level
        rm = 2**(math.ceil(math.log2(self._original_length)) - level) - 1
        
        # The number of nodes at the level of node i
        num = (i - 2 ** level)
        
        # The indices (external) of the range covered by node i, inclusive
        node_min = num * (rm + 1)
        node_max = rm + node_min
        return level, node_min, node_max, num
        
    def _query_node(self, node, i, j):
        """
        Recursive function for node queries.
        """
        # Get information about the node
        level, node_min, node_max, num = self._node_info(node)

        # The query range seq[i...j] is within the interval covered by the
        # node. Return the value of the node.
        if i <= node_min and j >= node_max:
            return self.seq[node]
        
        # No part of the query range seq[i...j] is covered by this node
        if (i > node_min and i > node_max) or (j < node_min and j < node_max):
            return self._identity
        
        # Some part of the query range seq[i...j] is covered by this node.
        # Get information from the children
        result_child_l = self._query_node(2 * node, i, j)
        result_child_r = self._query_node(2 * node + 1, i, j)
        return self._function(result_child_l, result_child_r)
 
    def _children(self, i_internal):
        return self.seq[2 * i_internal], self.seq[2 * i_internal + 1]
    
    def _internal_index(self, i_external):
        return i_external + self.tree_size // 2
        
    def __repr__(self):
        slice_obj = slice(self.tree_size // 2, 
                          self.tree_size // 2 + self._original_length)
        
        return repr(self.seq[slice_obj])
        

if __name__ == "__main__":
    import pytest
    # --durations=10  <- May be used to show potentially slow tests
    pytest.main(args=['.', '--doctest-modules', '-v'])
    


