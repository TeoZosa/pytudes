""" https://leetcode.com/problems/k-closest-points-to-origin/

QuickSelect (Hoare's selection algorithm):
    Find the kth-smallest element in an unordered list via relatively sorting
    the list up to the kth element =>
    the k closest elements are the first k elements in the relatively sorted list.

Examples:
    >>> Solution().kClosest([[1,3],[-2,2]], K=1)
    [[-2, 2]]

See Also:
    - pytudes/_2021/miscellany/sorting/dutch_nation_flag_problem.py
    - pytudes/_2021/miscellany/sorting/quicksort.py

"""

import copy
import random


class Solution:
    def kClosest(self, points: list[list[int]], K: int) -> list[list[int]]:
        return k_closest(points, K)


def k_closest(
    points: list[list[int]], K: int, in_place: bool = True
) -> list[list[int]]:
    """

    Complexity:
        n = len(points)
            Time: O(n) *on average*
            Space: O(n)

    Args:
        points: list of [x,y] coordinate pairs
        K: num closest points to origin to return [1-indexed]
        in_place: whether or not to perform the partitioning in-place

    Returns:
         the K closest points to the origin

    Examples:
        >>> random.seed(32)
        >>> assert(k_closest([[1,3],[-2,2]], K=1, in_place=True) == k_closest([[1,3],[-2,2]], K=1, in_place=False))
        >>> k_closest([[1,3],[-2,2]], K=1)
        [[-2, 2]]
        >>> k_closest([[3,3],[5,-1],[-2,4]], K=2)
        [[3, 3], [-2, 4]]
        >>> points = [
        ...      [-63, -55], [-20, 17], [-88, -82], [-90, -95], [-88, 18],
        ...      [-62, -21], [71, -64], [-14, 56], [65, 90], [-48, -52],
        ...      [59, 92], [-44, -59], [-3, -66]
        ... ]
        >>> k_closest(points,K=7)
        [[-20, 17], [-14, 56], [-62, -21], [-3, -66], [-48, -52], [-44, -59], [-63, -55]]

    """
    if not in_place:
        points = copy.deepcopy(points)
    _quickselect(points, start=0, end=len(points) - 1, num_closest_points=K)
    return points[:K]


def kth_closest(points: list[list[int]], K: int, in_place: bool = True) -> list[int]:
    """

    Complexity:
        n = len(points)
            Time: O(n) *on average*
            Space: O(n)

    Args:
        points: list of [x,y] coordinate pairs
        K: the num closest point to origin to return [1-indexed]
        in_place: whether or not to perform the partitioning in-place

    Returns:
         the Kth-closest point to the origin

    Examples:
        >>> assert(kth_closest([[1,3],[-2,2]], K=1, in_place=True) == kth_closest([[1,3],[-2,2]], K=1, in_place=False))
        >>> kth_closest([[1,3],[-2,2]], K=1)
        [-2, 2]
        >>> kth_closest([[3,3],[5,-1],[-2,4]], K=2)
        [-2, 4]
        >>> points = [
        ...      [-63, -55], [-20, 17], [-88, -82], [-90, -95], [-88, 18],
        ...      [-62, -21], [71, -64], [-14, 56], [65, 90], [-48, -52],
        ...      [59, 92], [-44, -59], [-3, -66]
        ... ]
        >>> kth_closest(points,K=7)
        [-63, -55]
    """
    if not in_place:
        points = copy.deepcopy(points)
    _quickselect(points, start=0, end=len(points) - 1, num_closest_points=K)
    kth_idx = K - 1
    return points[kth_idx]


