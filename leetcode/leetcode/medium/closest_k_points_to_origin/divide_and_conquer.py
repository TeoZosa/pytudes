"""
Quick Select - O(N) *on average*; Space: O(N)
  a modified quick-sort like algorithm

if we quickselect by some pivot,
    *on average in linear time*
we'll halve the problem space


"""

import random


class Solution:
    def kClosest(self, points: list[list[int]], K: int) -> list[list[int]]:
        """
        Examples:
            >>> Solution().kClosest([[1,3],[-2,2]], 1)
            [[-2, 2]]
            >>> res = Solution().kClosest([[3,3],[5,-1],[-2,4]], 2)
            >>> assert (sorted(res) == [[-2, 4], [3, 3]])
        """
        sort(points, start_idx=0, end_idx=len(points) - 1, K=K)
        return points[:K]


# side effects: `points` mutation
def sort(points, start_idx, end_idx, K):
    """
    Partially sorts A[start_idx:end_idx+1]
    so the first K elements
    are the smallest K elements.

    Examples:
        >>> points, K = [[1,3],[-2,2]], 1
        >>> start_idx, end_idx = 0, len(points) - 1
        >>> sort(points, start_idx, end_idx, K)
        >>> assert( points == [[-2, 2], [1, 3]])
    """

    # No elements (ptrs crossed) => already sorted
    is_base_case = lambda: start_idx >= end_idx
    if is_base_case():
        return
    else:  # divide and conquer
        mid_idx = partition(points, start_idx, end_idx)
        recurse(points, start_idx, end_idx, mid_idx, K)


# side effects: `points` mutation
def partition(points, start_idx, end_idx):
    """
    Partition by pivot A[i],
    returning an index mid
    such that
        A[start_idx] <= A[mid_idx] <= A[end_idx]
            for start_idx < mid_idx < end_idx.

    Examples:
        >>> points= [[3,3],[5,-1],[-2,4]]
        >>> start_idx, end_idx = 0, len(points) - 1
        >>> mid_idx = partition(points,start_idx,end_idx)
        >>> assert(mid_idx in list(range(start_idx, end_idx+1)))
    """

    pivot_idx = _compute_pivot_idx_and_swap_to_start(points, start_idx, end_idx)
    pivot_distance = get_distance(points, pivot_idx)
    mid_idx = _do_partition_and_get_mid_idx(
        points, start_idx + 1, end_idx, pivot_distance
    )
    # Swap pivot to mid (since A[mid] ≤ A[pivot])
    swap_elements(points, pivot_idx, mid_idx)
    return mid_idx


def _compute_pivot_idx_and_swap_to_start(points, start_idx, end_idx, rand_pivot=True):
    """
    Segregate pivot at start of array
        i.e. points == [pivot] + unpartitioned_points_array
    equivalent to an in-place scratch space sub-array
    """
    if rand_pivot:
        pivot_idx = random.randint(start_idx, end_idx)  # inclusive range
        swap_elements(points, start_idx, pivot_idx)
    return start_idx


def _do_partition_and_get_mid_idx(points, left_ptr, right_ptr, pivot_distance):
    """Swap larger elements in left partition with smaller elements in right partition"""

    def find_swappable_partition_idxs():
        # find larger (than pivot) item in left partition
        nonlocal left_ptr
        while not ptrs_crossed() and get_distance(points, left_ptr) <= pivot_distance:
            left_ptr += 1

        # find smaller (than pivot )item in right partition
        nonlocal right_ptr
        while not ptrs_crossed() and get_distance(points, right_ptr) >= pivot_distance:
            right_ptr -= 1
        return left_ptr, right_ptr  # Redundant but reduces obtuseness

    ptrs_crossed = lambda: left_ptr > right_ptr

    # post-condition: A[right_ptr] ≤ A[pivot_idx]
    while not ptrs_crossed():
        left_ptr, right_ptr = find_swappable_partition_idxs()
        if not ptrs_crossed():  # Swap items to correct partition
            swap_elements(points, left_ptr, right_ptr)
    # else: Base case: degenerate sub-arrays <=> already partitioned
    mid_idx = right_ptr
    return mid_idx


