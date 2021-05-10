"""https://leetcode.com/problems/maximum-subarray/

Constraints:
    - 1 ≤ nums.length ≤ 3 * 10^4
    - -10^5 ≤ nums[i] ≤ 10^5

Examples:
    >>> Solution().maxSubArray([])
    0

"""
import functools


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        return max_subarray_greedy(nums)


def max_subarray_greedy(nums: list[int]) -> int:
    """Returns the largest non-empty contiguous subarray sum

    A variant of Kadane's Algorithm.

    Args:
        nums: An array of integers drawn from the range [-10^5, 10^5]

    Examples:
        >>> max_subarray_greedy([-2,1,-3,4,-1,2,1,-5,4])
        6
        >>> max_subarray_greedy([1])
        1
        >>> max_subarray_greedy([5,4,-1,7,8])
        23
        >>> max_subarray_greedy([])
        0

    """
    ## EDGE CASE ##
    if not nums:
        return 0

    ## INITIALIZE VARS ##
    max_sum = curr_sum = -float("inf")
    for num in nums:
        # Reset subarray sum if current subarray sum is negative which
        # implies inclusion would produce a smaller subarray sum.
        if curr_sum < 0:
            curr_sum = num
        else:
            curr_sum += num
        max_sum = max(max_sum, curr_sum)

    return max_sum


def max_subarray_kadane(nums: list[int]) -> tuple[int, list[int]]:
    """Returns the largest non-empty contiguous subarray sum and corresponding subarray

    A variant of Kadane's Algorithm

    Args:
        nums: An array of integers drawn from the range [-10^5, 10^5]

    Examples:
        >>> max_subarray_kadane([-2,1,-3,4,-1,2,1,-5,4])
        (6, [4, -1, 2, 1])
        >>> max_subarray_kadane([1])
        (1, [1])
        >>> max_subarray_kadane([5,4,-1,7,8])
        (23, [5, 4, -1, 7, 8])
        >>> max_subarray_kadane([])
        (0, [])

    """
    ## EDGE CASE ##
    if not nums:
        return 0, nums

    ## INITIALIZE VARS ##
    max_sum = -float("inf")
    max_subarray_start_index = max_subarray_end_idx = 0

    curr_sum = 0
    start_index = 0
    for end_index, num in enumerate(nums):
        curr_sum += num

        if curr_sum > max_sum:
            max_sum = curr_sum
            max_subarray_start_index, max_subarray_end_idx = start_index, end_index

        # Reset subarray vars if current subarray sum is negative (i.e.,
        # adding it to any element would produce a smaller sum).
        if curr_sum < 0:
            curr_sum = 0
            start_index = end_index + 1

    return max_sum, nums[max_subarray_start_index : max_subarray_end_idx + 1]


def max_subarray_tabulate(nums: list[int]) -> int:
    """Returns the largest non-empty contiguous subarray sum

    Args:
        nums: An array of integers drawn from the range [-10^5, 10^5]

    Examples:
        >>> max_subarray_tabulate([-2,1,-3,4,-1,2,1,-5,4])
        6
        >>> max_subarray_tabulate([1])
        1
        >>> max_subarray_tabulate([5,4,-1,7,8])
        23
        >>> max_subarray_tabulate([])
        0

    """
    ## EDGE CASE ##
    if not nums:
        return 0

    ## INITIALIZE VARS ##
    # subarr_sum[i] contains the maximum possible sum achievable by a
    # contiguous subarray in nums consisting of nums[i] and, potentially,
    # the immediately *preceding* maximum sum contiguous subarray
    subarr_sum = nums.copy()  # subarr_sum[i] initialized with singleton subarray sums

    # Update each idx to contain the maximum contiguous subarry sum that could
    # be obtained by the inclusion of the element at that idx; in other words,
    # include a previously running subarray sum if it would produce a larger
    # sum, else ONLY include the element at that idx (thus starting a new
    # subarray partition)
    for i in range(1, len(nums)):
        if subarr_sum[i - 1] > 0:
            # a larger subarray sum would be achieved by including predecessor contiguous subarray
            subarr_sum[i] += subarr_sum[i - 1]
    return max(subarr_sum)


