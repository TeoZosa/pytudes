"""
https://leetcode.com/problems/k-closest-points-to-origin/

QuickSelect (Hoare's selection algorithm):
    Find the kth-smallest element in an unordered list via relatively sorting
    the list up to the kth element =>
    the k closest elements are the first k elements in the relatively sorted list.


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
            K: num closest points to origin to return
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


def _quickselect(
    points: list[list[int]], start: int, end: int, num_closest_points: int
) -> None:
    """In-place Quickselect of points[start:end+1] for K=num_closest_points

    Complexity:
        n = len(points)
            Time: O(n) *on average*
            Space: O(n)
    """

    def swap_elements(i, j) -> None:
        points[i], points[j] = points[j], points[i]

    get_distance = lambda i: sum([coord ** 2 for coord in points[i]])

    ## BASE CASE ##
    if start >= end:
        return

    ## INITIALIZE VARS ##
    pivot_idx = random.randint(start, end)  # inclusive range
    pivot_distance = get_distance(pivot_idx)

    ## 3-WAY PARTITION ##
    # INVARIANT: mid_start < unsorted_start ≤ unsorted_end
    swap_elements(start, pivot_idx)  # move pivot to start for variable name correctness
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
    left_end, mid_end, right_start = mid_start - 1, unsorted_end, unsorted_end + 1

    ## DIVIDE & CONQUER ##
    left_and_mid_partition_size = mid_end - start + 1
    if num_closest_points < left_and_mid_partition_size:  # RECURSE LEFT
        remaining_num_closest_points = num_closest_points
        _quickselect(points, start, left_end, remaining_num_closest_points)
    elif num_closest_points > left_and_mid_partition_size:  # RECURSE RIGHT
        remaining_num_closest_points = num_closest_points - left_and_mid_partition_size
        _quickselect(points, right_start, end, remaining_num_closest_points)
