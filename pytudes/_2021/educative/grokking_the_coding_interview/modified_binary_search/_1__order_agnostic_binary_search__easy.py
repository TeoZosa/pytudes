"""https://www.educative.io/courses/grokking-the-coding-interview/R8LzZQlj8lO

"""


def binary_search(arr: list[int], val: int) -> int:
    """Binary search modified to operate on both ascending and descending sorted arrays

    Complexity:
        Time: O(logn) & Ω(1)
        Space: O(1)

    Args:
        arr: array of numbers sorted in ascending or descending order
        val: element in arr for which to search

    Returns: index of val being searched if val is in items, else -1

    Examples:
        >>> binary_search([4, 6, 10],10)
        2
        >>> binary_search([1, 2, 3, 4, 5, 6, 7],5)
        4
        >>> binary_search([10, 6, 4],10)
        0
        >>> binary_search([10, 6, 4],4)
        2
        >>> binary_search([],0)
        -1
        >>> binary_search([1],0)
        -1

    """
    ## EDGE CASES ##
    if not arr:
        return -1

    """ALGORITHM"""
    check_left = lambda: val < arr[mid] if is_ascending else val > arr[mid]
    check_right = lambda: val > arr[mid] if is_ascending else val < arr[mid]
    ## INITIALIZE VARS
    start, end = 0, len(arr) - 1
    is_ascending = arr[start] <= arr[end]

    while start <= end:
        mid = (start + end) // 2
        if check_left():
            end = mid - 1
        elif check_right():
            start = mid + 1
        else:
            return mid
    else:
        return -1  # element not found


#
# def binary_search_orig(arr: list[int], val: int) -> int:
#     """
#
#     Args:
#         arr:
#         val:
#
#     Returns:
#
#     Examples:
#         >>> binary_search_orig([4, 6, 10],10)
#         2
#         >>> binary_search_orig([1, 2, 3, 4, 5, 6, 7],5)
#         4
#         >>> binary_search_orig([10, 6, 4],10)
#         0
#         >>> binary_search_orig([10, 6, 4],4)
#         2
#
#     """
#     start, end = 0, len(arr) - 1
#     isAscending = arr[start] < arr[end]
#
#     while start <= end:
#         # calculate the middle of the current range
#         mid = (start + end) // 2
#
#         if val == arr[mid]:
#             return mid
#
#         if isAscending:  # ascending order
#             if val < arr[mid]:
#                 end = mid - 1  # the 'key' can be in the first half
#             elif val > arr[mid]:
#                 start = mid + 1  # the 'key' can be in the second half
#             else:  # key > arr[mid]
#                 return mid
#         else:  # descending order
#             if val > arr[mid]:
#                 end = mid - 1  # the 'key' can be in the first half
#             else:  # key < arr[mid]
#                 start = mid + 1  # the 'key' can be in the second half
#
#     return -1  # element not found
