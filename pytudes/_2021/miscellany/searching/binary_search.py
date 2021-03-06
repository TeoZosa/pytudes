"""

Useful lemma:

    Binary search post-condition:
        1. if FOUND =>
            ************************************
            * arr[mid] == val                  *
            * arr[start] ≤ arr[mid] ≤ arr[end] *
            ************************************
            in the worst case of logn iterations:
                arr[start] == arr[mid] == arr[end]

        2. otherwise NOT FOUND =>
            arr[end] < val < arr[start]
            <=>
            ************************************
            * arr[end] is IMMEDIATE PREDECESSOR*
            * arr[start] is IMMEDIATE SUCCESSOR*
            ************************************
            note: indexes may be out-of-bounds, so must check; i.e.,
                end == -1
                start == len(arr)

Note:
    `middle = (start + end) // 2`
    has a good chance of producing an integer overflow (IN LANGUAGES OTHER THAN PYTHON)
    so it’s generally recommended that you represent the middle as
    `middle = start + (end — start) // 2`

    BUT in Python INTEGERS DO NOT TYPICALLY OVERFLOW;
    from https://docs.python.org/3/library/exceptions.html#OverflowError:
        ```
        exception OverflowError
            Raised when the result of an arithmetic operation is too large to be represented.
            This cannot occur for integers
            (which would rather raise MemoryError than give up).
            However, for historical reasons,
            OverflowError is sometimes raised for integers that are outside a required range.
            Because of the lack of standardization of floating point exception handling in C,
            most floating point operations are not checked.

        ```
"""


def binary_search(items: list, val) -> int:
    """

    Args:
        items:
        val:

    Returns: index of val being searched if val is in items, else -1

    Examples:
        >>> binary_search([0,1,2,3,4,5], val = 6)
        -1
        >>> binary_search([], val = 2)
        -1
        >>> binary_search([0,1,2,3,4,5], val = 2)
        2
        >>> binary_search([0,1,2,2,3,4,5], val = 2)
        3
        >>> binary_search([0,1,2,2,3,4,5], val = 0)
        0

    """
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if val > items[mid]:  # Search RIGHT
            start = mid + 1
        elif val < items[mid]:  # Search LEFT
            end = mid - 1
        else:  # Found idx of val
            return mid
    else:
        return -1


def binary_search_recursive(items: list, val) -> int:
    """

    Args:
        items:
        val:

    Returns:

    Examples:
        >>> binary_search_recursive([0,1,2,3,4,5], val = 6)
        -1
        >>> binary_search_recursive([], val = 2)
        -1
        >>> binary_search_recursive([0,1,2,3,4,5], val = 2)
        2
        >>> binary_search_recursive([0,1,2,2,3,4,5], val = 2)
        3
        >>> binary_search_recursive([0,1,2,2,3,4,5], val = 0)
        0

    """
    return _binary_search_recursive(items, 0, len(items) - 1, val)


def _binary_search_recursive(items: list, start, end, val) -> int:
    ## BASE CASE ##
    if start > end:
        return -1

    mid = (start + end) // 2
    if val > items[mid]:  # Search RIGHT
        return _binary_search_recursive(items, mid + 1, end, val)
    elif val < items[mid]:  # Search LEFT
        return _binary_search_recursive(items, start, mid - 1, val)
    else:  # Found idx of val
        return mid
