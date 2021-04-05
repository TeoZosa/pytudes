"""https://leetcode.com/problems/merge-k-sorted-lists/

    Constraints:
        k == lists.length
        0 <= k <= 10^4
        0 <= lists[i].length <= 500
        -10^4 <= lists[i][j] <= 10^4
        lists[i] is sorted in ascending order.
        The sum of lists[i].length won't exceed 10^4.

    Examples:
        >>> Solution().mergeKLists([[]])
        []

    Categories:
        Heap
        Blind 75
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int = None):
        self.val = x
        self.next = None

    def __iter__(self):
        curr = self
        while curr is not None:
            yield curr
            curr = curr.next

    def as_list(self):
        return [node.val for node in self]


ListNodeType = Optional[ListNode]


# Original signature: def mergeKLists(self, lists: List[ListNode]) -> ListNode;
# Since ListNodes can be None, this is technically not correct


def convert_to_listnode(arr: list[int]) -> ListNodeType:
    if not arr:
        return None
    first, rest = arr[0], arr[1:]
    head = curr = ListNode(first)
    for val in rest:
        curr.next = ListNode(val)
        curr = curr.next
    return head


class Solution:
    def mergeKLists(self, lists: list[ListNodeType]) -> ListNodeType:
        return _merge_k_lists(lists)


def _merge_k_lists(lists: list[ListNodeType]) -> ListNodeType:
    """Merge a list of linked-lists into a single, sorted linked-list

    Args:
        lists: array of linked-lists, each sorted in ascending order.

    Returns: a single merged, sorted linked-list

    Examples:
        >>> list_nodes = [convert_to_listnode(sublist) for sublist in [[1,4,5],[1,3,4],[2,6]]]
        >>> _merge_k_lists(list_nodes).as_list()
        [1, 1, 2, 3, 4, 4, 5, 6]
        >>> _merge_k_lists([[]])
        []
        >>> assert(_merge_k_lists([]) == None)


    """
    ## EDGE CASES ##
    if not lists:
        return None

    """ALGORITHM"""
    ## BASE CASE
    if len(lists) == 1:
        return lists[0]

    mid = len(lists) // 2
    left, right = _merge_k_lists(lists[:mid]), _merge_k_lists(lists[mid:])
    return merge(left, right)


def merge(*args):
    default = False
    return merge_default(*args) if default else merge_alt(*args)


def merge_alt(left, right):
    if not (left and right):
        # return the non-None ListNode, if one exists
        return left or right
    elif left.val < right.val:
        left.next = merge_default(left.next, right)
        return left
    else:
        right.next = merge_default(left, right.next)
        return right


def merge_default(left, right):
    merged_handle = merged = ListNode()
    while left and right:
        if left.val < right.val:
            merged.next, left = left, left.next
        else:
            merged.next, right = right, right.next
        merged = merged.next

    # either l or r (or both) is now None
    # => make merged.next point to the non-None ListNode
    merged.next = left or right
    return merged_handle.next