def recurse(points, start_idx, end_idx, mid_idx, K):
    """
    Args:
        points: partitioned around mid_idx
            A[start_idx] <= A[mid_idx] <= A[end_idx]
        mid_idx: pivot value
        K: num closest points needed

    Examples:
        >>> points, K = [[-2, 4], [3, 3], [5, -1]], 1
        >>> start_idx, end_idx, mid_idx = 0, 2, 2
        >>> recurse(points, start_idx, end_idx, mid_idx, K)
        >>> assert( points == [[3, 3], [-2, 4], [5, -1]])

        >>> points, K = [[3, 3], [-2, 4], [5, -1]], 2
        >>> start_idx, end_idx, mid_idx = 0, 1, 1
        >>> recurse(points, start_idx, end_idx, mid_idx, K)
        >>> assert( points == [[3, 3], [-2, 4], [5, -1]])
    """
    get_left_partition_size = lambda: mid_idx - start_idx + 1
    if K < get_left_partition_size():
        # => left partition has enough elements to get K smallest eleemnts
        # <==> can ignore right partition entirely
        # ==> get next K smallest elements in the left partition
        left_start_idx, left_end_idx = start_idx, mid_idx - 1
        sort(points, left_start_idx, left_end_idx, K=K)
    elif K > get_left_partition_size():
        # => left partition already has |left partition| smallest elements
        # <==> can ignore left partition entirely
        # ==> get next K - |left_partition| smallest elements in the
        # right partition
        right_begin, right_end = mid_idx + 1, end_idx
        sort(points, right_begin, right_end, K=(K - get_left_partition_size()))


def swap_elements(points, i, j) -> None:
    points[i], points[j] = points[j], points[i]


def get_distance(points, idx) -> int:
    """
    Examples
        >>> get_distance([[1,3],[-2,2]],0)
        10
        >>> get_distance([[1,3],[-2,2]],1)
        8
    """
    return sum([coord ** 2 for coord in points[idx]])


class Solution_simple:
    def kClosest(self, points: list[list[int]], K: int) -> list[list[int]]:

        """
        Examples:
            >>> Solution_simple().kClosest([[1,3],[-2,2]], 1)
            [[-2, 2]]
            >>> res = Solution_simple().kClosest([[3,3],[5,-1],[-2,4]], 2)
            >>> assert (sorted(res) == [[-2, 4], [3, 3]])
        """

        def sort(points, start_idx, end_idx, K):
            is_base_case = lambda: start_idx >= end_idx
            if is_base_case():
                return
            else:  # divide and conquer
                mid_idx = partition(points, start_idx, end_idx)

                # Recurse
                left_partition_size = mid_idx - start_idx + 1
                if K < left_partition_size:
                    left_start_idx, left_end_idx = start_idx, mid_idx - 1
                    sort(points, left_start_idx, left_end_idx, K=K)
                elif K > left_partition_size:
                    right_begin, right_end = mid_idx + 1, end_idx
                    sort(points, right_begin, right_end, K=(K - left_partition_size))

        # side effects: `points` mutation
        def partition(points, start_idx, end_idx):
            pivot_idx = _compute_pivot_idx_and_swap_to_start(points, start_idx, end_idx)
            pivot_distance = get_distance(points, pivot_idx)
            mid_idx = _do_partition_and_get_mid_idx(
                points, start_idx + 1, end_idx, pivot_distance
            )
            swap_elements(points, pivot_idx, mid_idx)
            return mid_idx

        sort(points, start_idx=0, end_idx=len(points) - 1, K=K)
        return points[:K]


if __name__ == "__main__":
    import xdoctest

    xdoctest.doctest_module(__file__, command="all")
