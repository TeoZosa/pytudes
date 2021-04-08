"""https://www.educative.io/courses/grokking-the-coding-interview/mymvP915LY9

"""


def search_min_diff_element(arr: list[int], val: int) -> int:
    """Binary search to find number that has min difference with ‘val’

    Complexity:
        Time: Θ(logn) <=> O(logn) & Ω(logn)
        Space: O(1)

    Args:
        arr: array of numbers sorted in ascending order
        val: element in arr for which to find companion element with the min difference

    Returns: element in arr that has min difference with ‘val’

    Examples:
        >>> search_min_diff_element([4, 6, 10],7)
        6
        >>> search_min_diff_element([4, 6, 10],4)
        4
        >>> search_min_diff_element([1, 3, 8, 10, 15],12)
        10
        >>> search_min_diff_element([4, 6, 10],17)
        10

    """
    ## EDGE CASES ##
    if val < arr[0]:  # smallest item has min difference with ‘val’
        return arr[0]
    if val > arr[-1]:  # largest item has min difference with ‘val’
        return arr[-1]

    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if val < arr[mid]:
            end = mid - 1
        elif val > arr[mid]:
            start = mid + 1
        else:
            return arr[mid]  # diff == 0 min_diff found
    else:
        # arr[start] & arr[end] are immediate successor & predecessor, respectively, of `val`
        #   See Also: pytudes/Miscellany/searching/binary_search.py:18

        # Since edge cases take care of bounds checks, find the min diff of arr[start], arr[end].
        compute_diff = lambda other_val: abs(val - other_val)
        return min(arr[start], arr[end], key=compute_diff)
