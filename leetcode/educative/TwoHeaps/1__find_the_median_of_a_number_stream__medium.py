"""https://www.educative.io/courses/grokking-the-coding-interview/3Yj2BmpyEy4"""
import heapq


class MinHeap:
    """heapq-based interface"""

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
    """MinHeap with negated numbers"""

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
        Returns: Median of number stream
        Complexity:
                Time: O(1)
        """
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
    pass
    medianOfAStream = NumberStreamTrackingMedian()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
