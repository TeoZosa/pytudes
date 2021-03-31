"""https://www.educative.io/courses/grokking-the-coding-interview/R1B78K9oBEz

"""


def find_range(arr: list[int], val: int) -> list[int]:
    """Binary search to find the range of a given number ‘val’.

        The range of val will be the first and last position of val in the arr.
    Args:
        arr: array of numbers sorted in ascending order
        val: element in arr for which to find the inclusive range
    Complexity:
        Time: Θ(logn) <=> O(logn) & Ω(logn) (since we must consider duplicates)
        Space: O(1)
    Returns: the inclusive range of val idxs if val is present, else [-1, -1]
    Examples:
        >>> find_range([4, 6, 6, 6, 9], 6)
        [1, 3]
        >>> find_range([1, 3, 8, 10, 15], 10)
        [3, 3]
        >>> find_range([1, 3, 8, 10, 15], 12)
        [-1, -1]
    """

    def binary_search(find_last_pos: bool) -> int:
        """ALGORITHM"""
        check_left = lambda: val < arr[mid] or val == arr[mid] and not find_last_pos
        check_right = lambda: val > arr[mid] or val == arr[mid] and find_last_pos
        ## INITIALIZE VARS ##
        val_idx = -1
        start, end = 0, len(arr) - 1

        ## BINARY SEARCH ##
        while start <= end:
            mid = (start + end) // 2
            # Found a val idx
            if val == arr[mid]:
                val_idx = mid

            if check_left():
                end = mid - 1
            elif check_right():
                start = mid + 1

        # first or last pos of val_idx if val exists, -1 otherwise
        return val_idx

    ## EDGE CASES ##
    if not arr:  # Redundant given binary search conditions
        return [-1, -1]

    """ALGORITHM"""

    first_pos = binary_search(find_last_pos=False)
    # Minor optimization for better constants (logn vs. 2logn);
    #   if 'val' not present in `arr`, skip `last_pos` search
    last_pos = -1 if first_pos == -1 else binary_search(find_last_pos=True)
    return [first_pos, last_pos]


# modified Binary Search
def binary_search_orig(arr: list[int], val: int, find_max_index: bool) -> int:
    ## INITIALIZE VARS ##
    keyIndex = -1
    start, end = 0, len(arr) - 1

    ## BINARY SEARCH ##
    while start <= end:
        mid = (start + end) // 2
        if val < arr[mid]:
            end = mid - 1
        elif val > arr[mid]:
            start = mid + 1
        else:  # key == arr[mid]
            keyIndex = mid
            if find_max_index:
                start = mid + 1  # search ahead to find the last index of 'key'
            else:
                end = mid - 1  # search behind to find the first index of 'key'

    return keyIndex
