"""https://www.educative.io/courses/grokking-the-coding-interview/qVANqMonoB2"""

from leetcode.utils.linked_list import NodeType, convert_list_to_linked_list


def reverse_sub_list(head: NodeType, p: int, q: int) -> NodeType:
    return _reverse_sub_list(head, p, q)


def _reverse_sub_list(head: NodeType, start_pos: int, end_pos: int) -> NodeType:
    """

    Given the head of a LinkedList and two positions ‘p’ and ‘q’,
    reverse the LinkedList from position ‘p’ to ‘q’.

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
        >>> head = _reverse_sub_list(head,2,4)
        >>> head.as_list()
        [1, 4, 3, 2, 5]
        >>> head = convert_list_to_linked_list([1,2,3,4,5])
        >>> head = _reverse_sub_list(head,10,15)
        >>> head.as_list()
        [1, 2, 3, 4, 5]
    """
    ## Edge Cases ##
    if not head:  # Vacuous linked list
        return head

    if start_pos < 1:  # Not 1-indexed
        return head

    if end_pos <= start_pos:  # Invalid range
        return head

    """Algorithm"""
    ## INITIALIZE vars ##
    curr_pos = 1

    ## FIND sublist 1 & 2 ##
    curr, prev = head, None
    while curr is not None:
        if curr_pos == start_pos:  # Capture the sublist1 tail, sublist2 head
            s1_tail, s2_head = prev, curr
            break
        prev, curr = curr, curr.nxt
        curr_pos += 1
    else:  # INVALID: start_pos > list size
        return head

    ## REVERSE sublist2 (< HEAD sublist3) ##
    curr, prev = s2_head, None
    while curr is not None and start_pos <= curr_pos <= end_pos:
        curr.nxt, prev, curr = prev, curr, curr.nxt
        curr_pos += 1
    # POST-CONDITION: list size < end_pos XOR end_pos < curr_pos
    s3_head, s2_reversed_head = curr, prev
    s2_reversed_tail = s2_head  # Readable alias

    ## RE-LINK sublists ##
    s1_tail.nxt = s2_reversed_head  # LINK s1 to r_s2
    s2_reversed_tail.nxt = s3_head  # LINK r_s2 to s3

    return head


def main():
    head = convert_list_to_linked_list([1, 2, 3, 4, 5])
    orig_vals = head.as_list()
    print(f"{orig_vals=}")

    head = _reverse_sub_list(head, 2, 4)  # Update local head ptr
    reversed_vals = head.as_list()
    print(f"{reversed_vals=}")
