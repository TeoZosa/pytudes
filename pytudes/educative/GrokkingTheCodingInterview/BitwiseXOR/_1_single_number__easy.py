"""https://www.educative.io/courses/grokking-the-coding-interview/gk20xz4VwpG

"""


def find_single_number(arr: list[int]) -> int:
    """Finds the single number in a non-empty array of integers where every number appears exactly twice, except for one which appears exactly once.

    Complexity:
        Time: O(n)
        Space: O(1)

    Args:
        arr: array of numbers with all but a single element appearing exactly twice,
            the single element that does not appear two times appears exactly once

    Returns: the single element that appears exactly once

    Examples:
        >>> find_single_number([1, 4, 2, 1, 3, 2, 3])
        4

    """
    """ALGORITHM"""
    ## INITIALIZE VARS ##
    single_number = 0

    # XOR of all values in arr:
    #   all duplicate elements will cancel out
    #   leaving `single_number ^ 0` = `single_number`
    for num in arr:  # REDUCE
        single_number ^= num
    return single_number
