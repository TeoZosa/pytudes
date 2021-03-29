import copy


def mergesort(nums: list, in_place: bool = True) -> list:
    """
    Complexity:
        n = len(items)
            Time: O(nlogn)
            Space: O(n) for copies of sorted subarrays
    Examples:
        >>> mergesort([3,3,1,1,2,2], in_place=True)
        [1, 1, 2, 2, 3, 3]
        >>> mergesort([3,2,1,1,2,3], in_place=True)
        [1, 1, 2, 2, 3, 3]
        >>> mergesort([0,-4,2,-2,4]*3, in_place=True)
        [-4, -4, -4, -2, -2, -2, 0, 0, 0, 2, 2, 2, 4, 4, 4]
    """
    if not in_place:
        nums = copy.deepcopy(nums)
    _mergesort(nums, 0, len(nums) - 1)
    return nums


def _mergesort(nums: list, start: int, end: int) -> None:

    ## EDGE CASES ##
    if not nums:
        return

    """Algorithm"""
    ## BASE CASE ##
    if start >= end:
        return

    ## INITIALIZE VARS##
    mid = (start + end) // 2

    ## RECURSIVELY SORT SUBARRAYS##
    _mergesort(nums, start, mid)
    left = nums[start : mid + 1]

    _mergesort(nums, mid + 1, end)
    right = nums[mid + 1 : end + 1]

    ## MERGE SORTED SUBARRAYS ##
    curr_left_idx = curr_right_idx = 0
    insertion_idx = start
    # Merge until a single subarray is exhausted
    while curr_left_idx < len(left) and curr_right_idx < len(right):
        if left[curr_left_idx] <= right[curr_right_idx]:
            nums[insertion_idx] = left[curr_left_idx]
            curr_left_idx += 1
        else:
            nums[insertion_idx] = right[curr_right_idx]
            curr_right_idx += 1
        insertion_idx += 1

    # Merge remaining subarray
    if curr_left_idx == len(left):
        while curr_right_idx < len(right):
            nums[insertion_idx] = right[curr_right_idx]
            curr_right_idx += 1
            insertion_idx += 1
    else:
        while curr_left_idx < len(left):
            nums[insertion_idx] = left[curr_left_idx]
            curr_left_idx += 1
            insertion_idx += 1
