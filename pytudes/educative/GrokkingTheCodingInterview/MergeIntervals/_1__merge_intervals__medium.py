"""https://www.educative.io/courses/grokking-the-coding-interview/3jyVPKRA8yx

    Categories:
        Blind 75
        Interval

    See Also:
        https://leetcode.com/problems/merge-intervals/
"""


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return str(self.as_list())

    def as_list(self) -> list[int]:
        return [self.start, self.end]


def merge(intervals: list[Interval]) -> list[Interval]:
    """Generate a new schedule with non-overlapping intervals by merging intervals which overlap

    Complexity:
        n = len(intervals)
            Time: O(nlogn) for the initial sort
            Space: O(n) for the worst case of no overlapping intervals
    Examples:
        >>> [i.as_list() for i in merge(
        ... intervals=[Interval(1, 4), Interval(2, 5), Interval(7, 9)])
        ... ]
        [[1, 5], [7, 9]]
        >>> [i.as_list() for i in merge(
        ... intervals=[Interval(6, 7), Interval(2, 4), Interval(5, 9)])
        ... ]
        [[2, 4], [5, 9]]
        >>> [i.as_list() for i in merge(
        ... intervals=[Interval(1, 4), Interval(2, 6),Interval(3, 5)])
        ... ]
        [[1, 6]]
    """
    ## EDGE CASES ##
    if not intervals or len(intervals) < 2:
        return intervals

    """ALGORITHM"""
    # sort the intervals on start time
    intervals.sort(key=lambda _interval: _interval.start)

    ## INITIALIZE VARS ##
    prev_interval, remaining_intervals = intervals[0], intervals[1:]

    # DS's/res
    merged_intervals = []

    for curr_interval in remaining_intervals:
        if curr_interval.start <= prev_interval.end:  # overlapping intervals
            ## MERGE intervals ##
            # by (potentially) updating the previous interval's end
            prev_interval.end = max(curr_interval.end, prev_interval.end)
        else:  # non-overlapping interval
            ## CHECK NEXT interval ##
            merged_intervals.append(Interval(prev_interval.start, prev_interval.end))
            prev_interval = curr_interval
    # Add the last interval
    merged_intervals.append(Interval(prev_interval.start, prev_interval.end))

    return merged_intervals


def main():
    for intervals in [
        [Interval(1, 4), Interval(2, 5), Interval(7, 9)],
        [Interval(6, 7), Interval(2, 4), Interval(5, 9)],
        [Interval(1, 4), Interval(2, 6), Interval(3, 5)],
    ]:
        original_intervals_pretty_printed = ",".join([str(i) for i in intervals])
        print(f"Original intervals: {original_intervals_pretty_printed}")

        merged_intervals_pretty_printed = ",".join([str(i) for i in merge(intervals)])
        print(f"Merged intervals: {merged_intervals_pretty_printed}")

        print()


main()
