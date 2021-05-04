"""https://www.educative.io/courses/grokking-the-coding-interview/qA5wW7R8ox7

Given an array of numbers sorted in an ascending order,
find the CEILING of a given number ‘val’.
    The CEILING of val will be the
    smallest element in the given array *greater than OR equal* to val.

"""


def search_ceiling_of_a_number(arr: list[int], val: int) -> int:
    """Binary search to find the ceiling of a given number.

    The ceiling of a number is defined to be
    the smallest element *greater than OR equal* to val.

    Complexity:
        Time: O(logn) & Ω(1)
        Space: O(1)

    Args:
        arr: array of numbers sorted in ascending order
        val: element in arr for which to find the ceiling if the ceiling is in arr, else -1

    Returns: index of the ceiling of val being searched if ceiling is in items, else -1

    Examples:
        >>> search_ceiling_of_a_number([4, 6, 10], 6)
        1
        >>> search_ceiling_of_a_number([1, 3, 8, 10, 15], 12)
        4
        >>> search_ceiling_of_a_number([4, 6, 10], -1)
        0
        >>> search_ceiling_of_a_number([], 1)
        -1
        >>> search_ceiling_of_a_number([4, 6, 10], 17)
        -1

    """
    ## EDGE CASES ##
    if not arr:
        return -1
    if val > arr[-1]:  # no ceiling <=> 'val' is bigger than the biggest element
        return -1

    """ALGORITHM"""
    ## INITIALIZE VARS ##
    start, end = 0, len(arr) - 1

    ## BINARY SEARCH ##
    while start <= end:
        mid = (start + end) // 2
        if val < arr[mid]:
            end = mid - 1
        elif val > arr[mid]:
            start = mid + 1
        else:  # equal case
            return mid
    else:  # greater than case
        # arr[start] is the immediate successor to val
        #   See Also: pytudes/miscellany/searching/binary_search.py:19
        # Note: start < len(arr)
        #   since we only execute binary search if the ceiling exists
        return start
