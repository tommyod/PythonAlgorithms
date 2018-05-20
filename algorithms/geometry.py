#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Geometry algorithms.
"""

import itertools


def closest_pair_line(sequence):
    """
    Return the indices of the two closest points in a sequence, i.e. the two 
    points such that their difference is minimized.
    
    Algorithmic details
    -------------------
    Memory: O(n)
    Time: O(n * log(n))
    where n is the length of the sequence.
    
    Examples
    --------
    >>> closest_pair_line([0, 25, 50, 22, 75, 100])
    (1, 3)
    
    >>> closest_pair_line([100, 0, -100, 50, -50, -98])
    (2, 5)
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
    
    # Use the indices to look up the unsorted indices
    answer_tuple = (sorted_seq[i][1], sorted_seq[j][1])
    return (min(answer_tuple), max(answer_tuple))


def elements_of_maxnorm(free_rank, maxnorm_value):
    """
    Yield every element of Z^r such that max_norm(element) = maxnorm_value.
    
    Parameters
    ----------
    free_rank : int
        The free rank (like dimension) of Z^r, i.e. free_rank = r.
    maxnorm_value : int
        The value of the maximum norm of the elements generated.
        
    Yields
    -------
    tuple
        Elements in Z^r that satisfy the norm criterion.
        
    Algorithmic details
    -------------------
    Memory: O((2 * m + 1)^(f-1))
    Time: O(f * (2m)^(f-1)) to compute every value
    where f is the free rank and m is the maxnorm value.
        
    Examples
    ---------
    >>> free_rank = 3 # Like dimension
    >>> maxnorm_value = 4
    >>> elements = list(elements_of_maxnorm(free_rank, maxnorm_value))
    >>> # Verify that the max norm is the correct value
    >>> all(max(abs(k) for k in e) for e in elements)
    True
    
    >>> # Verify the number of elements
    >>> n = maxnorm_value
    >>> len(elements) == ((2*n + 1)**free_rank - (2*n - 1)**free_rank)
    True
    """
    if maxnorm_value == 0:
        yield tuple([0] * free_rank)
        return

    # There are two 'walls' per dimension, front and back
    for wall in range(free_rank):

        # In each wall, the boundaries must shrink, two at a time
        boundary_reduced = [1] * wall + [0] * (free_rank - wall - 1)

        # The arguments into the cartesian product
        prod_arg = [range(-maxnorm_value + k, maxnorm_value + 1 - k)
                    for k in boundary_reduced]

        # Take cartesian products along the boundaries of the r-dimensional
        # cube. Yield from opposite sides of the hypercube.
        for boundary_element in itertools.product(*prod_arg):
            start, end = boundary_element[:wall], boundary_element[wall:]
            yield start + (maxnorm_value,) + end
            yield start + (-maxnorm_value,) + end
            
            
def area_of_polygon(list_of_points):
    """
    Return the signed area of a simple polygon.
    
    See http://geomalgorithms.com/a01-_area.html for a discussion.
    
    Parameters
    ----------
    list_of_points : list
        A list of points in counterlockwise order, 
        i.e. [(0, 0), (1, 0), (1, 1)].
        
    Returns
    -------
    float
        The signed area. Positive if the points are given in counter clockwise
        order. Negative if the points are given in clockwise order.
        
    Algorithmic details
    -------------------
    Memory: O(1)
    Time: O(n)
    where n is the number of points.
        
    Examples
    ---------
    >>> points = [(0, 0), (1, 0), (1, 1)]
    >>> area_of_polygon(points)
    0.5
    
    >>> points = [(0, 1), (3, 2), (2, 5), (-1, 6), (-2, 3)]
    >>> area_of_polygon(points)
    16.0
    """
    
    def area_of_segment(arr, i, n):
        """
        Length of a single segment in the sum.
        """
        return arr[i % n][0] * (arr[(i + 1) % n][1] - arr[(i - 1) % n][1])
    
    n = len(list_of_points)
    return sum(area_of_segment(list_of_points, i, n) for i in range(n)) / 2


if __name__ == "__main__":
    import pytest
    # --durations=10  <- May be used to show potentially slow tests
    pytest.main(args=['.', '--doctest-modules', '-v'])
    
    