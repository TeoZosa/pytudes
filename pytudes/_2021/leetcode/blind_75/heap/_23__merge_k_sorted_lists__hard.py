"""https://leetcode.com/problems/merge-k-sorted-lists/

Constraints:
    - k == lists.length
    - 0 <= k <= 10^4
    - 0 <= lists[i].length <= 500
    - -10^4 <= lists[i][j] <= 10^4
    - lists[i] is sorted in ascending order.
    - The sum of lists[i].length won't exceed 10^4.

Examples:
    >>> assert(Solution().mergeKLists([None]) is None)

"""
import heapq
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

    # # If we could override ListNode definition, this would make algorithm using min heap cleaner
    # def __lt__(self, other):
    #     return self.val < other.val


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
        return merge_k_lists_heap(lists)


def merge_k_lists_heap(lists: list[ListNodeType]) -> ListNodeType:
    """Merge a list of linked-lists into a single, sorted linked-list

    Args:
        lists: array of linked-lists, each sorted in ascending order.

    Returns: a single merged, sorted linked-list

    Examples:
        >>> list_nodes = [convert_to_listnode(sublist) for sublist in [[1,4,5],[1,3,4],[2,6]]]
        >>> merge_k_lists_heap(list_nodes).as_list()
        [1, 1, 2, 3, 4, 4, 5, 6]
        >>> list_nodes = [convert_to_listnode(sublist) for sublist in [[1,1,4,5],[1,3,4],[2,6]]]
        >>> merge_k_lists_heap(list_nodes).as_list()
        [1, 1, 1, 2, 3, 4, 4, 5, 6]
        >>> assert (merge_k_lists_heap([convert_to_listnode([])]) is None)
        >>> assert(merge_k_lists_heap([]) is None)

    """
    ## EDGE CASES ##
    if not lists:
        return None

    """ALGORITHM"""
    ## INITIALIZE VARS ##
    # res
    min_heap = []

    ## Push root nodes of linked list onto min heap
    for list_idx, list_node in enumerate(lists):

        # Add root list nodes to heap, ordered by `val` and then `list_idx`
        # in other words, nodes with duplicate vals will be tie-broken by `list_idx
        #   `val` x `list_idx` guaranteed to be unique since
        #      - list_levels are unique
        # (needed to prevent heapq from comparing ListNodes which do not implement comparison functions)
        if list_node is not None:
            heapq.heappush(min_heap, (list_node.val, list_idx, list_node))

    ## PROCESS HEAP
    # Until empty: Pop min elements from heap & push their `.next` nodes onto heap

    # `head` is a handle to the final linked list we will return
    # i.e., `head.next` points to the root of the final linked list
    curr = head = ListNode()
    while len(min_heap) > 0:
        _, list_idx, next_node = heapq.heappop(min_heap)
        curr.next = next_node
        curr = curr.next

        # Add inner list nodes to heap, ordered by `val` and then `list_idx`
        # in other words, nodes with duplicate vals will be tie-broken by `list_idx
        #   `val` x `list_idx` guaranteed to be unique since
        #       - list_levels are unique
        #       - ONLY *ONE* item from each list will be in the heap at any one time
        # (needed to prevent heapq from comparing ListNodes which do not implement comparison functions)
        if (list_node := curr.next) is not None:
            heapq.heappush(min_heap, (list_node.val, list_idx, list_node))

    return head.next


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
        >>> assert(_merge_k_lists([]) is None)

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
