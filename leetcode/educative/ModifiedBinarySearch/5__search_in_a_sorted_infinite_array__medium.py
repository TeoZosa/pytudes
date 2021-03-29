"""https://www.educative.io/courses/grokking-the-coding-interview/B1ZW38kXJB2

"""
from typing import Union


class ArrayReader:
    def __init__(self, arr: list[int]):
        self.arr = arr

    def get(self, index: int, default_val: float = float("inf")) -> Union[int, float]:
        return self.arr[index] if index < len(self.arr) else default_val

    # Array notation access
    # def __getitem__(self, item):
    #     return self.arr[item] if item < len(self.arr) else float("inf")


def search_in_infinite_array(array_reader: ArrayReader, val: int) -> int:
    """Binary search to find given number ‘val’ in an infinite sorted array (or an array with unknown size)

        Since it is not possible to define an array with infinite/unknown size,
        the ArrayReader interface is used to read elements of the array.
            ArrayReader.get(index) will return the number at index;
        if index exceeds array bounds, it will return float("inf").

        note: MAY NEVER FINISH if array is truly infinite (i.e., stream) and duplicates are allowed
        else it must eventually finish if val is < infinity
    Args:
        array_reader: infinite sorted array (or an array with unknown size) INTERFACE
        val: element in array_read for which to find
    Complexity:
        N = size of finite subset (end - start +1) of infinite array
        Time: Θ(logn) <=> O(logn) & Ω(logn) (since we continously double array bounds to find finite subset)
        Space: O(1)
    Returns: the idx of val if val is present, else -1
    Examples:
        >>> reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
        >>> search_in_infinite_array(reader, 16)
        6
        >>> search_in_infinite_array(reader, 11)
        -1
        >>> reader = ArrayReader([1, 3, 8, 10, 15])
        >>> search_in_infinite_array(reader, 15)
        4
        >>> search_in_infinite_array(reader, 200)
        -1
    """
    ## EDGE CASES ##
    if not array_reader:
        return -1
    """ALGORITHM"""
    # find the proper bounds first
    start, end = 0, 1
    # continuously double bounds until val ≤ array_reader.get(end)
    # (Θ(logn) due to doubling at each iteration)
    while array_reader.get(end) < val:
        arr_size_doubled = (end - start + 1) * 2
        start, end = end + 1, end + arr_size_doubled

    ## BINARY SEARCH ##
    while start <= end:
        mid = (start + end) // 2
        if val < array_reader.get(mid):  # LEFT
            end = mid - 1
        elif val > array_reader.get(mid):  # RIGHT
            start = mid + 1
        else:  # found
            return mid
    else:  # not found
        return -1
