"""https://www.educative.io/courses/grokking-the-coding-interview/7XMlMEQPnnQ"""


def smallest_subarray_with_given_sum(target_sum: int, arr: list[int]) -> int:
    """
    Args:
        target_sum: target sum
        arr: numbers to explore
    Returns:
        LENGTH of smallest subarray with window_sum ≥ target_sum
    Examples:
        >>> smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])
        2
        >>> smallest_subarray_with_given_sum(8, [2, 1, 5, 2, 8])
        1
        >>> smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])
        3
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
    for window_end in range(len(arr)):
        ## EXPANSION
        window_sum += arr[window_end]

        ## WINDOW MATCH
        while window_sum >= target_sum:
            min_subarr_len = min(min_subarr_len, get_curr_win_size())

            ## CONTRACTION
            window_sum -= arr[window_start]
            window_start += 1

    return max(min_subarr_len, 0)
