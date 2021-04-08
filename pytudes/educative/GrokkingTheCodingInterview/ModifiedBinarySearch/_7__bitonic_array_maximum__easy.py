"""https://www.educative.io/courses/grokking-the-coding-interview/RMyRR6wZoYK

"""


def find_max_in_bitonic_array(arr: list[int]) -> int:
    """Binary search to find the maximum value in a bitonic array (aka *Peak Finding*)

    Bitonic: *strictly* increasing AND THEN *strictly* decreasing.
    i.e., arr[i] < arr[i+1] < ... < arr[max_element_idx] > ... > arr[j] > arr[j+1]

    Complexity:
        Time: Θ(logn) <=> O(logn) & Ω(logn)
        Space: O(1)

    Args:
        arr: bitonic array
            (i.e., a *strictly* increasing sequence preceding a central peak
            followed by *strictly* a decreasing sequence)

    Returns: the maximum value in bitonic array `arr`

    Raises: ValueError if the array is not strictly increasing/decreasing

    Examples:
        >>> find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]) # Bitonic
        12
        >>> find_max_in_bitonic_array([3, 8, 3, 1]) # Bitonic
        8
        >>> find_max_in_bitonic_array([1, 3, 8, 12]) # Strictly increasing (Bitonic w/ no decreasing range)
        12
        >>> find_max_in_bitonic_array([10, 9, 8]) # Strictly decreasing (Bitonic w/ no increasing range)
        10

    """
    ## EDGE CASES ##
    if not arr:
        raise ValueError

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
    return arr[start]
