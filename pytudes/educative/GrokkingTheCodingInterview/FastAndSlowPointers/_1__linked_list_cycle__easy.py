"""https://www.educative.io/courses/grokking-the-coding-interview/N7rwVyAZl6D

    Categories:
        Binary
        Bit Manipulation
        Blind 75

    See Also:
        https://leetcode.com/problems/linked-list-cycle/
"""

from pytudes.utils.linked_list import Node, NodeType, convert_list_to_linked_list


def has_cycle(head: NodeType) -> bool:
    """
    Args:
        head: head of a singly-linked list of nodes
    Returns:
        whether or not the linked list has a cycle
    Examples:
        >>> has_cycle(None)
        False
        >>> head = Node("self-edge")
        >>> head.nxt = head
        >>> has_cycle(head)
        True
        >>> head = convert_list_to_linked_list([1,2,3,4,5,6])
        >>> has_cycle(head)
        False
        >>> head.nxt.nxt.nxt.nxt.nxt.nxt = head.nxt.nxt
        >>> has_cycle(head)
        True
        >>> head.nxt.nxt.nxt.nxt.nxt.nxt = head.nxt.nxt.nxt
        >>> has_cycle(head)
        True
    """
    slow = fast = head
    while fast is not None and fast.nxt is not None:  # since fast ≥ slow
        slow = slow.nxt
        fast = fast.nxt.nxt
        if slow == fast:
            return True  # found the cycle
    else:
        return False


def main():
    head = convert_list_to_linked_list([1, 2, 3, 4, 5, 6])
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.nxt.nxt.nxt.nxt.nxt.nxt = head.nxt.nxt
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.nxt.nxt.nxt.nxt.nxt.nxt = head.nxt.nxt.nxt
    print("LinkedList has cycle: " + str(has_cycle(head)))


main()
