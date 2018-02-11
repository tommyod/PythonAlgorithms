# PythonAlgorithms
Clean, educational implementations of vital algorithms in Python.

------

![](https://api.travis-ci.org/tommyod/PythonAlgorithms.svg?branch=master)

# Project overview

Implementations of algorithms in Python 3.6.

The following rules apply:

- Only Python standard library functions are used, except for `pytest` for testing and `flake8` for PEP8 checking.
- Every public function and method must include **at least 3 doctests/examples**.
- Every algorithm must include **at least 5 test cases**, which should test edge cases.

The following guidelines apply:

- The PEP8 style should be used, this may be checked using the `flake8` tool.
- Object orientation, generators, and so forth should be used when possible.
- Every algorithm should include **at least one litterature** reference, as well as algorithmic information.

# Contributing

Here's how to contribute:

1. Fork the project to your GitHub account.
2. Clone your fork to your local computer.
3. Add this to as upstream using `git remote add upstream https://github.com/tommyod/PythonAlgorithms.git`
4. Make your contribution to the project. Add tests, keep it clean.
5. Install flake8 using `pip install flake8`, then run `flake8 --show-source --ignore=F811,W293,W391,W292`. Make sure there are no errors.
6. Run the tests using `pytest --doctest-modules -v`. Testing should be fast, and every algorithm should include at least 5 tests.
7. Run `git fetch upstream` to get the lastest changes from upstream (this repo),
   then run `git rebase upstream/master` to rebase your changes on top of this repo.
8. Create a pull request.

# Algorithms to implement

Here's a list of algorithms that should be considered.
For more information, see this [list of algorithms](https://en.wikipedia.org/wiki/List_of_algorithms) from Wikipedia.

## Graphs and networks

- [ ] Representation: directed graphs
- [ ] Representation: undirected graphs
- [ ] Representation: networks (graphs with edges)
- [ ] DFS
- [ ] BFS
- [ ] Connected components
- [ ] Minimum spanning tree
- [ ] Checking if bipartite
- [ ] Topological sorting of a DAG
- [ ] Maximu flow / Ford-Fulkerson algorithm

## Mathematics

- [ ] Fibonacci
- [ ] Binomial coeffs
- [ ] Prime numbers
- [ ] Prime factorization
- [ ] Extended Euclidean algorithm
- [ ] Optimal matrix multiplication
- [ ] Primality testing
- [ ] Generating primes

## Knapsack problems

- [ ] Maximal subset sum (weights equal values)
- [ ] Knapsack with repetition
- [ ] Knapsack without repetition

## Strings and sequences

- [ ] Longest common substring
- [ ] KMP algorithm
- [ ] Edit distance
- [ ] Edit /w custom error function (i.e. wrong typing keyboard)
- [ ] Running average

## Geometry

- [ ] Closest pairs of points on the line
- [ ] Closest pairs of points in the plane

## Sorting and order statistics
- [ ] Bucket sort
- [ ] Mergesort
- [ ] Median finding in linear time (p.215 in Cormen)
