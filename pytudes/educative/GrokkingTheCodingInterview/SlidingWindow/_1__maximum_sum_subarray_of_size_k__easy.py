"""https://www.educative.io/courses/grokking-the-coding-interview/JPKr0kqLGNP

"""


def max_sum_sub_array_of_size_k(K: int, arr: list[int]) -> int:
    """

    Examples:
        >>> max_sum_sub_array_of_size_k(3,[2, 1, 5, 1, 3, 2])
        9
        >>> max_sum_sub_array_of_size_k(2,[2, 3, 4, 1, 5])
        7

    """
    ## EDGE CASES ##
    if not arr or K <= 0:
        return 0

    """ALGORITHM"""
    get_curr_win_size = lambda: window_end - window_start + 1
    ## INITIALIZE VARS ##

    max_sum, window_sum = 0, 0
    window_start = 0

    ## SLIDING
    for window_end in range(len(arr)):
        ## EXPANSION
        window_sum += arr[window_end]  # add the next element
        ## WINDOW MATCH
        if get_curr_win_size() == K:
            max_sum = max(max_sum, window_sum)
            ## CONTRACTION
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum
