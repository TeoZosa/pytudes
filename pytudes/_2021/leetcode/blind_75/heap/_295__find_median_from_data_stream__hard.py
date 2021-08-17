"""https://leetcode.com/problems/find-median-from-data-stream/

See Also:
    - pytudes/_2021/educative/grokking_the_coding_interview/two_heaps/_1__find_the_median_of_a_number_stream__medium.py

"""
import heapq


class MedianFinder:
    """

    Invariant: at any time, either:
        1. max_heap is 1 element larger (odd) =>  median is max_heap root
        2. heap sizes are equal (even) => median is avg of heap roots

    Complexity:
        n = len(max_heap) + len(min_heap) <=> size of input number stream
        Time: O(nlogn)
        Space: O(n)
            => Given invariant:
                => len(max_heap) ~= n/2 = O(n)
                => len(min_heap) ~= n/2 = O(n)

    Examples:
        >>> num_stream = MedianFinder()
        >>> num_stream.addNum(3)
        >>> num_stream.addNum(1)
        >>> num_stream.findMedian()
        2.0
        >>> num_stream.addNum(5)
        >>> num_stream.findMedian()
        3.0
        >>> num_stream.addNum(4)
        >>> num_stream.findMedian()
        3.5

    """

    def __init__(self):
        self.max_heap = (
            []
        )  # containing first half of numbers (and extra if cardinality is odd)
        self.min_heap = []  # containing second half of numbers

    def max_heap_push(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)

    def min_heap_push(self, num: int) -> None:
        heapq.heappush(self.min_heap, num)

    def max_heap_pop(self) -> int:
        return -heapq.heappop(self.max_heap)

    def min_heap_pop(self) -> int:
        return heapq.heappop(self.min_heap)

    def max_heap_peek(self) -> int:
        return -self.max_heap[0]

    def min_heap_peek(self) -> int:
        return self.min_heap[0]

    def addNum(self, num: int) -> None:
        """

        Complexity:
                Time: O(logn)

        Args:
            num:

        """
        if len(self.max_heap) == 0 or num <= self.max_heap_peek():
            self.max_heap_push(num)
        else:
            self.min_heap_push(num)

        # rebalance heaps?
        # max heap must equal min heap or have ONLY 1 extra element
        if len(self.max_heap) - 1 > len(self.min_heap):  # max_heap has too many
            self.min_heap_push(self.max_heap_pop())

        # min heap must equal max meap or have ONLY 1 fewer element
        # should never have more elements
        elif len(self.min_heap) > len(self.max_heap):  # min heap has too many
            self.max_heap_push(self.min_heap_pop())

    def findMedian(self) -> float:
        """

        Complexity:
                Time: O(1)

        Returns: median of current numbers stored in the MedianFinder object

        Raises:
            RuntimeError: if there are no numbers stored in the MedianFinder object

        Examples:
            >>> num_stream = MedianFinder()
            >>> num_stream.findMedian()
            Traceback (most recent call last):
            ...
            RuntimeError

        """
        if len(self.max_heap) == 0:
            raise RuntimeError

        if len(self.max_heap) == len(self.min_heap):
            return (self.max_heap_peek() + self.min_heap_peek()) / 2
        else:
            return float(self.max_heap_peek())


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
