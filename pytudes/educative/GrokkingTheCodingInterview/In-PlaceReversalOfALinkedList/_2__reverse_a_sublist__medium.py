"""https://www.educative.io/courses/grokking-the-coding-interview/qVANqMonoB2

Categories:
    - Linked List
    - Blind 75

See Also:
    - https://leetcode.com/problems/linked-list-cycle/

"""

from pytudes.utils.linked_list import NodeType, convert_list_to_linked_list


def reverse_sub_list(head: NodeType, p: int, q: int) -> NodeType:
    return _reverse_sub_list(head, p, q)


def _reverse_sub_list(head: NodeType, start_pos: int, end_pos: int) -> NodeType:
    """

    Given the head of a LinkedList and 1-indexed positions `start_pos` and
    `end_pos`, reverse the LinkedList from position `start_pos` to `end_pos`.

    Returns:
        the head of the in-place sublist-reversed LinkedList

    Examples:
        >>> head = convert_list_to_linked_list([1,2,3,4,5])
        >>> head.as_list()
        [1, 2, 3, 4, 5]
        >>> head = _reverse_sub_list(head,2,4)
        >>> head.as_list()
        [1, 4, 3, 2, 5]
        >>> head = convert_list_to_linked_list([1,2,3,4,5])
        >>> head = _reverse_sub_list(head,10,15)
        >>> head.as_list()
        [1, 2, 3, 4, 5]

    """
    ## EDGE CASES ##
    if not head:  # Vacuous linked list
        return head
    if start_pos < 1:  # Not 1-indexed
        return head
    if end_pos <= start_pos:  # Invalid range
        return head

    """Algorithm"""
    ## INITIALIZE VARS ##
    curr_pos = 1

    ## FIND sublist 1 & 2 ##
    curr, prev = head, None
    while curr is not None and curr_pos < start_pos:
        prev, curr = curr, curr.nxt
        curr_pos += 1
    s2_head, s1_tail = curr, prev

    if s2_head is None:  # No sublist to reverse <=> list size < start_pos
        return head

    ## REVERSE sublist2 ##
    curr, prev = s2_head, None
    while curr is not None and start_pos <= curr_pos <= end_pos:
        curr.nxt, prev, curr = prev, curr, curr.nxt  # reverse node
        curr_pos += 1
    # POST-CONDITION: list size < end_pos XOR end_pos < curr_pos
    s3_head, s2_reversed_head = curr, prev
    s2_reversed_tail = s2_head  # Readable alias

    ## RE-LINK sublists ##
    s1_tail.nxt = s2_reversed_head
    s2_reversed_tail.nxt = s3_head

    return head


def main():
    head = convert_list_to_linked_list([1, 2, 3, 4, 5])
    orig_vals = head.as_list()
    print(f"{orig_vals=}")

    head = _reverse_sub_list(head, 2, 4)  # Update local head ptr
    reversed_vals = head.as_list()
    print(f"{reversed_vals=}")
