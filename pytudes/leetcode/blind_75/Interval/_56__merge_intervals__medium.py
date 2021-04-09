"""https://leetcode.com/problems/merge-intervals/

Constraints:
    - 1 <= intervals.length <= 104
    - intervals[i].length == 2
    - 0 <= starti <= endi <= 104

Examples:
    >>> Solution().merge([])
    []

See Also:
    - pytudes/educative/GrokkingTheCodingInterview/MergeIntervals/_1__merge_intervals__medium.py

"""


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        return merge(intervals)


def merge(intervals: list[list[int]]) -> list[list[int]]:
    """Generate a new schedule with non-overlapping intervals by merging intervals which overlap

    Complexity:
        n = len(intervals)
            Time: O(nlogn) for the initial sort
            Space: O(n) for the worst case of no overlapping intervals

    Examples:
        >>> merge(intervals=[[1,3],[2,6],[8,10],[15,18]])
        [[1, 6], [8, 10], [15, 18]]
        >>> merge(intervals=[[1,4],[4,5]])
        [[1, 5]]
        >>> merge(intervals=[[1,4]])
        [[1, 4]]

    """
    ## EDGE CASES ##
    if len(intervals) <= 1:
        return intervals

    """ALGORITHM"""
    ## INITIALIZE VARS ##
    intervals.sort(key=lambda k: k[0])  # sort on start times

    # DS's/res
    merged_intervals = []

    # MERGE INTERVALS
    prev_interval, remaining_intervals = intervals[0], intervals[1:]
    for curr_interval in remaining_intervals:
        # if prev interval end >= curr interval start
        if prev_interval[1] >= curr_interval[0]:
            # adjust new prev interval
            prev_interval[1] = max(prev_interval[1], curr_interval[1])
        else:
            merged_intervals.append(prev_interval)
            prev_interval = curr_interval
    merged_intervals.append(prev_interval)

    return merged_intervals
