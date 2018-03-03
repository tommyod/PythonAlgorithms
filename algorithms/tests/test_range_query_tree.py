#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test sequence algorithms.
"""
import pytest

try:
    from ..range_query_tree import RQT
except ValueError:
    pass


class TestRQT(object):
    
    def test_range_sums(self):
        """
        Test some range sum examples.
        """
        
        rqt = RQT([1, 2, 3, 4, 5])
        
        assert rqt.query(0, 1) == 3
        assert rqt.query(0, 0) == 1
        assert rqt.query(1, 3) == 2 + 3 + 4

        rqt[1] = 3

        assert rqt.query(0, 1) == 4
        assert rqt.query(1, 3) == 3 + 3 + 4
        
    def test_range_products(self):
        """
        Test some range product examples.
        """
        import operator
        
        rqt = RQT([1, 2, 3, 4, 5], operator.mul, 1)
        
        assert rqt.query(0, 1) == 2
        assert rqt.query(0, 0) == 1
        assert rqt.query(1, 3) == 2 * 3 * 4

        rqt[1] = 3

        assert rqt.query(0, 1) == 3
        assert rqt.query(1, 3) == 3 * 3 * 4
        
    def test_range_min(self):
        """
        Test some range min examples.
        """
        def minimum(a, b):
            return min(a, b)

        identity = float('inf')
        rqt = RQT([5, 1, 9], minimum, identity)
        
        assert rqt.query(0, 0) == 5
        assert rqt.query(1, 2) == 1
        assert rqt.query(0, 2) == 1

        rqt[0] = 3
        rqt[1] = 6
        rqt[2] = 9

        assert rqt.query(0, 1) == 3
        assert rqt.query(1, 1) == 6
        assert rqt.query(1, 2) == 6
        
    def test_range_max(self):
        """
        Test some range max examples.
        """
        def maximum(a, b):
            return max(a, b)
        
        identity = -float('inf')
        rqt = RQT([2, 8, 6, 4, 7, 9], maximum, identity)
        
        assert rqt.query(0, 1) == 8
        assert rqt.query(3, 5) == 9
        
    def test_indices_updating(self):
        """
        Make sure only correct indices can be updated.
        """
        rqt = RQT([1, 2, 3])
        
        with pytest.raises(IndexError):
            rqt.update(-1, 10)
            
        with pytest.raises(IndexError):
            rqt.update(3, 10)
            
    def test_indices_query(self):
        """
        Make sure query indices make sense.
        """
        rqt = RQT([1, 2, 3])
        
        with pytest.raises(IndexError):
            rqt.query(-1, 2)
            
        with pytest.raises(IndexError):
            rqt.query(1, 3)
            
        with pytest.raises(IndexError):
            rqt.query(-5, 5)
            
        with pytest.raises(IndexError):
            rqt.query(2, 1)


if __name__ == "__main__":
    import pytest
    #  --durations=10  <- May be used to show potentially slow tests
    pytest.main(args=['.', '--doctest-modules', '-v'])