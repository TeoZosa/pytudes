"""https://www.educative.io/courses/grokking-the-coding-interview/g2w6QPBA2Nk

Given an array of lowercase letters sorted in ascending order,
find the smallest letter in the given array *strictly* greater than a given ‘key’.

Assume the given array is a circular list, which means that:
    the last letter is assumed to be connected with the first letter.

This also means that:
    the first letter of the array is the smallest letter
    and is greater than the last letter of the array
        min(letters) == letters[0]
        max(letters) == letters[-1]
        <=> letters[0] < letters[-1]
        but val < letters[0] <=> letters[-1] < val

See Also:
    - pytudes/Miscellany/insertion_sort.py:46

"""


def search_next_letter(letters: list[str], val: str) -> str:
    """Binary search to find the successor of a given letter, defined as the smallest element *strictly* greater than the given letter

    Args:
        letters: circular array of letters sorted in ascending order
        val: element in letters for which to find the immediate successor

    Complexity:
        Time: Θ(logn) <=> O(logn) & Ω(logn) (since we must consider duplicates)
        Space: O(1)

    Returns: the immediate successor letter of val

    Examples:
        >>> search_next_letter(['a', 'c', 'f', 'h'],'f')
        'h'
        >>> search_next_letter(['a', 'c', 'f', 'h'],'b')
        'c'
        >>> search_next_letter(['a', 'c', 'f', 'h'],'m')
        'a'
        >>> search_next_letter(['a', 'c', 'f', 'f', 'h'],'f')
        'h'

    """

    ## EDGE CASES ##
    if not letters:
        raise ValueError
    if val < letters[0] or val > letters[-1]:  # if 'val' lies between cycle start/end
        return letters[0]

    """ALGORITHM"""
    ## INITIALIZE VARS ##
    start, end = 0, len(letters) - 1

    ## BINARY SEARCH ##
    while start <= end:
        mid = (start + end) // 2
        if val < letters[mid]:
            end = mid - 1
        else:  # val >= letters[mid]:
            start = mid + 1
    # letters[start] is the immediate successor to val
    # See Also: pytudes/Miscellany/searching/binary_search.py:19

    return letters[start % len(letters)]  # Note: redundant given edge-case check
