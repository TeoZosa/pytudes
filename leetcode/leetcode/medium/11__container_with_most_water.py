"""
https://leetcode.com/problems/container-with-most-water
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        return compute_max_area(height)


def compute_max_area(heights: list[int]) -> int:
    """
    Given n non-negative integers a1, a2, ..., an , where each represents a
    point at coordinate (i, ai). n vertical lines are drawn such that the
    two endpoints of the line i is at (i, ai) and (i, 0). Find two lines,
    which, together with the x-axis forms a container, such that the
    container contains the most water.
    Args:
        heights: list of non-negative integers [a1, a2, ..., an],
                where each represents a point at coordinate (i, ai)
                i.e., the height of a vertical line at y-coordinate i is ai
    Returns:
        Maximum area achievable between any two elements in heights
    Examples:
        >>> compute_max_area(heights=[1,8,6,2,5,4,8,3,7])
        49
        >>> compute_max_area(heights=[4,3,2,1,4])
        16
        >>> compute_max_area(heights=[1,2,1])
        2
        >>> compute_max_area(heights=[1,1])
        1
        >>> compute_max_area(heights=[1])
        0
        >>> compute_max_area(heights=[])
        0
    """
    ## EDGE CASES ##
    if not heights:
        return 0

    ## INITIALIZE VARS ##
    l, r = 0, len(heights) - 1
    max_area = 0

    ## TWO POINTERS ##
    while l < r:
        interval_width = r - l
        left_height, right_height = heights[l], heights[r]
        min_height = min(left_height, right_height)
        max_area = max(max_area, interval_width * min_height)

        ## MOVE POINTER(S) ##
        if left_height < right_height:
            l += 1
        else:
            r -= 1

    return max_area
