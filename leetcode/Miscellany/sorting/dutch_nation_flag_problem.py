"""Three-way partitioning function.
   e.g., for Quicksort variants to be robust to repeated elements

See Also:
    https://en.wikipedia.org/wiki/Dutch_national_flag_problem
    leetcode/Miscellany/sorting/quicksort.py
"""

import copy


def three_way_partition(items: list[int], pivot: int, in_place=True) -> list[int]:
    """
    Args:
        items:
        pivot: middle partition value; used to determine the partitions
        in_place: whether to perform partition in-place
    Complexity:
        Time: Θ(n)
        Space: O(1) (if in-place)
    Returns: items partitioned (i.e., RELATIVELY SORTED) according to mid value
    Examples:
        >>> three_way_partition([3,3,1,1,2,2], pivot=2, in_place=True)
        [1, 1, 2, 2, 3, 3]
        >>> three_way_partition([3,2,1,1,2,3], pivot=2, in_place=True)
        [1, 1, 2, 2, 3, 3]
        >>> three_way_partition([0,-4,2,-2,4]*3, pivot=0, in_place=True)
        [-4, -2, -2, -4, -4, -2, 0, 0, 0, 4, 2, 2, 4, 4, 2]
    """
    if not items:
        return items

    """ALGORITHM"""

    def swap_elements(i, j):
        items[i], items[j] = items[j], items[i]

    ## INITIALIZE VARS ##
    mid_start, unsorted_start, unsorted_end = 0, 0, len(items) - 1

    # DS's/res
    if not in_place:
        items = copy.deepcopy(items)

    # INVARIANTS:
    #   mid_start < unsorted_start ≤ unsorted_end
    #   All the un-partitioned elements are in items[unsorted_start:unsorted_end+1]
    while unsorted_start <= unsorted_end:  # some items still not partitioned
        if items[unsorted_start] < pivot:  # bottom partition
            swap_elements(unsorted_start, mid_start)
            mid_start += 1
            unsorted_start += 1
        elif items[unsorted_start] > pivot:  # top partition
            swap_elements(unsorted_start, unsorted_end)
            unsorted_end -= 1
        else:  # already in correct location
            unsorted_start += 1
    # POST-CONDITION: `unsorted_start > unsorted_end` => after while loop:
    #   `unsorted_start` == FIRST item in RIGHT (val > pivot) partition
    #   `unsorted_end` == LAST item in MIDDLE (val == pivot) partition
    #   `mid_start` == FIRST item in MIDDLE (val == pivot) partition
    #       because `unsorted_start` ALWAYS increments with `mid_start` or by itself

    return items
