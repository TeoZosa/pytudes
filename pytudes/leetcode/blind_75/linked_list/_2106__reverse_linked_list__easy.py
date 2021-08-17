"""https://leetcode.com/problems/reverse-linked-list/

Examples:
    >>> assert(Solution().reverseList(None) is None)

See Also:
    - pytudes/educative/grokking_the_coding_interview/in_place_reversal_of_a_linked_list/_1__reverse_a_linked_list__easy.py

"""
from pytudes._2021.utils.linked_list import ListNode, convert_list_to_linked_list

ListNode = ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return reverse_list(head)


def reverse_list(head: ListNode) -> ListNode:
    """

    Args:
        head: head of a linked list of nodes

    Returns: the head of the in-place-reversed linked list (i.e. original tail)

    Examples:
        >>> head = convert_list_to_linked_list([1,2,3,4,5])
        >>> head.as_list()
        [1, 2, 3, 4, 5]
        >>> head = reverse_list(head)
        >>> head.as_list()
        [5, 4, 3, 2, 1]
        >>> head = convert_list_to_linked_list([1,2])
        >>> reverse_list(head).as_list()
        [2, 1]
        >>> head = convert_list_to_linked_list([])
        >>> assert(reverse_list(head) is None)

    """

    """ALGORITHM"""
    prev, curr = None, head
    while curr is not None:  # if not curr: return prev
        # reverse curr.next link, update prev & curr ptrs
        curr.next, prev, curr = prev, curr, curr.next  # do reversal
    return prev
