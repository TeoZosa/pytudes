"""https://leetcode.com/problems/linked-list-cycle/

Constraints:
    - The number of the nodes in the list is in the range [0, 104].
    - -105 ≤ Node.val ≤ 105
    - pos is -1 or a valid index in the linked-list.

Examples:
    >>> Solution().hasCycle(None)
    False

"""
from pytudes.utils import linked_list

ListNode = linked_list.ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        return has_cycle(head)


def has_cycle(head: ListNode) -> bool:
    """Returns True if the linked list has a cycle, otherwise False

    There is a cycle in a linked list if there is some node in the list
    that can be reached again by continuously following the next pointer.

    Complexity:
        n = linkedlist length, k = cycle length (note: k < n)
        Time: O(n) = O(n + k)
            Cases:
                1. List has no cycle:
                    The fast pointer reaches the end first
                    and the run time depends on the list's length,
                    which is O(n).

                2. List has a cycle:
                    We break down the movement of the slow pointer into two steps,
                    the non-cyclic part and the cyclic part:

                        The slow pointer takes "non-cyclic length" steps to enter the cycle.
                        At this point, the fast pointer has already reached the cycle.
                        Number of iterations = non-cyclic length = N

                        Both pointers are now in the cycle.
                        Consider two runners running in a cycle -
                        the fast runner moves 2 steps
                        while the slow runner moves 1 steps at a time.

                        Since the speed difference is 1, it takes
                            (distance between the 2 runners)/(difference of speed)
                        loops for the fast runner to catch up with the slow runner.
                        As the distance is at most cyclic length K and the speed difference is 1, we conclude that
                            Number of iterations ~= cyclic length K
        Space: O(1) (two (a constant) pointers)

    Args:
        head: head of a singly-linked list of nodes

    Examples:
        >>> has_cycle(None)
        False
        >>> head = ListNode("self-edge")
        >>> head.next = head
        >>> has_cycle(head)
        True
        >>> head = linked_list.convert_list_to_linked_list([1,2,3,4,5,6])
        >>> has_cycle(head)
        False
        >>> head.next.next.next.next.next.next = head.next.next
        >>> has_cycle(head)
        True
        >>> head.next.next.next.next.next.next = head.next.next.next
        >>> has_cycle(head)
        True

    """

    """ALGORITHM"""
    # Floyd's Cycle Finding Algorithm:
    # Traverse list until a node is revisited (cycle)
    # or we complete traversal (acyclic)
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    else:
        return False


def has_cycle_hashtable(head: ListNode) -> bool:
    """Cycle-finding algorithm using a hashtable to mark nodes as visited

    Complexity:
        n = linkedlist length, k = cycle length (note: k < n)
        Time: O(n)
        Space: O(n) (size of the `visited` set)

    Args:
        head: head of a singly-linked list of nodes

    Returns:
        whether or not the linked list has a cycle

    Examples:
        >>> has_cycle(None)
        False
        >>> head = ListNode("self-edge")
        >>> head.next = head
        >>> has_cycle_hashtable(head)
        True
        >>> head = linked_list.convert_list_to_linked_list([1,2,3,4,5,6])
        >>> has_cycle_hashtable(head)
        False
        >>> head.next.next.next.next.next.next = head.next.next
        >>> has_cycle_hashtable(head)
        True
        >>> head.next.next.next.next.next.next = head.next.next.next
        >>> has_cycle_hashtable(head)
        True

    """

    """ALGORITHM"""

    ## INITIALIZE VARS ##
    # DS's/res
    visited = set()

    # Traverse list until a node is revisited (cycle)
    # or we complete traversal (acyclic)
    curr = head
    while curr is not None:
        if curr in visited:
            return True
        else:
            visited.add(curr)
        curr = curr.next
    else:
        return False
