"""https://leetcode.com/problems/squares-of-a-sorted-array/

Constraints:
    - 1 ≤ nums.length ≤ 104
    - -104 ≤ nums[i] ≤ 104
    - nums is sorted in non-decreasing order.

Examples:
    >>> Solution().sortedSquares([])
    []

"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted_squares(nums)


def sorted_squares(nums: list[int]) -> list[int]:
    """Returns a (non-decreasing) sorted array of the squares of each element in nums

    Complexity:
        n = len(nums)
        Time: O(n)
        Space: O(n) (for the new sorted array)

    Args:
        nums: a sorted array of numbers drawn from the range [-∞,+∞]

    Examples:
        >>> sorted_squares([])
        []
        >>> sorted_squares([-4,-1,0,3,10])
        [0, 1, 9, 16, 100]
        >>> sorted_squares([-7,-3,2,3,11])
        [4, 9, 9, 49, 121]

    """
    """ALGORITHM"""
    ## INITIALIZE VARS ##
    # DS's/res
    sorted_nums_squared = [None] * len(nums)
    insertion_idx = len(sorted_nums_squared) - 1  # insert back to front

    ## TWO POINTERS
    l_idx, r_idx = 0, len(nums) - 1
    while l_idx <= r_idx:
        left_num_squared, right_num_squared = nums[l_idx] ** 2, nums[r_idx] ** 2
        # Add larger element to array
        if left_num_squared < right_num_squared:
            sorted_nums_squared[insertion_idx] = right_num_squared
            r_idx -= 1
        else:
            sorted_nums_squared[insertion_idx] = left_num_squared
            l_idx += 1
        insertion_idx -= 1

    return sorted_nums_squared


def sorted_squares_brute_force(nums: list[int]) -> list[int]:
    """Returns a (non-decreasing) sorted array of the squares of each element in nums

    Naively squares each element and sorts the array

    Complexity:
        n = len(nums)
        Time: O(nlogn)
        Space: O(n) (for the sorted array)
            Note: even if "in-place", still O(n) for the timsort auxillary space.

    Args:
        nums: a sorted array of numbers drawn from the range [-∞,+∞]

    Examples:
        >>> sorted_squares_brute_force([])
        []
        >>> sorted_squares_brute_force([-4,-1,0,3,10])
        [0, 1, 9, 16, 100]
        >>> sorted_squares_brute_force([-7,-3,2,3,11])
        [4, 9, 9, 49, 121]

    """
    for i in range(len(nums)):
        nums[i] *= nums[i]
    return sorted(nums)
