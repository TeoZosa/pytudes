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
