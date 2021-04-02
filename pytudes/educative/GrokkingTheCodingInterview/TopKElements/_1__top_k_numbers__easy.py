"""https://www.educative.io/courses/grokking-the-coding-interview/RM535yM9DW0

"""
import heapq


def find_k_largest_numbers(nums: list[int], k: int) -> list[int]:
    """
    Complexity:
        Time: O(nlogk)
        Space O(k)
    Args:
        nums: array of numbers for which to find the largest k elements
        k: num largest elements to find

    Returns: the k largest elements in `nums`
    Examples:
        >>> find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)
        [5, 12, 11]
        >>> find_k_largest_numbers([5, 12, 11, -1, 12], 3)
        [11, 12, 12]

    """
    ## EDGE CASES ##
    if not nums:
        return nums

    """ALGORITHM"""
    ## INITIALIZE VARS ##

    # DS's/res
    min_heap = []

    ## HEAPIFY
    for idx, num in enumerate(nums):
        if idx < k:  # put first 'K' numbers in the min heap
            heapq.heappush(min_heap, num)
        else:
            # Maintain a k-sized min heap by only adding `num`
            # if it is bigger than the smallest (root) element in the min heap
            heapq.heappushpop(min_heap, num)  # noop if num < min_heap[0] (root)

    return min_heap
