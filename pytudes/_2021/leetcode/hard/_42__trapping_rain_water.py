""" https://leetcode.com/problems/trapping-rain-water/

Examples:
    >>> Solution().trap([])
    0

See Also:
    - pytudes/_2021/leetcode/blind_75/array/_11__container_with_most_water__medium.py

"""


class Solution:
    def trap(self, height: list[int]) -> int:
        return compute_trapped_rain_water(height)


def compute_trapped_rain_water(heights: list[int]) -> int:
    """
    Given n non-negative integers representing an elevation map (height)
    where the width of each bar is 1,
    compute how much water it can trap after raining.

    Notes:
        if `left_max_height` and `right_max_height` are the maximum heights
        of the already-processed left and right elevations, respectively:

            For each index i:
                Since the amount of water we can trap is bounded by:
                    `min(left_max_height, right_max_height)`
                and since no water can be trapped in space already taken up by:
                    `heights[i]`
                this means that we trap exactly:
                    `min(left_max_height, right_max_height) - heights[i]` water.

        heights =
        2,0,1,0,3,1,0,2,2,0,4
                            []
                []          []
        []      []    [][]  []
        []__[]__[][]__[][]__[]
        0|2|1|2|0|1|2|1|1|2|0
        = trapped_rain_water_at_each_idx
        => sum(trapped_rain_water_at_each_idx) = trapped_rain_water

    Args:
        heights: list of non-negative integers [a1, a2, ..., an],
                where each represents a point at coordinate (i, ai)
                i.e., the height of a vertical line at y-coordinate i is ai

    Returns: Sum of areas between heights unbroken

    Examples:
        >>> compute_trapped_rain_water(heights=[0,1,0,2,1,0,1,3,2,1,2,1])
        6
        >>> compute_trapped_rain_water(heights=[4,2,0,3,2,5])
        9
        >>> compute_trapped_rain_water(heights=[1,0,1])
        1
        >>> compute_trapped_rain_water(heights=[1,1])
        0
        >>> compute_trapped_rain_water(heights=[1])
        0
        >>> compute_trapped_rain_water(heights=[])
        0

    """
    ## EDGE CASES ##
    if not heights:
        return 0

    ## INITIALIZE VARS ##
    l, r = 0, len(heights) - 1
    left_max_height, right_max_height = 0, 0

    # res
    trapped_water = 0

    ## TWO POINTERS ##
    while l < r:
        left_height, right_height = heights[l], heights[r]
        left_max_height = max(left_max_height, left_height)
        right_max_height = max(right_max_height, right_height)

        ## MOVE POINTER(S) ##
        # Add `min(left_max_height, right_max_height) - heights[i]`
        if left_max_height <= right_max_height:
            trapped_water += left_max_height - left_height
            l += 1
        else:
            trapped_water += right_max_height - right_height
            r -= 1

    return trapped_water
