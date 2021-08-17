"""https://www.educative.io/courses/grokking-the-coding-interview/3jyVPKRA8yx

"""
import heapq


class Job:
    def __init__(self, start: int, end: int, cpu_load: int):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        """for MinHeap based on job.end"""
        return self.end < other.end


class MinHeap:
    """heapq-based interface"""

    def __init__(self):
        self._heap = []

    def __len__(self):
        return len(self._heap)

    def push(self, job: Job) -> None:
        heapq.heappush(self._heap, job)

    def pop(self) -> Job:
        return heapq.heappop(self._heap)

    def peek(self) -> Job:
        return self._heap[0]


def find_max_cpu_load(jobs: list[Job]) -> int:
    """

    Complexity:
        n = len(jobs)
            Time: O(nlogn) for the initial sort
            Space: O(n) for the worst case of all non-vacuous jobs with the same end time

    Returns: the missing number in the range [0,n]

    Examples:
        >>> find_max_cpu_load(jobs=[])
        0
        >>> find_max_cpu_load(jobs=[Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)])
        7
        >>> find_max_cpu_load(jobs=[Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)])
        15
        >>> find_max_cpu_load(jobs=[Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)])
        8

    """
    if not jobs:
        return 0

    """ALGORITHM"""
    # sort jobs by start time
    jobs.sort(key=lambda _job: _job.start)

    ## INITIALIZE VARS ##
    current_cpu_load = 0

    # DS's/res
    min_heap = MinHeap()
    max_cpu_load = 0

    for curr_job in jobs:
        # Remove previous jobs that have ended
        while len(min_heap) > 0 and min_heap.peek().end <= curr_job.start:
            ## UN-MERGE intervals ##
            current_cpu_load -= min_heap.pop().cpu_load
        # Add the current job
        min_heap.push(curr_job)

        ## MERGE intervals ##
        current_cpu_load += curr_job.cpu_load
        max_cpu_load = max(max_cpu_load, current_cpu_load)

    return max_cpu_load


def main():
    for jobs in [
        [Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)],
        [Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)],
        [Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)],
    ]:
        print(f"Maximum CPU load at any time: {find_max_cpu_load(jobs)}")


main()
