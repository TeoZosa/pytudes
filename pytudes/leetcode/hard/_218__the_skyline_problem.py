"""https://leetcode.com/problems/the-skyline-problem/

See Also:
    https://briangordon.github.io/2014/08/the-skyline-problem.html
"""

import heapq


class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        """
        Examples:
            >>> Solution().getSkyline([])
            []
        """
        return get_skyline(buildings)


def get_skyline(buildings: list[list[int]]) -> list[list[int]]:
    """Computes a city's skyline formed by all the buildings in a given city.

    A city's skyline is the outer contour of the silhouette
    formed by all the buildings in that city when viewed from a distance.

    You may assume all buildings are perfect rectangles
    grounded on an absolutely flat surface at height 0.

    Args:
        buildings: locations and heights of all the buildings
            in the form buildings[i] = [left_i, right_i, height_i]
            where:
                left_i: x coordinate of the left edge of the ith building.
                right_i: x coordinate of the right edge of the ith building.
                height_i: height of the ith building.

    Returns: the skyline formed by these buildings collectively.

        Represented as a list of "key points" sorted by their x-coordinate
            in the form [[x1,y1],[x2,y2],...].
        Each key point is the left endpoint of some horizontal segment in the skyline
            EXCEPT the last point in the list,
                which always has a y-coordinate 0
                and is used to mark the skyline's termination where the rightmost building ends.
        Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

        Constraint(s):
            There must be no consecutive horizontal lines of equal height in the output skyline.
                For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable;
                the three lines of height 5 should be merged into one in the final output as such:
                [...,[2 3],[4 5],[12 7],...]
    Examples:
        >>> get_skyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])
        [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
        >>> get_skyline([[0,2,3],[2,5,3]])
        [[0, 3], [5, 0]]
        >>> get_skyline([[1,2,1],[1,2,2],[1,2,3]])
        [[1, 3], [2, 0]]

    See Also:
        https://leetcode.com/problems/the-skyline-problem/discuss/61261/10-line-Python-solution-104-ms
    """
    """ALGORITHM"""
    heap_peek = lambda: min_heap[0]
    heap_pop = lambda: heapq.heappop(min_heap)
    heap_push = lambda item: heapq.heappush(min_heap, item)
    ## INITIALIZE VARS ##
    # DS's/res
    skyline, min_heap = [], [[0, float("inf")]]

    # Reorder `buildings` tuple elements so sorting priority is L, then H, then R
    L_H_R_triplets = [(L, -H, R) for L, R, H in buildings]

    # Isolate `buildings` R elements for heap filtering
    # and (optionally) discard R-overlapping buildings for efficiency (using set-comprehension)
    # Note: using tuples since they are hashable and sets need hashable types
    R_inf_none_triplets = {(R, float("inf"), None) for _, R, _ in buildings}

    # iterate over buildings R/L edges, sorted by R/L and height
    for L_or_R_x_coord, height, right_coord in sorted(
        L_H_R_triplets + list(R_inf_none_triplets)
    ):
        # Note:
        # L_or_R_x_coord:
        #   R if height is float("inf") and right_coord is None
        #   L otherwise

        # Remove heap entries with R ≤ L_or_R_x_coord
        #
        # Since we are iterating in sorted order, heap will only
        # have elements with R's that preceded the current `L_or_R_x_coord` x-coordinate
        # and thus have either:
        #   1. already been dealt with (i.e., `L_or_R_x_coord` is an L) or
        #   2. will be swallowed by the current interval (i.e., `L_or_R_x_coord` is an R)
        while L_or_R_x_coord >= heap_peek()[1]:
            _ = heap_pop()

        # Don't push the `R_inf_none_triplets ` items
        # since those were only there to exclude entries from the final skyline
        # in the previous step
        if right_coord:
            heap_push([height, right_coord])

        # Merge heights functionality: only append new skyline silhouette if
        # height is not equal to last silhouette height to adhere to constraint:
        # "no consecutive horizontal lines of equal height in the output skyline."
        last_silhouette_height = skyline[-1][1] if skyline else None
        max_curr_silhouettes_height = -heap_peek()[0]
        if last_silhouette_height != max_curr_silhouettes_height:
            skyline.append([L_or_R_x_coord, max_curr_silhouettes_height])

    return skyline
