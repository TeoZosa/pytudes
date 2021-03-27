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
            elif insertion_val > items[mid_idx]:  # Search RIGHT
                left = mid_idx + 1
            else:  # idx of duplicate val
                insertion_idx = mid_idx
                break
        else:  # left > right => insertion_val < items[left]
            insertion_idx = left
        ## PROOF:
        # Pointers crossed <=> prev iteration: left == right <=> left == right == mid =>
        #   - insertion_val < items[mid_idx]
        #       => this iteration: left unchanged
        #       => insertion_val < items[left]
        #   - insertion_val > items[mid_idx]
        #       => this iteration: left = mid_idx + 1
        #       => insertion_val < items[left]
        #       (given the way binary search works and that we've finished searching the list)

        ## BISECT LEFT ##
        # Shift elements greater than `insertion_val` one position to the right
        # before inserting `insertion_val` into list
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
