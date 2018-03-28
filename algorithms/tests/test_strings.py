#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test sequence algorithms.
"""

try:
    from ..strings import (longest_common_substring)
except ValueError:
    pass


def test_longest_common_substring():
    """
    Test longest consequtive increasing subsequence.
    """
    lca = longest_common_substring
    
    assert lca('ABCDGH', 'AEDFHR') == 'ADH'
    assert lca('AGGTAB', 'GXTXAYB') == 'GTAB'
    assert lca('XMJYAUZ', 'MZJAWXU') == 'MJAU'  # Test from wikipedia
    assert lca('XAXXXBXCXX', 'YYAYBC') == 'ABC'
    assert lca('eqrrafzwvvscxd', 'quaiizkwmmsx') == 'qazwsx'
    assert lca('DaFEnGswGer', 'answer') == 'answer'
    assert lca('acndswfferdk', 'ainoswpper') == 'answer'
    assert lca('DaFEnGswGer', '') == ''


if __name__ == "__main__":
    import pytest
    # --durations=10  <- May be used to show potentially slow tests
    pytest.main(args=['.', '--doctest-modules', '-v'])