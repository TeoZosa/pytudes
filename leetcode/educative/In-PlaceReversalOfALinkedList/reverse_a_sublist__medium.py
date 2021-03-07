"""https://www.educative.io/courses/grokking-the-coding-interview/qVANqMonoB2"""

"""Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’."""

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


def convert_list_to_linked_list(arr: list[Any]) -> NodeType:
    """
    Utility fn for easier testing
    Args:
        arr: input array of elements to convert
    Returns:
        The head of the linked list derived from arr
    Examples:
        >>> convert_list_to_linked_list([1,2,3,4,5]).as_list()
        [1, 2, 3, 4, 5]
    """
    if not arr:
        return None

    first, rest = arr[0], arr[1:]
    head = curr = Node(first)
    for val in rest:
        curr.nxt = Node(val)
        curr = curr.nxt
    return head


def reverse_sub_list(head: NodeType, p: int, q: int) -> NodeType:
    """

    Args:
        head: head of a linked list of nodes
        [1-indexed positions]
        p: start pos
        q: end pos
    Returns:
        the head of the in-place sublist-reversed linked list
    Examples:
        >>> head = convert_list_to_linked_list([1,2,3,4,5])
        >>> head.as_list()
        [1, 2, 3, 4, 5]
        >>> head = reverse_sub_list(head,2,4)
        >>> head.as_list()
        [1, 4, 3, 2, 5]
    """
    start_pos, end_pos = p, q  # Readable aliases

    ## Edge Cases ##
    if not head:  # Vacuous linked list
        return head

    if start_pos < 1:  # Not 1-indexed
        return head

    if start_pos >= end_pos:  # Invalid range
        return head

    """Algorithm"""
    ## Initialize ##

    # vars
    curr_pos = 1

    ## FIND sublists 1 & 2 ##
    # GET TAIL sublist1
    # GET HEAD sublist2
    curr, prev = head, None
    while curr is not None:
        if curr_pos == start_pos:
            ## Capture the sublist1 tail, sublist2 head
            s1_tail, s2_head = prev, curr
            break
        prev, curr = curr, curr.nxt
        curr_pos += 1
    else:  # Invalid start_pos: exceeds list size
        return head

    ## REVERSE sublist2 < HEAD sublist3 ##
    curr, prev = s2_head, None
    while curr is not None and start_pos <= curr_pos <= end_pos:
        curr.nxt, prev, curr = prev, curr, curr.nxt
        curr_pos += 1
    # Post-condition: curr_pos > end_pos XOR end_pos > list size

    ## RE-LINK sublists ##
    # GET HEAD sublist3
    s3_head = curr  # None if end_pos > list size
    # GET TAIL/HEAD REVERSED sublist2
    s2_reversed_head, s2_reversed_tail = prev, s2_head  # Readable alias
    # LINK s1 to r_s2
    s1_tail.nxt = s2_reversed_head
    # LINK r_s2 to s3
    s2_reversed_tail.nxt = s3_head
    return head


def reverse(curr: NodeType, prev: NodeType = None) -> NodeType:
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
        >>> head = reverse(head)
        >>> head.as_list()
        [10, 8, 6, 4, 2]
    """
    while curr is not None:  # if not curr: return prev
        # reverse curr.next link, update prev & curr ptrs
        curr.nxt, prev, curr = prev, curr, curr.nxt  # do reversal
    return prev


def main():
    head = convert_list_to_linked_list([1, 2, 3, 4, 5])
    orig_vals = head.as_list()
    print(f"{orig_vals=}")

    head = reverse_sub_list(head, 2, 4)  # Update local head ptr
    reversed_vals = head.as_list()
    print(f"{reversed_vals=}")
