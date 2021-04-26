"""https://www.educative.io/courses/grokking-the-coding-interview/N7rwVyAZl6D

Categories:
    - Binary
    - Bit Manipulation
    - Blind 75

See Also:
    - pytudes/leetcode/blind_75/LinkedList/_141__linked_list_cycle__easy.py

"""

from pytudes.utils.linked_list import ListNode, NodeType, convert_list_to_linked_list


def has_cycle(head: NodeType) -> bool:
    """

    Args:
        head: head of a singly-linked list of nodes

    Returns:
        whether or not the linked list has a cycle

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
    while fast is not None and fast.next is not None:  # since fast ≥ slow
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True  # found the cycle
    else:
        return False


def main():
    head = convert_list_to_linked_list([1, 2, 3, 4, 5, 6])
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))


main()
