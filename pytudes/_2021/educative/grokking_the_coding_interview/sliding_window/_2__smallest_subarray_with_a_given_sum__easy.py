"""https://www.educative.io/courses/grokking-the-coding-interview/7XMlMEQPnnQ

"""


def smallest_subarray_with_given_sum(arr: list[int], target_sum: int) -> int:
    """

    Args:
        target_sum: target sum
        arr: numbers to explore

    Returns:
        LENGTH of smallest subarray with window_sum ≥ target_sum

    Examples:
        >>> smallest_subarray_with_given_sum([2, 1, 5, 2, 3, 2],7)
        2
        >>> smallest_subarray_with_given_sum([2, 1, 5, 2, 8],8)
        1
        >>> smallest_subarray_with_given_sum([3, 4, 1, 1, 6],8)
        3
        >>> smallest_subarray_with_given_sum([],8)
        0

    """

    ## EDGE CASES ##
    if not arr:
        return 0

    """ALGORITHM"""
    get_curr_win_size = lambda: window_end - window_start + 1
    ## INITIALIZE VARS ##
    window_start, window_sum = 0, 0

    # DS's/res var
    min_subarr_len = float("inf")

    ## SLIDING
    for window_end in range(len(arr)):  # pylint: disable=consider-using-enumerate
        ## EXPANSION
        window_sum += arr[window_end]

        ## WINDOW MATCH
        while window_sum >= target_sum:
            min_subarr_len = min(min_subarr_len, get_curr_win_size())

            ## CONTRACTION
            window_sum -= arr[window_start]
            window_start += 1

    return max(min_subarr_len, 0)
