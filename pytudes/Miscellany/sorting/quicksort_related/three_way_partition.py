"""Vanilla Quicksort robust to repeated elements

See Also:
    pytudes/Miscellany/sorting/dutch_nation_flag_problem.py
"""

import random


def partition_3_ways_and_get_left_end_right_start_indexes(
    items: list[int], start: int, end: int
) -> tuple[int, int]:
    """In-place partition of items[start:end+1]
    Complexity:
        Time: Θ(n)
        Space: O(1)
    Returns: end index of left partition, start index of right partition
    Examples:
        >>> items = []
        >>> partition_3_ways_and_get_left_end_right_start_indexes(items, start=0, end=0)
        (-1, -1)
        >>> items = ["RANGE TOO LARGE"]
        >>> partition_3_ways_and_get_left_end_right_start_indexes(items, start=0, end=2 )
        (-1, -1)
        >>> random.seed(64)
        >>> items = [3,3,1,1,2,2]
        >>> partition_3_ways_and_get_left_end_right_start_indexes(items, start=0, end=len(items)-1 )
        (-1, 2)
        >>> items = [3,2,1,1,2,3]
        >>> partition_3_ways_and_get_left_end_right_start_indexes(items, start=0, end=len(items)-1 )
        (3, 6)
        >>> items = [0,-4,2,-2,4]*3
        >>> partition_3_ways_and_get_left_end_right_start_indexes(items, start=0, end=len(items)-1 )
        (5, 9)
    """

    if not items or len(items) < end - start + 1:
        return -1, -1
    """ALGORITHM"""

    def swap_elements(i, j):
        items[i], items[j] = items[j], items[i]

    ## INITIALIZE VARS ##
    pivot_idx = random.randint(start, end)
    pivot = items[pivot_idx]

    ## 3-WAY PARTITION ##
    # INVARIANT: mid_start < unsorted_start ≤ unsorted_end
    swap_elements(start, pivot_idx)  # move pivot to start for variable name correctness
    mid_start, unsorted_start, unsorted_end = start, start + 1, end
    while unsorted_start <= unsorted_end:
        if items[unsorted_start] < pivot:  # left partition move
            swap_elements(unsorted_start, mid_start)
            mid_start += 1
            unsorted_start += 1
        elif items[unsorted_start] > pivot:  # right partition move
            swap_elements(unsorted_start, unsorted_end)
            unsorted_end -= 1
        else:  # already in correct location
            unsorted_start += 1
    left_end, right_start = mid_start - 1, unsorted_end + 1
    return left_end, right_start
