"""https://leetcode.com/problems/linked-list-cycle/

Constraints:
    - The number of the nodes in the list is in the range [0, 104].
    - -105 <= Node.val <= 105
    - pos is -1 or a valid index in the linked-list.


Examples:
    >>> Solution().hasCycle(None)
    False

"""
from pytudes.utils.linked_list import Node, convert_list_to_linked_list

ListNode = Node
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x: int):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        return has_cycle(head)


def has_cycle(head: ListNode) -> bool:
    """

    Args:
        head: head of a singly-linked list of nodes

    Returns: whether or not the linked list has a cycle

    Examples:
        >>> has_cycle(None)
        False
        >>> head = ListNode("self-edge")
        >>> head.next = head
        >>> has_cycle(head)
        True
        >>> head = convert_list_to_linked_list([1,2,3,4,5,6])
        >>> has_cycle(head)
        False
        >>> head.next.next.next.next.next.next = head.next.next
        >>> has_cycle(head)
        True
        >>> head.next.next.next.next.next.next = head.next.next.next
        >>> has_cycle(head)
        True

    """
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    else:
        return False
