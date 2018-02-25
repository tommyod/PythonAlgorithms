#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sandbox file for testing speed of primes generators.
"""

import time


def primes_naive(n):
    """
    A very naive primes algorithm.
    """
    for i in range(2, n + 1):
        
        # Assume it's not divisible
        divisible = False
        for j in range(2, i):

            # If a divisor is found, it's not prime
            if i % j == 0:
                divisible = True
                break
            
        # If it's not divisible, yield it
        if not divisible:
            yield i


def primes_odds_sqrt(n):
    """
    A slightly smarter primes algorithm, considering only odds,
    and only up to sqrt(i).
    
    For more, smarter code, see:
    http://archive.oreilly.com/pub/a/python/excerpt/
    pythonckbk_chap1/index1.html?page=last
    """
    if n >= 2: 
        yield 2

    for i in range(3, n + 1, 2):
        
        # Assume it's not divisible
        divisible = False
        for j in range(3, int(i**0.5 + 1), 2):

            # If a divisor is found, it's not prime
            if i % j == 0:
                divisible = True
                break
            
        # If it's not divisible, yield it
        if not divisible:
            yield i


if __name__ == "__main__":
    """
    Test algorithm speeds.
    """

    n = 10000
    algorithms = [primes_odds_sqrt]
    results = [None for i in algorithms]
    
    for i, algorithm in enumerate(algorithms):
        start_time = time.perf_counter()
        results[i] = list(algorithm(n))
        timed = round(time.perf_counter() - start_time, 5)
        print('Algorithm "{}" ran in {} s'.format(algorithm.__name__, timed))
         
    assert all(r == results[0] for r in results)
 