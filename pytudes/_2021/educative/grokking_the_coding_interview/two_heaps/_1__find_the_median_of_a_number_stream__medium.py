"""https://www.educative.io/courses/grokking-the-coding-interview/3Yj2BmpyEy4

See Also:
    - pytudes/_2021/leetcode/blind_75/heap/_295__find_median_from_data_stream__hard.py

"""
import heapq


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

    def __init__(self):
        self._heap = []

    def __len__(self):
        return len(self._heap)

    def push(self, num: int) -> None:
        heapq.heappush(self._heap, num)

    def pop(self) -> int:
        return heapq.heappop(self._heap)

    def peek(self) -> int:
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


class NumberStreamTrackingMedian:
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
        >>> num_stream = NumberStreamTrackingMedian()
        >>> num_stream.insert_num(3)
        >>> num_stream.insert_num(1)
        >>> num_stream.find_median()
        2.0
        >>> num_stream.insert_num(5)
        >>> num_stream.find_median()
        3.0
        >>> num_stream.insert_num(4)
        >>> num_stream.find_median()
        3.5

    """

    def __init__(self):
        self._max_heap = MaxHeap()  # containing first half of numbers
        self._min_heap = MinHeap()  # containing second half of numbers

    def insert_num(self, num: int) -> None:
        """

        Args:
            num:

        Complexity:
                Time: O(logn)

        """
        ## PUSH to correct HEAP ##
        # O(logn) push
        if len(self._max_heap) == 0 or num <= self._max_heap.peek():
            self._max_heap.push(num)
        else:
            self._min_heap.push(num)

        ## RE-BALANCE HEAPS: enforce invariant ##
        # O(logn) pop + O(logn) push
        if len(self._max_heap) - 1 > len(self._min_heap):  # max_heap too big
            self._min_heap.push(self._max_heap.pop())  # max_heap[0] => min_heap
        elif len(self._max_heap) < len(self._min_heap):  # min_heap too big
            self._max_heap.push(self._min_heap.pop())  # min_heap[0] => max_heap

    def find_median(self) -> float:
        """

        Complexity:
                Time: O(1)

        Returns: Median of number stream

        Raises:
            RuntimeError: if there are no numbers stored in the MedianFinder object or if
            RuntimeError: if the heaps have invalid sizes

        Examples:
            >>> num_stream = NumberStreamTrackingMedian()
            >>> num_stream.find_median()
            Traceback (most recent call last):
            ...
            RuntimeError
            >>> num_stream._max_heap.push(0)
            >>> num_stream._max_heap.push(0)
            >>> num_stream.find_median()
            Traceback (most recent call last):
            ...
            RuntimeError: INVARIANT BROKEN:
            Heaps have invalid sizes;
            Were they modified manually??

        """
        if len(self._max_heap) == 0:
            raise RuntimeError

        if len(self._max_heap) - 1 == len(self._min_heap):  # odd
            return float(self._max_heap.peek())
        elif len(self._max_heap) == len(self._min_heap):  # even
            return (self._max_heap.peek() + self._min_heap.peek()) / 2
        else:
            raise RuntimeError(
                "INVARIANT BROKEN:\n"
                "Heaps have invalid sizes;\n"
                "Were they modified manually??"
            )


def main():
    medianOfAStream = NumberStreamTrackingMedian()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
