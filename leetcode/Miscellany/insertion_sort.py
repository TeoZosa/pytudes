"""
NOTE:
- Contiguous slice update is O(k) where k = size of the slice
    => same big O as single-item swaps.
- Trivial overhead but improved readability for
    `reversed(range))` vs. `range(end, start-1, -1)`

"""
import random


def binary_insertion_sort(items: list) -> list:
    """

    Args:
        items:
    Complexity:
        Time: O(n^2)
        Space: O(1)

        NOTE: since shifting dominates the runtime,
        allowing binary search subroutine to be Θ(logn)
        by not breaking early if `items[mid_idx] == insertion_val`.

        This minimizes shift operations by ensuring
        `items[mid_idx]` is the smallest element *strictly* greater
        than `insertion_val` (i.e., the IMMEDIATE SUCCESSOR)

        See Also:
            leetcode/educative/ModifiedBinarySearch/3__next_letter__medium.py


    Returns:
    Examples:
        >>> binary_insertion_sort([5,4,3,2,1,0])
        [0, 1, 2, 3, 4, 5]
        >>> binary_insertion_sort([0,1,2,3,4,5])
        [0, 1, 2, 3, 4, 5]
        >>> binary_insertion_sort([5,4,3,2,1,0]*2)
        [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        >>> items = [random.randrange(0, 100) for _ in range(100)]
        >>> assert(binary_insertion_sort(items.copy()) == sorted(items))
    """

    for unsorted_start_idx in range(1, len(items)):
        ## Minor optimization to ensure Ω(n) (i.e., already sorted arrays)
        sorted_end_idx = unsorted_start_idx - 1
        insertion_val = items[unsorted_start_idx]
        if items[sorted_end_idx] <= insertion_val:  # Already in sorted order
            continue

        ## BINARY SEARCH for insertion idx ##
        left, right = 0, sorted_end_idx
        while left <= right:
            mid_idx = (left + right) // 2
            if insertion_val < items[mid_idx]:  # Search LEFT
                right = mid_idx - 1
            else:  # insertion_val >= items[mid_idx]
                left = mid_idx + 1
        insertion_idx = left
        # items[left] is now IMMEDIATE SUCCESSOR of insertion_val
        #   See Also: leetcode/Miscellany/searching/binary_search.py:19

        ## BISECT LEFT ##
        # Shift right items in the range [insertion_idx, len(items))
        # and insert `insertion_val` at `insertion_idx`
        for src_idx in reversed(range(insertion_idx, unsorted_start_idx)):
            items[src_idx + 1] = items[src_idx]
        items[insertion_idx] = insertion_val

    return items


def insertion_sort(items: list) -> list:
    """
    Examples:
        >>> items = [random.randrange(0, 100) for _ in range(100)]
        >>> assert(insertion_sort(items.copy()) == sorted(items))
    """

    for unsorted_start_idx in range(1, len(items)):
        insertion_val = items[unsorted_start_idx]

        ## LINEAR SEARCH for insertion idx ##
        insertion_idx = unsorted_start_idx
        while insertion_idx > 0 and items[insertion_idx - 1] > insertion_val:
            insertion_idx -= 1

        ## BISECT LEFT ##
        # Shift elements greater than `insertion_val` one position to the right
        for src_idx in reversed(range(insertion_idx, unsorted_start_idx)):
            items[src_idx + 1] = items[src_idx]
        items[insertion_idx] = insertion_val
    return items


def insertion_sort_loops_combined(items: list) -> list:
    """

    Args:
        items:

    Returns:
    Examples:
        >>> items = [random.randrange(0, 100) for _ in range(100)]
        >>> assert(insertion_sort_loops_combined(items.copy()) == sorted(items))
    """

    for unsorted_start_idx in range(1, len(items)):
        insertion_val = items[unsorted_start_idx]

        # Shift elements greater than `insertion_val` one position to the right
        insertion_idx = unsorted_start_idx
        while insertion_idx > 0 and items[insertion_idx - 1] > insertion_val:
            items[insertion_idx] = items[insertion_idx - 1]
            insertion_idx -= 1
        items[insertion_idx] = insertion_val

    return items
