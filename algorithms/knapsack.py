#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Knapsack algorithms.
"""

import itertools


def knapsack_without_repetition(capacity, values, weights=None):
    """
    Find the optimal set of items with values and weights, to fill a knapsack
    to maximal capacity.
    
    The knapsack has a capacity which limits our choice of items in such a way 
    that the sum of the items' weights can not exceed the knapsack capacity.
    
    Parameters
    ----------
    capacity : int
        An integer specifying the total capacity of the knapsack.
    values : iterable
        An iterable containing the value of each of the items.
    weights : iterable
        An iteratble containing the weight of each of the items.
        
    Returns
    -------
    ietrable : Indices of the items contained in the maximal value knapsack.
    numeric : The value of the maximal value knapsack.
    
    Algorithmic details
    -------------------
    Memory: O(W * n)
    Time: O(W * n)
    where W is the capacity of the knapsack and n is the number of items.
    
    Examples
    --------
    >>> knapsack_without_repetition(5, [100, 100, 1], [10, 10, 1])
    (1, [2])
    
    >>> knapsack_without_repetition(20, [100, 100, 1], [10, 10, 1])
    (200, [0, 1])
    
    References
    ----------
    [1] http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani
        .pdf#page=171&zoom=auto,-255,792
    [2] https://en.wikipedia.org/wiki/Knapsack_problem
    """
    
    # If no weights are specified, we set weights equal to values
    if not weights:
        weights = values.copy()
    
    # Make sure that the input is reasonable
    if len(values) != len(weights):
        msg = 'Size of values and weights iterables should be equal'
        raise ValueError(msg)
    
    # Create dp-table and list for retrieving the items chosen.
    number_of_items = len(values)
    table = [[0 for item in range(number_of_items + 1)] 
             for knapsack_weight in range(capacity + 1)]
    previous = dict()
    
    # Calculate maximal value knapsack            
    product = itertools.product(range(1, number_of_items + 1), 
                                range(1, capacity + 1))
    
    for item, knapsack_weight in product:
            
        # Get value and weight of current item
        item_value = values[item - 1]
        item_weight = weights[item - 1]
        
        # Set current knapsack equal to previous knapsack (not containing
        # current item)
        table[knapsack_weight][item] = table[knapsack_weight][item - 1]
        previous[(knapsack_weight, item)] = (knapsack_weight, item - 1)
        
        # Check if possible to add current item to the knapsack
        if knapsack_weight - item_weight >= 0:
            item_added = (table[knapsack_weight - item_weight][item - 1] + 
                          item_value)
            
            # If adding the current item to the knapsack will not increace the
            # knapsack value, we continue without adding it
            if item_added <= table[knapsack_weight][item]:
                continue
            
            # Add current item to knapsack
            table[knapsack_weight][item] = item_added
            previous[(knapsack_weight, item)] = (knapsack_weight - 
                                                 item_weight, item - 1)
    
    # Retrieve the content og the maximal value knapsack by backtracking
    content = []
    weight, item = capacity, number_of_items
    while weight != 0 and item != 0:
        previous_weight, previous_item = previous[(weight, item)]
        
        # Add 'item - 1' to content if it was added in the dp-table.
        if previous_weight < weight:
            content.append(item - 1)
        
        weight, item = previous_weight, previous_item

    # Get maximal value
    max_value = table[capacity][number_of_items]
    
    return max_value, sorted(content)


if __name__ == "__main__":
    import pytest
    print(knapsack_without_repetition(10, [9, 14, 16, 30], [2, 3, 4, 6]))
    # --durations=10  <- May be used to show potentially slow tests
    pytest.main(args=['.', '--doctest-modules', '-v'])