"""https://www.educative.io/courses/grokking-the-coding-interview/N7rwVyAZl6D"""

from typing import Any, Optional


class Node:
    """
    Notes:
        "NodeType" forward reference
            Forward reference syntax: annotation as a string literal
            See Also: https://www.python.org/dev/peps/pep-0484/#id28
    """

    def __init__(self, value: Any, nxt: "NodeType" = None):
        self.value = value
        self.nxt = nxt

    def __iter__(self):
        curr = self
        while curr is not None:
            yield curr
            curr = curr.nxt

    def as_list(self):
        return [node.value for node in self]


NodeType = Optional[Node]


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
    """

    def convert_list_to_linked_list_iterative(arr: list[Any]) -> NodeType:
        if not arr:
            return None

        first, rest = arr[0], arr[1:]
        head = curr = Node(first)
        for val in rest:
            curr.nxt = Node(val)
            curr = curr.nxt
        return head

    def convert_list_to_linked_list_recursive(arr: list[Any]) -> NodeType:
        if not arr:
            return None
        first, rest = arr[0], arr[1:]
        head = Node(first)
        head.nxt = convert_list_to_linked_list_recursive(rest)
        return head

    return (
        convert_list_to_linked_list_recursive(arr)
        if recursive
        else convert_list_to_linked_list_iterative(arr)
    )
