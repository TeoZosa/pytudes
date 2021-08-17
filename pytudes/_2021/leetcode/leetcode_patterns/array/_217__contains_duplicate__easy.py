"""https://leetcode.com/problems/contains-duplicate/

Constraints:
    - 1 ≤ nums.length ≤ 105
    - -109 ≤ nums[i] ≤ 109

Examples:
    >>> Solution().containsDuplicate([])
    False

"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return contains_duplicate(nums)


def contains_duplicate(nums: list[int]) -> bool:
    """Returns True if any value appears at least twice in the array, otherwise False

    Complexity:
        n = len(nums)
        Time: O(n)
        Space: O(n)

    Args:
        nums: array of possibly non-distinct values

    Examples:
        >>> contains_duplicate([1,2,3,1])
        True
        >>> contains_duplicate([1,2,3,4])
        False
        >>> contains_duplicate([1,1,1,3,3,4,3,2,4,2])
        True

    """

    """ALGORITHM"""
    ## INITIALIZE VARS ##
    # DS's/res
    nums_set = set()

    for num in nums:
        if num not in nums_set:
            nums_set.add(num)
        else:
            return True
    else:
        return False
