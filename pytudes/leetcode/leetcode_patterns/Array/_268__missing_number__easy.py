"""https://leetcode.com/problems/missing-number/

Constraints:
    - n == nums.length
    - 1 ≤ n ≤ 104
    - 0 ≤ nums[i] ≤ n
    - All the numbers of nums are unique.

Examples:
    >>> Solution().missingNumber([])
    0

See Also:
    - pytudes/educative/GrokkingTheCodingInterview/BitwiseXOR/_0__find_missing_number__easy.py
    - pytudes/educative/GrokkingTheCodingInterview/CyclicSort/_1__find_the_missing_number__easy.py

"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return missing_number_cyclic_sort(nums)


def missing_number_cyclic_sort(nums: list[int]) -> int:
    """Returns the single number in the range [0,n] missing in nums

    Complexity:
        Time: O(n)
        Space: O(1)

    Args:
        nums:
            array containing n distinct numbers taken from the range [0,n]
            (n+1 possible numbers)

    Examples:
        >>> missing_number_cyclic_sort([])
        0
        >>> missing_number_cyclic_sort([0])
        1
        >>> missing_number_cyclic_sort([3,0,1])
        2
        >>> missing_number_cyclic_sort([0,1])
        2
        >>> missing_number_cyclic_sort([9,6,4,2,3,5,7,0,1])
        8

    """
    """ALGORITHM"""

    def swap_elements(i, j):
        nums[i], nums[j] = nums[j], nums[i]

    ## INITIALIZE VARS ##
    n = len(nums)

    ## CYCLIC SORT
    curr_idx = 0
    while curr_idx < n:
        target_idx = nums[curr_idx]
        if curr_idx != target_idx and target_idx < n:
            swap_elements(curr_idx, target_idx)
        else:
            curr_idx += 1

    ## FIND MISSING NUMBER
    for curr_idx, target_idx in enumerate(nums):
        if curr_idx != target_idx:
            return curr_idx
    else:
        return n  # missing number is n itself
