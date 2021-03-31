LeetCode
==============================
![CI](https://github.com/TeoZosa/leetcode/workflows/CI/badge.svg)
![codecov](https://codecov.io/gh/TeoZosa/leetcode/branch/master/graph/badge.svg?token=3HF21UWY82)
![License](https://img.shields.io/github/license/TeoZosa/leetcode?style=plastic)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![powered by semgrep](https://img.shields.io/badge/powered%20by-semgrep-1B2F3D?labelColor=lightgrey&link=https://semgrep.dev/&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAA0AAAAOCAYAAAD0f5bSAAAABmJLR0QA/gD+AP+cH+QUAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH5AYMEy0l8dkqrQAAAvFJREFUKBUB5gIZ/QEAAP8BAAAAAAMG6AD9+hn/GzA//wD//wAAAAD+AAAAAgABAQDl0MEBAwbmAf36GQAAAAAAAQEC9QH//gv/Gi1GFQEC+OoAAAAAAAAAAAABAQAA//8AAAAAAAAAAAD//ggX5tO66gID9AEBFSRxAgYLzRQAAADpAAAAAP7+/gDl0cMPAAAA+wAAAPkbLz39AgICAAAAAAAAAAAs+vU12AEbLz4bAAAA5P8AAAAA//4A5NDDEwEBAO///wABAQEAAP//ABwcMD7hAQEBAAAAAAAAAAAaAgAAAOAAAAAAAQEBAOXRwxUAAADw//8AAgAAAAD//wAAAAAA5OXRwhcAAQEAAAAAAAAAAOICAAAABP3+/gDjzsAT//8A7gAAAAEAAAD+AAAA/wAAAAAAAAAA//8A7ePOwA/+/v4AAAAABAIAAAAAAAAAAAAAAO8AAAABAAAAAAAAAAIAAAABAAAAAAAAAAgAAAD/AAAA8wAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAA8AAAAEAAAA/gAAAP8AAAADAAAA/gAAAP8AAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAA7wAAAPsAAAARAAAABAAAAP4AAAAAAAAAAgAAABYAAAAAAAAAAAIAAAD8AwICAB0yQP78/v4GAAAA/wAAAPAAAAD9AAAA/wAAAPr9//8aHTJA6AICAgAAAAD8AgAAADIAAAAAAP//AB4wPvgAAAARAQEA/gEBAP4BAQABAAAAGB0vPeIA//8AAAAAAAAAABAC+vUz1QAAAA8AAAAAAwMDABwwPu3//wAe//8AAv//ABAcMD7lAwMDAAAAAAAAAAAG+vU0+QEBAvUB//4L/xotRhUBAvjqAAAAAAAAAAAAAQEAAP//AAAAAAAAAAAA//4IF+bTuuoCA/QBAQAA/wEAAAAAAwboAP36Gf8bMD//AP//AAAAAP4AAAACAAEBAOXQwQEDBuYB/foZAAAAAAD4I6qbK3+1zQAAAABJRU5ErkJggg==)](https://semgrep.dev/)
[![Dependabot](https://api.dependabot.com/badges/status?host=github&repo=TeoZosa/leetcode)](https://dependabot.com/)


---

**Source Code**: [https://github.com/TeoZosa/leetcode](https://github.com/TeoZosa/leetcode)

---

Overview
--------
Miscellaneous coding challenge for the purpose of professional edification.

Solutions strive towards a balance of both optimality and "elegance"
(in other words, simple enough to understand and remember/easily triangulate)
with sufficiently succinct, collocated documentation and tests.

> 📝 **Note**  
>  Given the strictly pedagogical nature of this endeavor,
>  final solutions are **always** informed by preexisting implementations.
>  As such, I make no explicit claims of originality.

### Project Structure
The project files are organized under problem source namespaces
(i.e., educative.io, leetcode, etc.)
and further organized into ad-hoc categories.

At the module-level, files are:
- Prefixed with their problem number
  (the canonical number if one exists, by order of introduction otherwise)
- [Optionally] Postfixed by a salient non-redundant characteristic
  (i.e., advertised difficulty level if not otherwise evident from superordinate directory names)

Within each module, Google-style (ish) docstrings and doctests
are used to document and test the code, respectively.

Documentation and tests are designed to serve the learning process,
not the other way around, so there is not an enforced standard.
However, in general:
- Self-evident fields are excluded
  - Ex. "arr: the array to sort"
- Non-standard fields are included ad-hoc to communicate salient information
  - E.g., time/space complexity, diagrams, etc.
- Attributions, links, and qualified file paths are included whenever possible

------------

Table of Contents

<!-- toc -->

- [Usage](#usage)
- [Development](#development)
  * [Package and Dependencies Installation](#package-and-dependencies-installation)
  * [Testing](#testing)
  * [Code Quality](#code-quality)
    + [Automate via Git Pre-Commit Hooks](#automate-via-git-pre-commit-hooks)
- [Further Reading](#further-reading)
- [Legal](#legal)
  * [License](#license)
  * [Credits](#credits)

<!-- tocstop -->

Usage
=====
The workflow I've found that has worked best for me:

1. Create a file adhering to project structure rules.
2. Define the necessary **type-annotated** module functions, classes, etc. stubs for the given problem.
3. Generate docstring stubs and add problem-specific information into corresponding fields.
    - i.e., `Args` for problem-specific parameters, `Returns` for the return value.
4. Iteratively implement the solution, alternating between adding/updating
   doctests in the `Examples` section and writing code, ala
   [TDD](https://en.wikipedia.org/wiki/Test-driven_development#:~:text=Test%2Ddriven%20development%20(TDD),software%20against%20all%20test%20cases.).
    - Development cycles can be made extremely fast when running in an IDE with built-in doctest support,
      e.g., using Pycharm and hitting the "Run Doctests" keyboard shortcut on significant changes.

> 📝 **Note**  
>  As much as possible, try not to import anything from any other project modules.
>  - This way, we maintain maximum flexibility regarding problem-specific implementations
>    by removing the opportunity to mistake
>    [incidental duplication](https://news.ycombinator.com/item?id=22022603)
>    for true systemic duplication (see:
>    [The software engineering rule of 3](https://erikbern.com/2017/08/29/the-software-engineering-rule-of-3.html)).
>  - As an added bonus, it also prevents the code from becoming abstruse due to excessive indirection.

Development
===========

> 📝 **Note**  
>  For convenience, many of the below processes are abstracted away
>  and encapsulated in single [Make](https://www.gnu.org/software/make/) targets.


> 🔥 **Tip**  
>  Invoking `make` without any arguments will display
>  auto-generated documentation on available commands.

Package and Dependencies Installation
--------------------------------------

Make sure you have Python 3.9+ and [`poetry`](https://python-poetry.org/)
installed and configured.

To install the package and all dev dependencies, run:
```shell script
make provision_environment
```

> 🔥 **Tip**  
>  Invoking the above without `poetry` installed will emit a
>  helpful error message letting you know how you can install poetry.

Testing
------------

We use [`tox`](https://tox.readthedocs.io/en/latest/) for our test automation framework
and [`pytest`](https://pytest.readthedocs.io/) for our testing framework.

To invoke the tests, run:

```shell script
make test
```

Code Quality
------------

We are using [`pre-commit`](https://pre-commit.com/) for our code quality
static analysis automation and management framework.

To invoke the analyses and auto-formatting over all version-controlled files, run:

```shell script
make lint
```

> 🚨 **Danger**  
>  CI will fail if either testing or code quality fail,
>  so it is recommended to automatically run the above locally
>  prior to every commit that is pushed.

### Automate via Git Pre-Commit Hooks

To automatically run code quality validation on every commit (over to-be-committed
files), run:

```shell script
make install-pre-commit-hooks
```

> ⚠️ Warning  
>  This will prevent commits if any single pre-commit hook fails
>  (unless it is allowed to fail)
>  or a file is modified by an auto-formatting job;
>  in the latter case, you may simply repeat the commit and it should pass.

Further Reading
===============

- [LeetCode](https://leetcode.com/)
- [Grokking the Coding Interview: Patterns for Coding Questions](https://www.educative.io/courses/grokking-the-coding-interview)
  - [14 Patterns to Ace Any Coding Interview Question](https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed)
- [Decode the Coding Interview in Python: Real-World Examples](https://www.educative.io/courses/decode-coding-interview-python)

---

Legal
=====

License
-------

LeetCode is licensed under the Apache License, Version 2.0.
See [LICENSE](./LICENSE) for the full license text.


Credits
-------

This project was generated from
[`@TeoZosa`'s](https://github.com/TeoZosa)
[`cookiecutter-cruft-poetry-tox-pre-commit-ci-cd`](https://github.com/TeoZosa/cookiecutter-cruft-poetry-tox-pre-commit-ci-cd)
template.
