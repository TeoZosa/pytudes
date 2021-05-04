"""https://leetcode.com/problems/merge-two-sorted-lists/

Constraints:
    - The number of nodes in both lists is in the range [0, 50].
    - -100 ≤ Node.val ≤ 100
    - Both l1 and l2 are sorted in non-decreasing order.

Examples:
    >>> Solution().mergeTwoLists(None, None)

"""
from pytudes.utils import linked_list

ListNode = linked_list.ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return merge_two_lists(l1, l2)


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """Returns a single sorted, in-place merged linked list of two sorted input linked lists

    The linked list is made by splicing together the nodes of l1 and l2

    Args:
        l1:
        l2:

    Examples:
        >>> l1 = linked_list.convert_list_to_linked_list([1,2,4])
        >>> l2 = linked_list.convert_list_to_linked_list([1,3,4])
        >>> merge_two_lists(l1, l2).as_list()
        [1, 1, 2, 3, 4, 4]
        >>> l1 = linked_list.convert_list_to_linked_list([])
        >>> l2 = linked_list.convert_list_to_linked_list([0])
        >>> merge_two_lists(l1, l2).as_list()
        [0]
        >>> merge_two_lists(l2, l1).as_list()
        [0]
        >>> merge_two_lists(None, None)

    """
    """ALGORITHM"""
    head_handle = curr = ListNode(None)
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            curr.next, l1 = l1, l1.next
        else:
            curr.next, l2 = l2, l2.next
        curr = curr.next
    # Post-condition:
    # if at least one list was not None, one list is now exhausted and `curr`
    # is the last node of the now exhausted list; complete splice by assigning
    # the head of the remaining non-exhausted list to `curr.next`
    curr.next = l1 if l1 is not None else l2

    return head_handle.next


import heapq


def merge_two_lists_heap(l1: ListNode, l2: ListNode) -> ListNode:
    """Returns a single sorted, in-place merged linked list of two sorted input linked lists

    The linked list is made by splicing together the nodes of l1 and l2

    Args:
        l1:
        l2:

    Examples:
        >>> l1 = linked_list.convert_list_to_linked_list([1,2,4])
        >>> l2 = linked_list.convert_list_to_linked_list([1,3,4])
        >>> merge_two_lists_heap(l1, l2).as_list()
        [1, 1, 2, 3, 4, 4]
        >>> l1 = linked_list.convert_list_to_linked_list([])
        >>> l2 = linked_list.convert_list_to_linked_list([0])
        >>> merge_two_lists_heap(l1, l2).as_list()
        [0]
        >>> merge_two_lists_heap(l2, l1).as_list()
        [0]
        >>> merge_two_lists_heap(None, None)

    """
    heap = []
    for k, list_k_head in enumerate([l1, l2]):
        curr = list_k_head
        while curr is not None:
            val_k_node_triple = (curr.val, k, curr)  # duplicate values tie-broken by k
            heapq.heappush(heap, val_k_node_triple)
            curr = curr.next

    head_handle = curr = ListNode(val=None)
    while heap:
        val, _, next_node = heapq.heappop(heap)
        curr.next = curr = next_node

    return head_handle.next
