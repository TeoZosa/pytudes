"""https://www.educative.io/courses/grokking-the-coding-interview/N7rwVyAZl6D

"""

from typing import Any, Optional


class ListNode:
    """

    Notes:
        "NodeType" is a forward reference
            Forward reference syntax: annotation as a string literal
            See Also: https://www.python.org/dev/peps/pep-0484/#id28

    """

    def __init__(self, val: Any, next_node: "NodeType" = None):
        self.val = val
        self.next = next_node

    def __iter__(self):
        curr = self
        while curr is not None:
            yield curr
            curr = curr.next

    def as_list(self):
        return [node.val for node in self]


NodeType = Optional[ListNode]


def convert_list_to_linked_list(arr: list[Any], recursive=False) -> NodeType:
    """

    Utility fn for easier testing

    Args:
        arr: input array of elements to convert
        recursive: whether or not to perform conversion recursively

    Returns:
        The head of the linked list derived from arr

    Examples:
        >>> convert_list_to_linked_list([2,4,6,8,10], recursive=False).as_list()
        [2, 4, 6, 8, 10]
        >>> convert_list_to_linked_list([2,4,6,8,10], recursive=True).as_list()
        [2, 4, 6, 8, 10]
        >>> assert(convert_list_to_linked_list([]) is None)

    """

    def convert_list_to_linked_list_iterative(arr: list[Any]) -> NodeType:
        if not arr:
            return None

        first, rest = arr[0], arr[1:]
        head = curr = ListNode(first)
        for val in rest:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    def convert_list_to_linked_list_recursive(arr: list[Any]) -> NodeType:
        if not arr:
            return None
        first, rest = arr[0], arr[1:]
        head = ListNode(first)
        head.next = convert_list_to_linked_list_recursive(rest)
        return head

    return (
        convert_list_to_linked_list_recursive(arr)
        if recursive
        else convert_list_to_linked_list_iterative(arr)
    )
