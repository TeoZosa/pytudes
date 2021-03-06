"""https://www.educative.io/courses/grokking-the-coding-interview/3wENz1N4WW9"""

from typing import Any, Optional


class Node:
    def __init__(self, value: Any, nxt: bool = None):
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


# [p =(p.n)> c =(c.n)> ...]
# [<(p.n)= p X c =(c.n)> n]; *n:= c.n*
# [<(p.n)= p <(c.n)= c X n]
# [p <(c.n)= c X n =(n.n)> n']; p, c = c, n
def reverse(head: NodeType, recursive=False) -> NodeType:
    """
    Args:
        head: head of a linked list of nodes
        recursive: whether or not to perform reversal recursively
    Returns:
        the head of the in-place-reversed linked list (i.e. original tail)
    Examples:
        >>> head = convert_list_to_linked_list([2,4,6,8,10])
        >>> head.as_list()
        [2, 4, 6, 8, 10]
        >>> head = reverse(head)
        >>> head.as_list()
        [10, 8, 6, 4, 2]
    """
    return reverse_recursive(head) if recursive else reverse_iterative(head)


def reverse_iterative(curr: NodeType, prev: NodeType = None) -> NodeType:
    """
    Args:
        curr: head of a linked list of nodes
        prev: previous node (if one exists)
    Returns:
        the head of the in-place-reversed linked list (i.e. original tail)
    Examples:
        >>> head = convert_list_to_linked_list([2,4,6,8,10])
        >>> head.as_list()
        [2, 4, 6, 8, 10]
        >>> head = reverse_iterative(head)
        >>> head.as_list()
        [10, 8, 6, 4, 2]
    """
    while curr is not None:  # if not curr: return prev
        # reverse curr.next link, update prev & curr ptrs
        curr.nxt, prev, curr = prev, curr, curr.nxt  # do reversal
    return prev


def reverse_recursive(curr: NodeType, prev: NodeType = None) -> NodeType:
    """
    Args:
        curr: head of a linked list of nodes
        prev: previous node (if one exists)
    Returns:
        the head of the in-place-reversed linked list (i.e. original tail)
    Examples:
        >>> head = convert_list_to_linked_list([2,4,6,8,10])
        >>> head.as_list()
        [2, 4, 6, 8, 10]
        >>> head = reverse_recursive(head)
        >>> head.as_list()
        [10, 8, 6, 4, 2]
    """
    if not curr:
        return prev
    # reverse next link, update prev & curr ptrs
    curr.nxt, prev, curr = prev, curr, curr.nxt  # do reversal at curr node
    return reverse_recursive(curr, prev)


def reverse_with_temp(head: NodeType) -> NodeType:
    """
    Args:
        head: head of a linked list of nodes
    Returns:
        the head of the in-place-reversed linked list (i.e. original tail)
    Examples:
        >>> head = convert_list_to_linked_list([2,4,6,8,10])
        >>> head.as_list()
        [2, 4, 6, 8, 10]
        >>> head = reverse_with_temp(head)
        >>> head.as_list()
        [10, 8, 6, 4, 2]
    """

    curr, prev = head, None
    while curr is not None:
        ## temp nxt var
        nxt = curr.nxt
        ## reverse curr.next link
        curr.nxt = prev
        ## update prev & curr ptrs
        prev, curr = curr, nxt
    return prev


def main():
    head = convert_list_to_linked_list([2, 4, 6, 8, 10])
    orig_vals = head.as_list()
    print(f"{orig_vals=}")

    head = reverse(head)  # Update local head ptr
    reversed_vals = head.as_list()
    print(f"{reversed_vals=}")


main()
