"""https://www.educative.io/courses/grokking-the-coding-interview/3jyVPKRA8yx"""


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return f"[{self.start}, {self.end}]"

    def as_list(self) -> list[int]:
        return [self.start, self.end]


def merge(intervals: list[Interval]) -> list[Interval]:
    """

    Args:
        intervals:

    Returns:
    Complexity:
        n = len(intervals)
            Time: O(nlogn)
            Space: O(n)

        Merged intervals: [1, 5][7, 9]
        Merged intervals: [2, 4][5, 9]
        Merged intervals: [1, 6]
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
    if len(intervals) < 2:
        return intervals

    """ALGORITHM"""
    # sort the intervals on the start time
    intervals.sort(key=lambda _interval: _interval.start)

    ## INITIALIZE VARS ##

    # vars
    last_interval, remaining_intervals = intervals[0], intervals[1:]
    # DS's/res
    mergedIntervals = []

    ## MERGE intervals ##
    for interval in remaining_intervals:
        if interval.start <= last_interval.end:  # overlapping intervals
            last_interval.end = max(interval.end, last_interval.end)  # adjust the 'end'
        else:  # non-overlapping interval
            # add the previous interval
            mergedIntervals.append(Interval(last_interval.start, last_interval.end))
            last_interval = interval  # update potentially overlapping interval
    # Add the last interval
    mergedIntervals.append(Interval(last_interval.start, last_interval.end))

    return mergedIntervals


def main():
    for intervals in [
        [Interval(1, 4), Interval(2, 5), Interval(7, 9)],
        [Interval(6, 7), Interval(2, 4), Interval(5, 9)],
        [Interval(1, 4), Interval(2, 6), Interval(3, 5)],
    ]:
        pretty_printed_intervals = ",".join(
            [str(i) for i in merge(intervals=intervals)]
        )
        print(f"Merged intervals: {pretty_printed_intervals}")


main()