def max_subarray_memoize(nums: list[int]) -> int:
    """Returns the largest non-empty contiguous subarray sum

    Args:
        nums: An array of integers drawn from the range [-10^5, 10^5]

    Examples:
        >>> max_subarray_memoize([-2,1,-3,4,-1,2,1,-5,4])
        6
        >>> max_subarray_memoize([1])
        1
        >>> max_subarray_memoize([5,4,-1,7,8])
        23
        >>> max_subarray_memoize([])
        0

    """
    ## EDGE CASE ##
    if not nums:
        return 0

    ## INITIALIZE VARS ##
    # subarr_sum[i] contains the maximum possible sum achievable by a
    # contiguous subarray in nums consisting of nums[i] and, potentially,
    # the immediately *preceding* maximum sum contiguous subarray
    subarr_sum = [None] * len(nums)
    subarr_sum[0] = nums[0]

    def calculate_max_subarray_sum(index_to_include: int):
        if index_to_include == 0:  # base case already initialized
            return

        prev_max_sum_subarray = index_to_include - 1
        if subarr_sum[prev_max_sum_subarray] is None:
            calculate_max_subarray_sum(prev_max_sum_subarray)

        subarr_sum[index_to_include] = nums[index_to_include]  # initialize
        if subarr_sum[prev_max_sum_subarray] > 0:
            subarr_sum[index_to_include] += subarr_sum[prev_max_sum_subarray]

    # Update each idx to contain the maximum contiguous subarray sum that could
    # be obtained by the inclusion of the element at that idx; in other words,
    # include a previously running subarray sum if it would produce a larger
    # sum, else ONLY include the element at that idx (thus starting a new
    # subarray partition)
    calculate_max_subarray_sum(len(nums) - 1)
    return max(subarr_sum)


def max_subarray_recursive(nums: list[int]) -> int:
    """Returns the largest non-empty contiguous subarray sum

    Args:
        nums: An array of integers drawn from the range [-10^5, 10^5]

    Examples:
        >>> max_subarray_recursive([-2,1,-3,4,-1,2,1,-5,4])
        6
        >>> max_subarray_recursive([1])
        1
        >>> max_subarray_recursive([5,4,-1,7,8])
        23
        >>> max_subarray_recursive([])
        0

    """
    ## EDGE CASE ##
    if not nums:
        return 0

    def calculate_max_subarray_sum(index_to_include: int, max_sum=-float("inf")):
        if index_to_include == 0:  # base case
            return nums[0], nums[0]

        max_subarray_sum = nums[index_to_include]  # initialize
        prev_max_subarray_sum, prev_max_sum = calculate_max_subarray_sum(
            index_to_include - 1, max_sum
        )
        if prev_max_subarray_sum > 0:
            max_subarray_sum += prev_max_subarray_sum

        return max_subarray_sum, max(prev_max_sum, max_subarray_sum)

    # Update each idx to contain the maximum contiguous subarray sum that could
    # be obtained by the inclusion of the element at that idx; in other words,
    # include a previously running subarray sum if it would produce a larger
    # sum, else ONLY include the element at that idx (thus starting a new
    # subarray partition)
    _, max_sum = calculate_max_subarray_sum(len(nums) - 1)
    return max_sum


def max_subarray_cache(nums: list[int]) -> int:
    """Returns the largest non-empty contiguous subarray sum

    Args:
        nums: An array of integers drawn from the range [-10^5, 10^5]

    Examples:
        >>> max_subarray_cache([-2,1,-3,4,-1,2,1,-5,4])
        6
        >>> max_subarray_cache([1])
        1
        >>> max_subarray_cache([5,4,-1,7,8])
        23
        >>> max_subarray_cache([])
        0

    """
    if not nums:
        return 0

    @functools.lru_cache(maxsize=None)
    def max_subarray_sum_ending_at_index(i: int) -> int:
        ## Base Case ##
        if i < 0:
            return 0

        return max(nums[i], max_subarray_sum_ending_at_index(i - 1) + nums[i])

    return max([max_subarray_sum_ending_at_index(i) for i in range(len(nums))])
