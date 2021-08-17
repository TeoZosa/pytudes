"""https://www.educative.io/courses/grokking-the-coding-interview/3wENz1N4WW9

Categories:
    - Linked List
    - Blind 75

See Also:
   - pytudes/leetcode/blind_75/linked_list/_2106__reverse_linked_list__easy.py

"""

from pytudes._2021.utils.linked_list import NodeType, convert_list_to_linked_list


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
        curr.next, prev, curr = prev, curr, curr.next  # do reversal
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
    curr.next, prev, curr = prev, curr, curr.next  # do reversal at curr node
    return reverse_recursive(curr, prev)


def reverse_iterative_with_temp(head: NodeType) -> NodeType:
    """

    Args:
        head: head of a linked list of nodes

    Returns:
        the head of the in-place-reversed linked list (i.e. original tail)

    Examples:
        >>> head = convert_list_to_linked_list([2,4,6,8,10])
        >>> head.as_list()
        [2, 4, 6, 8, 10]
        >>> head = reverse_iterative_with_temp(head)
        >>> head.as_list()
        [10, 8, 6, 4, 2]

    """

    curr, prev = head, None
    while curr is not None:
        ## temp next var
        nxt = curr.next
        ## reverse curr.next link
        curr.next = prev
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
