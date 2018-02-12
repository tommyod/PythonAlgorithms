# PythonAlgorithms
Clean, educational implementations of vital algorithms in Python.

------

![](https://api.travis-ci.org/tommyod/PythonAlgorithms.svg?branch=master)

# Project overview

This project aims to provide clean, testing and well-documented implementations
of common and important algorithms in Python 3.6.

We strive to adhere to the following **rules**:

- **No imports**. Only Python standard library functions are used, except for 
  `pytest` for testing and `flake8` for PEP8 checking.
- Every algorithm must include **at least 3 doctests/examples**.
- Every algorithm must include **at least 5 test cases**, which should ideally 
  test edge cases.
- The **PEP8 style-guide** should be followed, this may be checked using the 
  `flake8` tool.

In addition, the following **guidelines** apply:

- Explicit variable names, detailed and concise inline comments. 
  Readability matters.
- Object orientation, generators, and so forth should be used when possible.
- Every algorithm should ideally include **at least one litterature** reference, 
  as well as algorithmic information about time and space usage.

# Contributing

You are encouraged to contribute, whatever your skill level is. Here's how to 
contribute:

1. Fork the project to your GitHub account.
2. Clone your fork to your local computer.
3. Add this to as upstream using `git remote add upstream https://github.com/tommyod/PythonAlgorithms.git`
4. Make your contribution to the project. Add tests, keep it clean, and follow 
   the rules outlined above.
5. Install flake8 using `pip install flake8`, then run 
   `flake8 --show-source --ignore=F811,W293,W391,W292,W291`. 
   Make sure there are no errors.
6. Run the tests using `pytest --doctest-modules -v`. Tests should run quickly, 
   and every algorithm should include at least 5 tests and 2 doctests.
7. Run `git fetch upstream` to get the lastest changes from upstream (this repo),
   then run `git rebase upstream/master` to rebase your changes on top of this 
   repo.
8. Create a pull request. Write in detail about what you did.

For more detailed information about how to contribute to an open source project,
see the 
[pandas docs](https://pandas.pydata.org/pandas-docs/stable/contributing.html), 
[scikit-learn docs](http://scikit-learn.org/stable/developers/contributing.html) and the 
[git book](https://git-scm.com/book/en/v2).

# Algorithms to implement

Here's a list of algorithms that should be considered.
For more information, see this [list of algorithms](https://en.wikipedia.org/wiki/List_of_algorithms) from Wikipedia.
Although the code quality is dubious, [GeeksforGeeks](https://www.geeksforgeeks.org/fundamentals-of-algorithms/) has a list of algorithms.
Some "competing" GitHub repos are [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) and
[keon/algorithms](https://github.com/keon/algorithms), but again the code quality is debatable.

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

- [X] Fibonacci
- [ ] Binomial coeffs
- [ ] Prime numbers (generating primes)
- [ ] Prime factorization (factorize an integer)
- [ ] Extended Euclidean algorithm
- [ ] Optimal matrix multiplication (p.362 Halim)
- [ ] Primality testing (test if a number is prime)

## Knapsack problems

- [ ] Maximal subset sum (weights equal values)
- [ ] Knapsack with repetition
- [ ] Knapsack without repetition

## Sequences and strings

- [ ] Longest common substring
- [ ] KMP algorithm
- [ ] Edit distance
- [ ] Edit /w custom error function (i.e. wrong typing keyboard)
- [X] Running average
- [ ] Coin change (Halim p.109)
- [ ] Longest increasing subsequence
- [ ] Maximal range sum (Halim p.103)

## Geometry

- [X] Closest pairs of points on the line
- [ ] Closest pairs of points in the plane
- [ ] Interval covering (p.91 Halim)
- [ ] Elements by maxnorm

## Sorting and order statistics
- [ ] Bucket sort
- [ ] Mergesort
- [ ] Median finding in linear time (p.215 in Cormen)
