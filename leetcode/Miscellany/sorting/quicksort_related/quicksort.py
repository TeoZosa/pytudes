"""Vanilla Quicksort robust to repeated elements

See Also:
    leetcode/Miscellany/sorting/dutch_nation_flag_problem.py
"""

import copy
import random


def quicksort(items: list[int], in_place: bool = True) -> list[int]:
    """
    Complexity:
        n = len(items)
            Time: O(nlogn) *on average* | O(n^2) worst-case
            Space: O(logn) stack space pointers to keep track of the subarrays
                *MUST* sort smaller side first,
                tail-recurse into the larger side
                (i.e., tail-call optimization/elimination)
                See Also: https://en.wikipedia.org/wiki/Quicksort#Space_complexity
    Examples:
        >>> quicksort([3,3,1,1,2,2], in_place=True)
        [1, 1, 2, 2, 3, 3]
        >>> quicksort([3,2,1,1,2,3], in_place=True)
        [1, 1, 2, 2, 3, 3]
        >>> quicksort([0,-4,2,-2,4]*3, in_place=True)
        [-4, -4, -4, -2, -2, -2, 0, 0, 0, 2, 2, 2, 4, 4, 4]
    """
    if not in_place:
        items = copy.deepcopy(items)
    _quicksort(items, start=0, end=len(items) - 1)
    return items


def _quicksort(items: list[int], start: int, end: int) -> None:
    """In-place Quicksort of items[start:end+1]"""

    def swap_elements(i, j):
        items[i], items[j] = items[j], items[i]

    ## BASE CASE ##
    if start >= end:
        return

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

    ## DIVIDE & CONQUER ##
    left_partition_size = left_end - start + 1
    right_partition_size = end - right_start + 1
    if left_partition_size < right_partition_size:
        _quicksort(items, start, left_end)
        _quicksort(items, right_start, end)
    else:
        _quicksort(items, right_start, end)
        _quicksort(items, start, left_end)
