"""https://www.educative.io/courses/grokking-the-coding-interview/gx2OqlvEnWG

"""


def find_subsets(nums: list[int]) -> list[list[int]]:
    """BFS-based subsets

    Complexity:
        n = len(nums)
        P(S) (Powerset of S) = 2^n
        Since the powerset (the set of all subsets) of a set S is has
        2^n elements, we will have 2^n subsets.

            Time:
                O(n*2^n)
                n iterations, doubling the number of subsets at each iteration,
                and this doubling requires copying every element in every subset.
                Since the powerset (the set of all subsets) of a set S has 2^n elements,
                we will have 2^n subsets.

            Space:
                O(n*2^n)
                Since the powerset (the set of all subsets) of a set S has 2^n elements,
                we will have 2^n subsets.

    Args:
        nums: array of possibly non-distinct elements

    Returns:

    Examples:
        >>> find_subsets([1, 3])
        [[], [1], [3], [1, 3]]
        >>> find_subsets([1, 5, 3])
        [[], [1], [5], [1, 5], [3], [1, 3], [5, 3], [1, 5, 3]]

    """

    subsets = [[]]  # Initialized with the empty subset

    for num in nums:
        # we will take all existing subsets
        # and insert the current number in them to create new subsets
        new_subsets = [subset + [num] for subset in subsets]
        subsets += new_subsets

    return subsets
