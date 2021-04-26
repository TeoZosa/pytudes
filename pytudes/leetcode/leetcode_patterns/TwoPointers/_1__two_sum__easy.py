"""https://leetcode.com/problems/two-sum/

Constraints:
    - 2 ≤ nums.length ≤ 103
    - -109 ≤ nums[i] ≤ 109
    - -109 ≤ target ≤ 109
    - Only one valid answer exists.

Examples:
    >>> Solution().twoSum([0, 0], target=0)
    [0, 1]

"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return two_sum(nums, target)


def two_sum(nums: list[int], target: int) -> list[int]:
    """Returns the two distinct indexes of elements in nums that together sum to the given target

    Complexity:
        n = len(nums)
        Time: O(n)
        Space: O(n) (for hashtable)

    Args:
        nums: array of numbers
        target: value for which we are finding a two sum

    Examples:
        >>> two_sum([2,7,11,15], target=9)
        [0, 1]
        >>> two_sum([3,2,4], target=6)
        [1, 2]
        >>> two_sum([3,3], target=6)
        [0, 1]
        >>> two_sum([], target=0)
        Traceback (most recent call last):
        ...
        RuntimeError: Solution assumed to exist but was not found

    """

    """ALGORITHM"""
    ## INITIALIZE VARS ##
    # DS's/res
    nums_idx = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in nums_idx:
            return [nums_idx[diff], i]
        else:
            nums_idx[num] = i

    raise RuntimeError("Solution assumed to exist but was not found")
