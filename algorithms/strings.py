#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
String algorithms.
"""

import collections

PRINTING = False


def pprint(*args, **kwargs):
    """
    Printing which can be turned off or on globally. For debugging and
    learning.
    """
    if PRINTING:
        print(*args, **kwargs)


def longest_common_substring(string_a, string_b):
    """
    Find the longest common substring of `string_a` and `string_b`.
    
    This well-known string algorithm uses dynamic programming to compute the
    longest common substring. The substring does not have to be consequtive in
    either of the two input strings.

    Parameters
    ----------
    string_a : str
        A string.
    string_b : str
        A string.
        
    Returns
    -------
    str : The longest common substring of `string_a` and `string_b`.
    
    Algorithmic details
    -------------------
    Memory: O(nm)
    Time: O(nm)
    where n and m are the lengths of the two strings.
    
    Examples
    --------
    >>> longest_common_substring('aabkc', 'afbcg')
    'abc'
    
    >>> longest_common_substring('abc', 'auboc')
    'abc'

    
    References
    ----------
    [1] https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
    """
    
    # Make sure the input is reasonable
    if not isinstance(string_a, (str,)) or not isinstance(string_b, (str,)):
        raise TypeError('Strings must be passed.')
        
    # If either string is empty, return an empty string
    if not string_a or not string_b:
        return ''
    
    # DP table for the length of the longest common substring, as well as a
    # DP table to keep track of the previous value, used to reconstruct the
    # answer
    len_substring = collections.defaultdict(int)
    previous = collections.defaultdict(lambda: None)
    
    for i, a in enumerate(string_a):
        for j, b in enumerate(string_b):
            
            # If the strings match at the indices, then the longest common
            # substring must be what it was at the previous letters, plus one
            if a == b:
                len_substring[(i, j)] = 1 + len_substring[(i - 1, j - 1)]
                previous[(i, j)] = (i - 1, j - 1)
                continue
                
            # If the strings do not match, then the longest common substring
            # must be the previous best answers without one of the last chars
            if len_substring[(i - 1, j)] >= len_substring[(i, j - 1)]:
                len_substring[(i, j)] = len_substring[(i - 1, j)]
                previous[(i, j)] = (i - 1, j)
            else:
                len_substring[(i, j)] = len_substring[(i, j - 1)]
                previous[(i, j)] = (i, j - 1)
    
    # Having filled the DP table, we now reconstruct the answer by moving back
    # up to the start, noting when we move nortwest. When we do, we added a
    # new character to the longest common substring, and we add this to the
    # answer too.
    answer = ''
    while (i >= 0) and (j >= 0):
        i_prev, j_perv = previous[(i, j)]
        if (i_prev, j_perv) == (i - 1, j - 1):
            answer += string_a[i]
        (i, j) = i_prev, j_perv
        
    # Reverse the answer and return it
    return ''.join(char for char in reversed(answer))


if __name__ == "__main__":
    import pytest
    # --durations=10  <- May be used to show potentially slow tests
    pytest.main(args=['.', '--doctest-modules', '-v'])