"""https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Constraints:
    - 2 ≤ nums.length ≤ 10^3
    - -10^9 ≤ nums[i] ≤ 10^9
    - -10^9 ≤ target ≤ 10^9
    - Only one valid answer exists.

Examples:
    >>> Solution().twoSum([0, 0], target=0)
    [1, 2]

"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return two_sum_two_pointers_special_cases(nums, target)


def two_sum_hashtable(nums: list[int], target: int) -> list[int]:
    """Determines the two indexes of the elements that together sum to the given `target`

    Complexity:
        n = len(nums)
        Time: O(n)
        Space: O(n) (for hashtable)

    Args:
        nums: sorted array of numbers
        target: value for which we are finding a two sum

    Returns:
        distinct *1-indexed* indices of two numbers that add up to `target`
        where 1 ≤ answer[0] < answer[1] ≤ numbers.length.

    Examples:
        >>> two_sum_hashtable([2,7,11,15], target=9)
        [1, 2]
        >>> two_sum_hashtable([3,2,4], target=6)
        [2, 3]
        >>> two_sum_hashtable([3,3], target=6)
        [1, 2]
        >>> two_sum_hashtable([], target=0)
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
            return [nums_idx[diff] + 1, i + 1]
        else:
            nums_idx[num] = i

    raise RuntimeError("Solution assumed to exist but was not found")


def two_sum_two_pointers(nums: list[int], target: int) -> list[int]:
    """Determines the two indexes of the elements that together sum to the given `target`

    Complexity:
        n = len(nums)
        Time: O(n)
        Space: O(1)

    Args:
        nums: sorted array of numbers
        target: value for which we are finding a two sum

    Returns:
        distinct *1-indexed* indices of two numbers that add up to `target`
        where 1 ≤ answer[0] < answer[1] ≤ numbers.length.

    Examples:
        >>> two_sum_two_pointers([2,7,11,15], target=9)
        [1, 2]
        >>> two_sum_two_pointers([1,1,1,2,7,11,15,15,15,15], target=9)
        [4, 5]
        >>> two_sum_two_pointers([2,3,4], target=6)
        [1, 3]
        >>> two_sum_two_pointers([-1,0], target=-1)
        [1, 2]
        >>> two_sum_two_pointers([], target=0)
        Traceback (most recent call last):
        ...
        RuntimeError: Solution assumed to exist but was not found

    """

    """ALGORITHM"""
    l_idx, r_idx = 0, len(nums) - 1
    while l_idx < r_idx:
        l_r_sum = nums[l_idx] + nums[r_idx]
        if l_r_sum > target:
            r_idx -= 1
        elif l_r_sum < target:
            l_idx += 1
        else:
            return [l_idx + 1, r_idx + 1]

    raise RuntimeError("Solution assumed to exist but was not found")


def two_sum_two_pointers_special_cases(nums: list[int], target: int) -> list[int]:
    """Determines the two indexes of the elements that together sum to the given `target`

    Complexity:
        n = len(nums)
        Time: O(n) (better constants if `nums` has a large number of duplicate values, otherwise worse constants)
        Space: O(1)

    Optimizes for special cases related to duplicate values (enabled by the sorted pre-condition):
    if duplicate values exist and:
        - Two sum up to `target`:
            search terminates early since those elements must be adjacent
        - Do NOT contribute to a solution:
            uses binary search to skip past duplicate elements in the input array

    Args:
        nums: sorted array of numbers
        target: value for which we are finding a two sum

    Returns:
        distinct *1-indexed* indices of two numbers that add up to `target`
        where 1 ≤ answer[0] < answer[1] ≤ numbers.length.

    Examples:
        >>> two_sum_two_pointers_special_cases([2,7,11,15], target=9)
        [1, 2]
        >>> two_sum_two_pointers_special_cases([1,1,1,2,7,11,15,15,15,15], target=9)
        [4, 5]
        >>> two_sum_two_pointers_special_cases([1,1,1,2,7,11,15,15,15,15], target=2)
        [1, 2]
        >>> two_sum_two_pointers_special_cases([1,1,1,2,7,11,15,15,15,15], target=30)
        [9, 10]
        >>> two_sum_two_pointers_special_cases([2,3,4], target=6)
        [1, 3]
        >>> two_sum_two_pointers_special_cases([-1,0], target=-1)
        [1, 2]
        >>> two_sum_two_pointers_special_cases([], target=0)
        Traceback (most recent call last):
        ...
        RuntimeError: Solution assumed to exist but was not found

    """
    """ALGORITHM"""
    l_idx, r_idx = 0, len(nums) - 1
    while l_idx < r_idx:

        ## Special case #1: Return adjacent duplicate complements in constant time
        l_idx_next = l_idx + 1
        l_is_a_duplicate = l_idx_next < r_idx and nums[l_idx] == nums[l_idx_next]
        if l_is_a_duplicate and nums[l_idx] + nums[l_idx_next] == target:
            return [l_idx + 1, l_idx_next + 1]

        r_idx_next = r_idx - 1
        r_is_a_duplicate = r_idx_next > l_idx and nums[r_idx] == nums[r_idx_next]
        if r_is_a_duplicate and nums[r_idx] + nums[r_idx_next] == target:
            return [r_idx_next + 1, r_idx + 1]

        ## TWO POINTERS
        ## Special case # 2: Binary search past duplicates
        l_r_sum = nums[l_idx] + nums[r_idx]
        if l_r_sum > target:
            r_idx = (
                r_idx_next
                if not r_is_a_duplicate
                # Binary search past duplicates to find predecessor element
                else bisect_left(nums, nums[r_idx], l_idx, r_idx)
            )
        elif l_r_sum < target:
            l_idx = (
                l_idx_next
                if not l_is_a_duplicate
                # Binary search past duplicates to find successor element
                else bisect_right(nums, nums[l_idx], l_idx, r_idx)
            )
        else:
            return [l_idx + 1, r_idx + 1]

    raise RuntimeError("Solution assumed to exist but was not found")


def bisect_right(nums, val, start_idx, end_idx):
    while start_idx <= end_idx:
        mid_idx = start_idx + (end_idx - start_idx) // 2
        if nums[mid_idx] <= val:
            start_idx = mid_idx + 1
        elif nums[mid_idx] > val:  # pragma: no branch
            end_idx = mid_idx - 1
    return start_idx


def bisect_left(nums, val, start_idx, end_idx):
    while start_idx <= end_idx:
        mid_idx = start_idx + (end_idx - start_idx) // 2
        if nums[mid_idx] < val:
            start_idx = mid_idx + 1
        elif nums[mid_idx] >= val:  # pragma: no branch
            end_idx = mid_idx - 1
    return end_idx
