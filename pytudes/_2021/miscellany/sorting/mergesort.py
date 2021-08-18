def mergesort(nums: list, in_place: bool = True) -> list:
    """

    Complexity:
        n = len(nums)
            Time: O(nlogn)
            Space: O(n) for copies of sorted subarrays

    Examples:
        >>> assert(mergesort([3,3,1,1,2,2], in_place=True) == mergesort([3,3,1,1,2,2], in_place=False))
        >>> mergesort([3,3,1,1,2,2], in_place=True)
        [1, 1, 2, 2, 3, 3]
        >>> mergesort([3,2,1,1,2,3], in_place=True)
        [1, 1, 2, 2, 3, 3]
        >>> mergesort([0,-4,2,-2,4]*3, in_place=True)
        [-4, -4, -4, -2, -2, -2, 0, 0, 0, 2, 2, 2, 4, 4, 4]

    """
    if not in_place:
        return _mergesort(nums)
    else:
        _mergesort_space_optimized(nums, 0, len(nums) - 1)
        return nums


def _mergesort(nums: list) -> list:
    """

    Complexity:
        n = len(nums)
            Space: 2n = O(n)
                for (2 * n/2) copies of sorted left/right subarrays
                and (1 * n) copy of merged array

    Examples:
        >>> _mergesort([])
        []

    """
    ## EDGE CASES ##
    if not nums:
        return nums

    """Algorithm"""
    ## BASE CASE ##
    if len(nums) <= 1:
        return nums

    ## INITIALIZE VARS##
    mid = len(nums) // 2

    ## RECURSIVELY SORT SUBARRAYS ##
    left = _mergesort(nums[:mid])  # n/2 copy
    right = _mergesort(nums[mid:])  # n/2 copy
    return _merge(left, right)  # n copy


def _merge(left: list, right: list) -> list:
    ## INITIALIZE VARS ##
    curr_left_idx = curr_right_idx = 0

    # res
    merged = []
    ## Merge until a single subarray is exhausted
    while curr_left_idx < len(left) and curr_right_idx < len(right):
        if left[curr_left_idx] <= right[curr_right_idx]:
            merged.append(left[curr_left_idx])
            curr_left_idx += 1
        else:
            merged.append(right[curr_right_idx])
            curr_right_idx += 1

    ## Merge remainder of non-exhausted subarray
    if curr_left_idx == len(left):  # left exhausted <=> right not exhausted
        merged.extend(right[curr_right_idx:])
    else:  # right exhausted <=> left not exhausted
        merged.extend(left[curr_left_idx:])

    return merged


def _mergesort_space_optimized(nums: list, start: int, end: int) -> None:
    """Performing merge operation in-place by overwriting associated indexes of input array

    Complexity:
        n = len(nums)
            Space: n = O(n)
                for (2 * n/2) copies of sorted left/right subarrays

    Examples:
        >>> _mergesort_space_optimized([], 0, 0)

    """
    ## EDGE CASES ##
    if not nums:
        return

    """Algorithm"""
    ## BASE CASE ##
    if start >= end:
        return

    ## INITIALIZE VARS##
    mid = (start + end + 1) // 2

    ## RECURSIVELY SORT SUBARRAYS ##
    _mergesort_space_optimized(nums, start, mid - 1)
    left = nums[start:mid]  # n/2 copy

    _mergesort_space_optimized(nums, mid, end)
    right = nums[mid : end + 1]  # n/2 copy

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
