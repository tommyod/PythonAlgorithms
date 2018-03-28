#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sequence algorithms.
"""

import collections
import itertools
import operator

PRINTING = False


def pprint(*args, **kwargs):
    """
    Printing which can be turned off or on globally. For debugging and
    learning.
    """
    if PRINTING:
        print(*args, **kwargs)


def fibonacci_order_n(n, terms=5):
    """
    Yields the first t terms in the generalized Fibonacci numbers of order n.
    
    We define the generalized Fibonacci numbers of order n by the recursion:
    F(0 ... n) = 1
    F(i) = F(i - 1) + F(i - 2) + F(i - n)
    
    Algorithmic details
    -------------------
    Memory: O(t)
    Time: O(nt)
    where n is the order and t is the number of terms.
    
    Examples
    --------
    >>> list(fibonacci_order_n(2, terms = 8))
    [1, 1, 2, 3, 5, 8, 13, 21]
    
    >>> list(fibonacci_order_n(4, terms = 10))
    [1, 1, 1, 1, 4, 7, 13, 25, 49, 94]
    
    References
    ----------
    [1] ...
    """
    
    # Initialize a partial sequence, i.e. variables to keep track of.
    # Since F(i) = F(i - 1) + F(i - 2) + F(i - n), we only keep n variables.
    partial_sequence = collections.deque([1] * n)
    
    # Yield the variables in the partial sequence
    for i, value in enumerate(partial_sequence, start=1):
        if i > terms:
            return
        yield value
    
    # Start yielding, summing and exchanging in a queue-structure
    while True:
        i += 1
        next_value = sum(partial_sequence)
        
        # Add a break criterion to help the user, making it harder to
        # generate an infinite stream of elements
        if i > terms:
            return
            
        yield next_value
        partial_sequence.popleft()
        partial_sequence.append(next_value)


def maximums_from_left(iterable):
    """
    Yields (index, num) of the maximums as encountered from the left of the
    sequence. This function answers the question "How many times has the stock
    market been at an all-time high?"
    
    Algorithmic details
    -------------------
    Memory: O(1)
    Time: O(n)
    where n is the length of the sequence.
    
    Examples
    --------
    >>> sequence = [1, 3, 2, 4, 4, 3, 5]
    >>> list(maximums_from_left(sequence))
    [(0, 1), (1, 3), (3, 4), (4, 4), (6, 5)]
    """
    
    # Convert to an iterable
    iterable = iter(iterable)
    
    # Initialize DP-variable to the first value, which is the maximum so far
    max_so_far = next(iterable)
    yield 0, max_so_far
    
    # Iterate over the sequence, yield if higher than what's seen
    for i, number in enumerate(iterable, 1):
        if number >= max_so_far:
            max_so_far = number
            yield i, max_so_far


def longest_conseq_inc_subsequence(iterable, only_length=True):
    """
    Returns the longest consequtive (non-monotonically) increasing subsequence
    of an iterable. A non-monotonically increasing subsequence is a sequence
    such as [0, 3, 4, 4, 6].
    
    Parameters
    ----------
    only_length : bool
        Whether to return only the length of the subsequence, or the
        subsequence itself.
    
    Algorithmic details
    -------------------
    Memory: O(n)
    Time: O(n)
    where n is the length of the sequence.
    
    Examples
    --------
    >>> sequence = iter([0, 1, 0, 1, 2, 3, 0, 1, 2])
    >>> longest_conseq_inc_subsequence(sequence, only_length = False)
    [0, 1, 2, 3]
    
    >>> sequence = [2, 4, 0, 1, 2, 3, -1, 4, 5, 6]
    >>> longest_conseq_inc_subsequence(sequence, only_length = True)
    4
    """

    iterable = iter(iterable)
    
    # Initialize the counters and the lists used to keep track of lengths
    streak_seq_count = 1
    longest_seq_count = 1
    prev_value = next(iterable)
    streak_seq = [prev_value]
    longest_seq = [prev_value]
    
    # Go through the iterable
    for value in iterable:
        
        # If the current value is greater than or equal to the previous one,
        # add to the streak and increment the counter
        if value >= prev_value:
            streak_seq.append(value)
            streak_seq_count += 1
            
        # If the current value is smaller than the previous one,
        # restart the streak counter and the streak sequence
        else:
            streak_seq_count = 1
            streak_seq = [value]
            
        # If the streak is longer than the longest sequence seen,
        # store it. If not, then the previous longest is still the longest
        if streak_seq_count > longest_seq_count:
            longest_seq_count = streak_seq_count
            longest_seq = streak_seq
        
        print_str = 'value{}. LCIS: {}, SSC: {}, streak: {}, longest : {}'
        pprint(print_str.format(value, longest_seq_count, streak_seq_count,
                                streak_seq, longest_seq))
        
        # Set the previous value to the current value, for the next loop
        prev_value = value
        
    if only_length:
        return longest_seq_count
    else:
        return longest_seq


def longest_inc_subsequence(iterable, only_length=True):
    """
    TODO
    0, 1, 2, 0, 1, 3, 4, 0, 5 -> 0, 1, 2, 3, 4, 5
    
    """
    pass


def running_mean(iterable, kind='arithmetic'):
    """
    Compute the running mean of an iterable. After `n` items, the mean
    of the first `n` items are yielded.
    
    Parameters
    ----------
    iterable : iterable
        An iterable object.
    kind : str
        The type of mean to compute, either `arithmetic` or `geometric`.
        
    Algorithmic details
    -------------------
    Memory: O(1)
    Time: O(n)
    where n is the length of the sequence.
    
    Examples
    --------
    >>> sequence = iter([1, 2, 3])
    >>> list(running_mean(sequence))
    [1.0, 1.5, 2.0]
    
    >>> sequence = iter([1, 2, 3])
    >>> list(running_mean(sequence, kind='geometric'))
    [1.0, 1.4142135623730951, 1.8171205928321397]
    
    >>> sequence = iter([1, 0, 5])
    >>> list(running_mean(sequence))
    [1.0, 0.5, 2.0]
    """
    
    iterable = iter(iterable)
    
    # Two kinds of means are implemented
    if kind == 'arithmetic':
        bin_op = operator.add
        bin_op_repeated = operator.mul
    elif kind == 'geometric':
        bin_op = operator.mul
        bin_op_repeated = operator.pow
    else:
        error_msg = 'Argument `kind` must be `arithmetic` or `geometric`.'
        raise ValueError(error_msg)
    
    # Iterate over all the elements
    generator = enumerate(itertools.accumulate(iterable, bin_op), start=1)
    for term, accumulated in generator:
        yield bin_op_repeated(accumulated, 1 / term)


def running_mean_bounded(iterable, kind='arithmetic'):
    """
    Altenrative implementation of the running mean where intermediate
    calculations are bounded. This implementation would be far more robust
    when computing the geometric mean of a NumPy array, where overflow can
    happen.
    
    Parameters
    ----------
    iterable : iterable
        An iterable object.
    kind : str
        The type of mean to compute, either `arithmetic` or `geometric`.
    
    Algorithmic details
    -------------------
    Memory: O(1)
    Time: O(n)
    where n is the length of the sequence.
    
    Examples
    --------
    >>> sequence = iter([1, 2, 3])
    >>> list(running_mean_bounded(sequence))
    [1, 1.5, 2.0]
    
    >>> sequence = iter([1, 2, 3])
    >>> list(running_mean_bounded(sequence, kind='geometric'))
    [1, 1.4142135623730951, 1.8171205928321397]
    
    >>> sequence = iter([1, 0, 5])
    >>> list(running_mean_bounded(sequence))
    [1, 0.5, 1.9999999999999998]
    """
    
    iterable = iter(iterable)
    
    # Two kinds of means are implemented
    if kind == 'arithmetic':
        bin_op = operator.add
        bin_op_repeated = operator.mul
    elif kind == 'geometric':
        bin_op = operator.mul
        bin_op_repeated = operator.pow
    else:
        error_msg = 'Argument `kind` must be `arithmetic` or `geometric`.'
        raise ValueError(error_msg)
    
    # The first value is just the first item in the iterable
    mean = next(iterable)
    yield mean
    
    # General formulas for computing means
    # Arithmetic: S_n = S_{n-1} * {(n-1)/n} + a_n * {1/n}
    # Geometric : S_n = S_{n-1} ^ {(n-1)/n} * a_n ^ {1/n}
    for n, item in enumerate(iterable, start=2):
        mean = bin_op(bin_op_repeated(mean, (n - 1) / n),
                      bin_op_repeated(item, 1 / n))
        yield mean


if __name__ == "__main__":
    import pytest
    # --durations=10  <- May be used to show potentially slow tests
    pytest.main(args=['.', '--doctest-modules', '-v'])