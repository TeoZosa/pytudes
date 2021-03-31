"""
https://www.educative.io/courses/grokking-the-coding-interview/7D5NNZWQ8Wr
"""


def find_averages_of_subarrays_pythonic(K: int, arr: list[int]) -> list[float]:
    """

    Args:
        K: subarray (window) size
        arr: input array

    Returns:
        average of all K-length subarrays

    Examples:
        >>> find_averages_of_subarrays_pythonic(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
        [2.2, 2.8, 2.4, 3.6, 2.8]

    """

    ## EDGE CASES ##
    default_ret_val = []
    if not arr:
        return default_ret_val
    if K <= 0:
        return default_ret_val

    """ALGORITHM """
    ## INITIALIZE VARS ##

    window_start, window_end = 0, K - 1
    window_sum = float(sum(arr[window_start:window_end]))

    # DS's/res
    res = []

    ## SLIDING
    for window_end in range(window_end, len(arr)):
        ## EXPANSION
        window_sum += arr[window_end]  # handle_window_expansion_at_end
        ## WINDOW MATCH
        res.append(window_sum / K)  # handle_window_match
        ## CONTRACTION
        window_sum -= arr[window_start]  # handle_window_contraction_at_beginning
        window_start += 1
    return res


def find_averages_of_subarrays(target_window_size: int, arr: list[int]) -> list[float]:
    """
    Args:
        target_window_size: subarray (window) size
        arr: input array

    Returns:
        average of all K-length subarrays
        i.e. of size len(arr)-K + 1

    Examples:
        >>> find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
        [2.2, 2.8, 2.4, 3.6, 2.8]

    """
    ## EDGE CASES ##
    if target_window_size <= 0 or target_window_size > len(arr):
        return []

    """ALGORITHM"""
    get_curr_win_size = lambda: window_end - window_start + 1
    ## INITIALIZE VARS ##

    window_start, window_sum = 0, 0.0

    # DS's/res
    averages = []

    ## SLIDING
    for window_end in range(len(arr)):
        # EXPANSION
        window_sum += arr[window_end]

        ## WINDOW MATCH
        if get_curr_win_size() == target_window_size:
            averages.append(window_sum / target_window_size)

        ## CONTRACTION
        if get_curr_win_size() == target_window_size:
            window_sum -= arr[window_start]
            window_start += 1

    return averages
