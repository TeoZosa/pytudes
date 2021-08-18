"""https://leetcode.com/problems/single-number/

Constraints:
    - 1 ≤ nums.length ≤ 3 * 104
    - -3 * 104 ≤ nums[i] ≤ 3 * 104
    - Each element in the array appears twice except for one element which appears only once.

Examples:
    >>> Solution().singleNumber([])
    0

"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return single_number(nums)


def single_number(nums: list[int]) -> int:
    """Returns the only element in `nums` that appears exactly once

    Better Space than hashtable (O(n/2) = O(n))
        - in the worst case everything appears once before encountering duplicates
        (since we could always delete entries from the hashtable once we encounter exactly 2)

    Complexity:
        n = len(nums)
        Time: O(n)
        Space: O(1)

    Args:
        nums: array of integers s.t. every element appears twice, except for one

    Returns: the only element in `nums` that appears exactly once

    Examples:
        >>> single_number([2,2,1])
        1
        >>> single_number([4,1,2,1,2])
        4
        >>> single_number([1])
        1

    """

    """ALGORITHM"""
    ## INITIALIZE VARS ##
    single_num = 0
    for num in nums:
        single_num ^= num

    return single_num


def single_number_hashtable(nums: list[int]) -> int:
    """Returns the only element in `nums` that appears exactly once

    Complexity:
        n = len(nums)
        Time: O(n)
        Space: O(n)

    Args:
        nums: array of integers s.t. every element appears twice, except for one

    Returns: the only element in `nums` that appears exactly once

    Examples:
        >>> single_number_hashtable([2,2,1])
        1
        >>> single_number_hashtable([4,1,2,1,2])
        4
        >>> single_number_hashtable([1])
        1
        >>> single_number_hashtable([1,1])
        Traceback (most recent call last):
        ...
        ValueError: No element in `nums` appears exactly once.

    """

    """ALGORITHM"""
    ## INITIALIZE VARS ##
    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1

    for num, count in num_counts.items():
        if count == 1:
            return num
    else:
        raise ValueError("No element in `nums` appears exactly once.")
