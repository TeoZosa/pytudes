"""https://leetcode.com/problems/contains-duplicate/

Categories:
    - Array
    - Blind 75

Examples:
    >>> Solution().containsDuplicate([1,2,3])
    False

"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return contains_duplicate(nums)


def contains_duplicate(nums: list[int]) -> bool:
    """

    Args:
        nums: array of possibly non-distinct integers

    Returns: True if `nums` contains duplicate elements, False otherwise

    Examples:
        >>> contains_duplicate([1,2,3,1])
        True
        >>> contains_duplicate([1,2,3,4])
        False
        >>> contains_duplicate([1,1,1,3,3,4,3,2,4,2])
        True

    """
    hash_table = {}
    for num in nums:
        if hash_table.get(num) is None:
            hash_table[num] = True
        else:
            return True
    else:
        return False
