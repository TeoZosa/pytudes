"""https://www.educative.io/courses/grokking-the-coding-interview/3Yj2BmpyEy4

See Also:
    - pytudes/_2021/educative/grokking_the_coding_interview/two_heaps/_1__find_the_median_of_a_number_stream__medium.py

"""
import heapq
from typing import Optional


class MinHeap:
    """heapq-based interface

    Examples:
        >>> heap = MinHeap()
        >>> heap.push(1)
        >>> heap.push(2)
        >>> heap.push(3)
        >>> len(heap)
        3
        >>> heap.peek()
        1
        >>> heap.pop()
        1
        >>> heap.pop()
        2
        >>> heap.pop()
        3
    """

    def __init__(self) -> None:
        self._heap = []

    def __len__(self) -> int:
        return len(self._heap)

    def push(self, num: int) -> None:
        heapq.heappush(self._heap, num)

    def pop(self) -> int:
        return heapq.heappop(self._heap)

    def peek(self) -> Optional[int]:
        return self._heap[0]


class MaxHeap(MinHeap):
    """MinHeap with negated numbers

    Examples:
        >>> heap = MaxHeap()
        >>> heap.push(1)
        >>> heap.push(2)
        >>> heap.push(3)
        >>> heap.peek()
        3
        >>> heap.pop()
        3
        >>> heap.pop()
        2
        >>> heap.pop()
        1
    """

    def push(self, num: int) -> None:
        super().push(-num)

    def pop(self) -> int:
        return -super().pop()

    def peek(self) -> int:
        return -super().peek()
