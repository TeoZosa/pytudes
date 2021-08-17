"""https://leetcode.com/problems/reverse-linked-list/

Constraints:
    - The number of nodes in the list is the range [0, 5000].
    - -5000 ≤ Node.val ≤ 5000

Examples:
    >>> assert(Solution().reverseList(None) is None)

"""

from pytudes._2021.utils import linked_list

ListNode = linked_list.ListNode

from typing import Optional


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return reverse_list(head)


def reverse_list(head: ListNode) -> ListNode:
    """Returns an in-place reversed linked list

    Args:
        head: head of a linked list of nodes

    Returns: the head of the in-place-reversed linked list (i.e. original tail)

    Examples:
        >>> head = linked_list.convert_list_to_linked_list([1,2,3,4,5])
        >>> reverse_list(head).as_list()
        [5, 4, 3, 2, 1]
        >>> head = linked_list.convert_list_to_linked_list([1,2])
        >>> reverse_list(head).as_list()
        [2, 1]

    """
    """ALGORITHM"""
    prev, curr = None, head
    while curr is not None:
        curr.next, prev, curr = prev, curr, curr.next
    return prev


def reverse_list_recursive(head: ListNode, prev: Optional[ListNode] = None) -> ListNode:
    """Returns an in-place reversed linked list

    Args:
        head: head of a linked list of nodes
        prev: node that preceded head in the linkest list

    Returns: the head of the in-place-reversed linked list (i.e. original tail)

    Examples:
        >>> head = linked_list.convert_list_to_linked_list([1,2,3,4,5])
        >>> reverse_list_recursive(head).as_list()
        [5, 4, 3, 2, 1]
        >>> head = linked_list.convert_list_to_linked_list([1,2])
        >>> reverse_list_recursive(head).as_list()
        [2, 1]

    """
    """ALGORITHM"""
    ## BASE CASE ##
    if head is None:
        return prev

    # REVERSAL
    head.next, next_node = prev, head.next

    ## RECURSIVE CASE
    return reverse_list_recursive(head=next_node, prev=head)
