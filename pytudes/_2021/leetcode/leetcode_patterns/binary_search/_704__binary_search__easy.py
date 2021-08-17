"""https://leetcode.com/problems/binary-search/

Constraints:
    - 1 ≤ nums.length ≤ 104
    - -9999 ≤ nums[i], target ≤ 9999
    - All the integers in nums are unique.
    - nums is sorted in an ascending order.

Examples:
    >>> Solution().search([], target=0)
    -1

"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return get_idx_via_binary_search(nums, target)


def get_idx_via_binary_search(nums: list[int], target: int) -> int:
    """Returns the index of target if it exists, otherwise -1

    Complexity:
        n = len(nums)
        Time: O(logn)
        Space: O(1)

    Args:
        nums: array of integers sorted in ascending order
        target: element for which to search in `nums`

    Examples:
        >>> get_idx_via_binary_search([-1,0,3,5,9,12],target=9)
        4
        >>> get_idx_via_binary_search([-1,0,3,5,9,12],target=2)
        -1

    """
    """ALGORITHM"""
    start_idx, end_idx = 0, len(nums) - 1
    while start_idx <= end_idx:
        # Prevents "overflow" in other languages
        mid_idx = start_idx + (end_idx - start_idx) // 2
        if nums[mid_idx] < target:  # SEARCH RIGHT
            start_idx = mid_idx + 1
        elif nums[mid_idx] > target:  # SEARCH LEFT
            end_idx = mid_idx - 1
        else:  # FOUND `target`
            return mid_idx
    else:
        return -1
