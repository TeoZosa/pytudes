"""https://leetcode.com/problems/middle-of-the-linked-list/

Examples:
    >>> assert(Solution().middleNode(None) is None)

"""

from pytudes._2021.utils import linked_list

ListNode = linked_list.ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        return middle_node(head)


def middle_node(head: ListNode) -> ListNode:
    """Returns the middle node of the given linked list.

     If the cardinality of the linked list is even,
     returns the second middle node.

    Args:
        head:

    Examples:
        >>> head = linked_list.convert_list_to_linked_list([1,2,3,4,5,6])
        >>> middle_node(head).val
        4
        >>> head = linked_list.convert_list_to_linked_list([1,2,3,4,5])
        >>> middle_node(head).val
        3

    """
    """ALGORITHM"""
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
