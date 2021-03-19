"""
https://leetcode.com/problems/k-closest-points-to-origin/

QuickSelect (Hoare's selection algorithm):
    Find the kth-smallest element in an unordered list via relatively sorting
    the list up to the kth element =>
    the k closest elements are the first k elements in the relatively sorted list.

    Complexity:
        n = len(points)
            Time: O(n) *on average*
            Space: O(n)

See Also:
    leetcode/Miscellany/sorting/dutch_nation_flag_problem.py
    leetcode/Miscellany/sorting/quicksort.py
"""

import random
import copy


class Solution:
    def kClosest(
        self, points: list[list[int]], K: int, in_place: bool = True
    ) -> list[list[int]]:
        """
        Args:
            points: list of [x,y] coordinate pairs
            K: num closest points to origin to return [1-indexed]
            in_place: whether or not to perform the partitioning in-place
        Returns:
             the K closest points to the origin
        Examples:
            >>> Solution().kClosest([[1,3],[-2,2]], K=1)
            [[-2, 2]]
            >>> res = Solution().kClosest([[3,3],[5,-1],[-2,4]], K=2)
            >>> sorted(res)
            [[-2, 4], [3, 3]]
            >>> points = [
            ...      [-63, -55], [-20, 17], [-88, -82], [-90, -95], [-88, 18],
            ...      [-62, -21], [71, -64], [-14, 56], [65, 90], [-48, -52],
            ...      [59, 92], [-44, -59], [-3, -66]
            ... ]
            >>> res = Solution().kClosest(points,K=7)
            >>> sorted(res)
            [[-63, -55], [-62, -21], [-48, -52], [-44, -59], [-20, 17], [-14, 56], [-3, -66]]
        """
        if not in_place:
            points = copy.deepcopy(points)
        _quickselect(points, start=0, end=len(points) - 1, num_closest_points=K)
        return points[:K]


def kth_closest(points: list[list[int]], K: int, in_place: bool = True) -> list[int]:
    """
    Args:
        points: list of [x,y] coordinate pairs
        K: the num closest point to origin to return [1-indexed]
        in_place: whether or not to perform the partitioning in-place
    Returns:
         the Kth-closest point to the origin
    Examples:
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
    return points[K - 1]


def _quickselect(
    points: list[list[int]], start: int, end: int, num_closest_points: int
) -> None:
    """In-place Quickselect of points[start:end+1] for K=num_closest_points"""

    def swap_elements(i, j) -> None:
        points[i], points[j] = points[j], points[i]

    get_distance = lambda i: sum([coord ** 2 for coord in points[i]])

    ## BASE CASE ##
    if end < num_closest_points:
        return

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
    if num_closest_points <= left_end:  # K points somewhere in LEFT
        _quickselect(points, start, left_end, num_closest_points)
    elif num_closest_points > right_start:  # K-(left+mid) points somewhere in RIGHT
        _quickselect(points, right_start, end, num_closest_points)
    # else: # K points exactly in left and (potentially) some of mid


def _quickselect_iterative(
    points: list[list[int]], start: int, end: int, num_closest_points: int
) -> None:
    """In-place Quickselect of points[start:end+1] for K=num_closest_points"""

    def swap_elements(i, j) -> None:
        points[i], points[j] = points[j], points[i]

    get_distance = lambda i: sum([coord ** 2 for coord in points[i]])

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
        if num_closest_points <= left_end:  # LEFT has ALL K points
            end = left_end
        elif num_closest_points > right_start:  # RIGHT has K-(left+mid) points
            start = right_start
        else:  # K points exactly in left and (potentially) some of mid
            return