def _quickselect(
    points: list[list[int]], start: int, end: int, num_closest_points: int
) -> None:
    """Recursive in-place Quickselect of points[start:end+1] for K=num_closest_points

    Complexity:
        n = len(points)
            Time: O(n) *on average*
            Space: O(n)

    Args:
        points: list of [x,y] coordinate pairs
        start: start index bounding the quickselection
        end: end index bounding the quickselection
        num_closest_points: the num closest point to origin to return [1-indexed]

    Returns:

    Examples:
        >>> random.seed(32)
        >>> points = [
        ...      [-63, -55], [-63, -55], [-20, 17], [-88, -82], [-90, -95], [-88, 18],
        ...      [-62, -21], [71, -64], [-14, 56], [65, 90], [-48, -52],
        ...      [59, 92], [-44, -59], [-3, -66]
        ... ]
        >>> _quickselect(points, start=0, end=len(points) - 1, num_closest_points=5)
        >>> points
        [[-20, 17], [-14, 56], [-62, -21], [-3, -66], [-48, -52], [-44, -59], [-63, -55], [-63, -55], [65, 90], [71, -64], [59, 92], [-88, 18], [-90, -95], [-88, -82]]

    """

    def swap_elements(i, j) -> None:
        points[i], points[j] = points[j], points[i]

    get_distance = lambda i: sum(coord ** 2 for coord in points[i])

    ## INITIALIZE VARS ##
    pivot_idx = random.randint(start, end)  # inclusive range
    pivot_distance = get_distance(pivot_idx)

    ## 3-WAY PARTITION ##
    # INVARIANT: mid_start < unsorted_start ≤ unsorted_end
    swap_elements(start, pivot_idx)  # move pivot to start for var name correctness
    mid_start, unsorted_start, unsorted_end = start, start + 1, end
    while unsorted_start <= unsorted_end:
        if get_distance(unsorted_start) < pivot_distance:  # left partition move
            swap_elements(unsorted_start, mid_start)
            mid_start += 1
            unsorted_start += 1
        elif get_distance(unsorted_start) > pivot_distance:  # right partition move
            swap_elements(unsorted_start, unsorted_end)
            unsorted_end -= 1
        else:  # already in correct location
            unsorted_start += 1
    left_end, right_start = mid_start - 1, unsorted_end + 1

    ## DIVIDE & CONQUER ##
    kth_idx = num_closest_points - 1
    if kth_idx <= left_end:  # K points somewhere LEFT
        _quickselect(points, start, left_end, num_closest_points)
    elif kth_idx >= right_start:  # K-(left+mid) points somewhere RIGHT
        _quickselect(points, right_start, end, num_closest_points)
    ## BASE CASE ##
    else:  # K points exactly in left + at least 1 element in mid
        return


def _quickselect_iterative(
    points: list[list[int]], start: int, end: int, num_closest_points: int
) -> None:
    """In-place Quickselect of points[start:end+1] for K=num_closest_points

    Complexity:
        n = len(points)
            Time: O(n) *on average*
            Space: O(n)

    Args:
        points: list of [x,y] coordinate pairs
        start: start index bounding the quickselection
        end: end index bounding the quickselection
        num_closest_points: the num closest point to origin to return [1-indexed]

    Returns:

    Examples:

        >>> random.seed(32)
        >>> points = [
        ...      [-63, -55], [-63, -55], [-20, 17], [-88, -82], [-90, -95], [-88, 18],
        ...      [-62, -21], [71, -64], [-14, 56], [65, 90], [-48, -52],
        ...      [59, 92], [-44, -59], [-3, -66]
        ... ]
        >>> _quickselect_iterative(points, start=0, end=len(points) - 1, num_closest_points=5)
        >>> points
        [[-20, 17], [-14, 56], [-62, -21], [-3, -66], [-48, -52], [-44, -59], [-63, -55], [-63, -55], [65, 90], [71, -64], [59, 92], [-88, 18], [-90, -95], [-88, -82]]

    """

    def swap_elements(i, j) -> None:
        points[i], points[j] = points[j], points[i]

    get_distance = lambda i: sum(coord ** 2 for coord in points[i])

    ## BASE CASE ##
    while start < end:

        ## INITIALIZE VARS ##
        pivot_idx = random.randint(start, end)  # inclusive range
        pivot_distance = get_distance(pivot_idx)

        ## 3-WAY PARTITION ##
        # INVARIANT: mid_start < unsorted_start ≤ unsorted_end
        swap_elements(start, pivot_idx)  # move pivot to start for var name correctness
        mid_start, unsorted_start, unsorted_end = start, start + 1, end
        while unsorted_start <= unsorted_end:
            if get_distance(unsorted_start) < pivot_distance:  # LEFT partition move
                swap_elements(unsorted_start, mid_start)
                mid_start += 1
                unsorted_start += 1
            elif get_distance(unsorted_start) > pivot_distance:  # RIGHT partition move
                swap_elements(unsorted_start, unsorted_end)
                unsorted_end -= 1
            else:  # already in correct location
                unsorted_start += 1
        left_end, right_start = mid_start - 1, unsorted_end + 1

        ## DIVIDE & CONQUER ##
        kth_idx = num_closest_points - 1
        if kth_idx <= left_end:  # K points somewhere LEFT
            end = left_end
        elif kth_idx >= right_start:  # K-(left+mid) points somewhere RIGHT
            start = right_start
        ## BASE CASE ##
        else:  # K points exactly in left + at least 1 element in mid
            return
