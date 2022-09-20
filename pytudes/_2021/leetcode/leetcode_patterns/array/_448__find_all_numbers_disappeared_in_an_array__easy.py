"""https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Constraints:
    - n == nums.length
    - 1 ≤ n ≤ 105
    - 1 ≤ nums[i] ≤ n

Examples:
    >>> Solution().findDisappearedNumbers([])
    []

"""


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        return find_disappeared_numbers(nums)


def find_disappeared_numbers(nums: list[int]) -> list[int]:
    """Returns the integers in the range [1, n] that do not appear in nums.

    Best space complexity, but runtime constants worse

    Complexity:
        n = len(nums)
        Time: O(n)
        Space: O(1)

    Args:
        nums:
            array of n integers where `nums[i]` is in the range [1, n]
            Note: if any number is missing,
            that implies some other number is duplicated

    Examples:
        >>> find_disappeared_numbers([4,3,2,7,8,2,3,1])
        [5, 6]
        >>> find_disappeared_numbers([1,1])
        [2]

    """
    """ALGORITHM"""

    def swap_elements(i, j):
        nums[i], nums[j] = nums[j], nums[i]

    ## INITIALIZE VARS ##
    n = len(nums)

    ## CYCLIC SORT
    curr_idx = 0
    while curr_idx < n:
        target_idx = nums[curr_idx] - 1  # make 0-indexed
        # note: target_idx always < n since max(nums) ≤ n
        # so we can remove bounds checks typically needed in cyclic sort subroutines

        # Since the numbers may be duplicates,
        # prevent cycles by skipping swaps with elements that are
        # already in the correct location:
        # 1. swaps with self (i.e., current element already in the correct location)
        # 2. swaps with duplicate elements (future element already in correct location)
        if target_idx not in (curr_idx, nums[target_idx] - 1):
            swap_elements(curr_idx, target_idx)
        else:
            curr_idx += 1

    ## FIND DISAPPEARED NUMBERS
    disappeared_numbers = []
    for expected_num, actual_num in enumerate(nums, start=1):
        if expected_num != actual_num:
            disappeared_numbers.append(expected_num)
    return disappeared_numbers


def find_disappeared_numbers_set(nums: list[int]) -> list[int]:
    """Returns the integers in the range [1, n] that do not appear in nums.

    Better constants on time than cyclic sort version, but needs extra space

    Complexity:
        n = len(nums)
        Time: O(n)
        Space: O(n)

    Args:
        nums:
            array of n integers where `nums[i]` is in the range [1, n]
            Note: if any number is missing,
            that implies some other number is duplicated

    Examples:
        >>> find_disappeared_numbers_set([4,3,2,7,8,2,3,1])
        [5, 6]
        >>> find_disappeared_numbers_set([1,1])
        [2]

    """
    """ALGORITHM"""
    ## INITIALIZE VARS ##
    n = len(nums)
    distinct_nums = set(nums)
    return [num for num in range(1, n + 1) if num not in distinct_nums]


def find_disappeared_numbers_hashtable(nums: list[int]) -> list[int]:
    """Returns the integers in the range [1, n] that do not appear in nums.

    Worse than set and adds unnecessary complexity

    Complexity:
        n = len(nums)
        Time: O(n)
        Space: O(n)

    Args:
        nums:
            array of n integers where `nums[i]` is in the range [1, n]
            Note: if any number is missing,
            that implies some other number is duplicated

    Examples:
        >>> find_disappeared_numbers_hashtable([4,3,2,7,8,2,3,1])
        [5, 6]
        >>> find_disappeared_numbers_hashtable([1,1])
        [2]

    """
    """ALGORITHM"""
    ## INITIALIZE VARS ##
    n = len(nums)
    # DS's/res
    counts = {num: 0 for num in range(1, n + 1)}

    for num in nums:
        counts[num] += 1
    return [num for num, count in counts.items() if count == 0]
