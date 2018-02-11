#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 21:13:49 2018

@author: tommy
"""

PRINTING = False


def closest_pair_line(sequence):
    """
    Return the two closest points in a sequence, i.e. the two points such that
    their difference is minimized.
    
    Algorithmic details
    -------------------
    Memory: O(n)
    Time: O(n * log(n))
    where n is the length of the sequence.
    
    Examples
    --------
    >>> closest_pair_line([0, 25, 50, 22, 75, 100])
    (22, 25)
    
    >>> closest_pair_line([100, 0, -100, 50, -50, -98])
    (-100, -98)
    
    References
    ----------
    [1] ...
    """
    len_sequence = len(sequence)
    
    # Make sure the input makes sense
    if len_sequence < 2:
        raise ValueError('Sequence length must at least be 2.')
    
    # Sort the sequence, get a list of tuples with (value, old_index).
    # We need the indicies to look up the values later on.
    sorted_seq = sorted((val, index) for (index, val) in enumerate(sequence))
    sorted_v = list((val) for (val, index) in sorted_seq)
    
    # Compute the differences in the sorted sequence, keep track of indices
    range_gen = range(1, len_sequence)
    diff_gen = ((sorted_v[i] - sorted_v[i - 1], (i, i - 1)) for i in range_gen)
    
    # Compute the minimum value and the minimal indices
    min_value, (i, j) = min(diff_gen)
    
    # Use the indices to get the actual values and return in canonical order
    answer_tuple = (sorted_v[i], sorted_v[j])
    return (min(answer_tuple), max(answer_tuple))


if __name__ == "__main__":
    import pytest
    # --durations=10  <- May be used to show potentially slow tests
    pytest.main(args=['.', '--doctest-modules', '-v'])