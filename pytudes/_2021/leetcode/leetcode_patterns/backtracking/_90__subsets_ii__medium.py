"""https://leetcode.com/problems/subsets-ii/

The solution set must not contain duplicate subsets. Return the solution in any order.
Given an integer array nums that may contain duplicates,
return all possible subsets (the power set).
    - The solution set must not contain duplicate subsets.
    - Return the solution in any order.

Constraints:
    - 1 ≤ nums.length ≤ 10
    - -10 ≤ nums[i] ≤ 10

Examples:
    >>> Solution().subsetsWithDup([])
    [[]]

"""


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        return find_subsets(nums)


def find_subsets(nums: list[int]) -> list[list[int]]:
    """

    Args:
        nums: array of possibly non-distinct elements

    Returns: The proper (no duplicates) powerset of `nums`

    Examples:
        >>> find_subsets([1,2,2])
        [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
        >>> find_subsets([0])
        [[], [0]]

    """

    """ALGORITHM"""
    ## INITIALIZE VARS ##
    # sort the numbers to handle duplicates by making them adjacent
    nums.sort()

    # DS's/res
    all_subsets = new_subsets = [[]]  # Initialized with the empty subset

    for i, curr_num in enumerate(nums):
        prev_num = None if i == 0 else nums[i - 1]
        # if current and the previous elements are same,
        # the previous number ALREADY covered some of the search space
        # => do NOT create new subsets from the same set of elements
        # <=> create new subsets ONLY from the subsets CREATED IN PREVIOUS ITERATION
        valid_subsets = all_subsets if curr_num != prev_num else new_subsets
        new_subsets = [subset + [curr_num] for subset in valid_subsets]
        all_subsets += new_subsets

    return all_subsets
