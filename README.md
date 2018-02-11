# PythonAlgorithms
Clean, educational implementations of vital algorithms in Python.

------

![](https://api.travis-ci.org/tommyod/PythonAlgorithms.svg?branch=master)



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
