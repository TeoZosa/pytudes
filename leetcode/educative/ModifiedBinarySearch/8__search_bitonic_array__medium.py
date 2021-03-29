"""https://www.educative.io/courses/grokking-the-coding-interview/RMyRR6wZoYK

"""


def search_bitonic_array(arr: list[int], val: int) -> int:
    """Binary search to find a given value in a bitonic array

    Bitonic: *strictly* increasing AND THEN *strictly* decreasing.
    i.e., arr[i] < arr[i+1] < ... < arr[max_element_idx] > ... > arr[j] > arr[j+1]

    Args:
        arr: bitonic array
            (i.e., a *strictly* increasing sequence preceding a central peak
            followed by *strictly* a decreasing sequence)
    Complexity:
        Time: Θ(logn) <=> O(logn) & Ω(logn) (for find max)
        Space: O(1)
    Returns: an index of `val` in bitonic array `arr` if val is in `arr`, else -1
        Note: index not guaranteed to be distinct
    Raises: ValueError if the array is not strictly increasing/decreasing
    Examples:
        >>> search_bitonic_array([1, 3, 8, 4, 3], 4) # Bitonic
        3
        >>> search_bitonic_array([3, 8, 3, 1], 8) # Bitonic
        1
        >>> search_bitonic_array([1, 3, 8, 12], 12) # Strictly increasing (Bitonic w/ no decreasing range)
        3
        >>> search_bitonic_array([10, 9, 8], 10) # Strictly decreasing (Bitonic w/ no increasing range)
        0
    """
    ## EDGE CASES ##
    if not arr:
        raise ValueError

    """ALGORITHM"""
    max_index = find_max_idx_in_bitonic_array(arr)  ## Find idx of CENTRAL PEAK

    ## SEARCH LEFT of peak
    if (left_idx := binary_search_order_agnostic(arr, val, 0, max_index)) != -1:
        return left_idx
    else:  ## SEARCH RIGHT of peak
        return binary_search_order_agnostic(arr, val, max_index + 1, len(arr) - 1)


def find_max_idx_in_bitonic_array(arr: list[int]) -> int:
    """leetcode/educative/ModifiedBinarySearch/_7__bitonic_array_maximum__easy.py

    Returns: index of max value in arr
    """
    start, end = 0, len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > arr[mid + 1]:  # DECREASING <=> LEFT (including mid)
            end = mid
        elif arr[mid] < arr[mid + 1]:  # INCREASING <=> RIGHT
            start = mid + 1
        else:
            raise ValueError("Input NOT Bitonic: duplicates detected")
    # arr[start] is peak
    #   since start is only updated if new start is greater than mid
    return start


def binary_search_order_agnostic(arr: list[int], val: int, start: int, end: int) -> int:
    """leetcode/educative/ModifiedBinarySearch/1__order_agnostic_binary_search__easy.py

    Args:
        arr: array of numbers sorted in ascending or descending order
        val: element in arr for which to search
    Returns: index of val being searched if val is in arr, else -1
    """
    is_ascending = arr[start] <= arr[end]
    check_left = lambda: val < arr[mid] if is_ascending else val > arr[mid]
    check_right = lambda: val > arr[mid] if is_ascending else val < arr[mid]

    while start <= end:
        mid = (start + end) // 2
        if check_left():
            end = mid - 1
        elif check_right():
            start = mid + 1
        else:
            return mid
    else:
        return -1  # element not found
