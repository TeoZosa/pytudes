# Definition for singly-linked list.
from typing import List, Optional

import icontract

# -10^4 <= lists[i][j] <= 10^4
import typeguard


@icontract.invariant(lambda self: self.val is None or -(10 ** 4) <= self.val <= 10 ** 4)
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None


ListNodeType = Optional[ListNode]


def list_node_sublist_constraints_satisfied(lists: List[ListNodeType]) -> bool:
    is_ascending_order = True
    is_legal_sublist_len = True
    is_legal_sublist_sum = True

    for sublist_listnode in lists:
        len_ctr = 0
        sublist_sum = 0
        curr = sublist_listnode
        while curr:
            len_ctr += 1
            sublist_sum += curr.val
            if curr.next:
                # lists[i] is sorted in ascending order.
                is_ascending_order = is_ascending_order and curr.val <= curr.next.val
                if not is_ascending_order:
                    return False
            curr = curr.next

        # 0 <= lists[i].length <= 500
        is_legal_sublist_len = is_legal_sublist_len and 0 <= len_ctr <= 500
        if not is_legal_sublist_len:
            return False

        # The sum of lists[i].length won't exceed 10^4.
        is_legal_sublist_sum = is_legal_sublist_sum and 0 <= sublist_sum <= 10 ** 4
        if not is_legal_sublist_sum:
            return False

    were_sublist_constraints_satisfied = (
        is_ascending_order and is_legal_sublist_len and is_legal_sublist_sum
    )
    if not were_sublist_constraints_satisfied:
        raise RuntimeError("BUG: This should be true if we got this far!")

    return True


def constraints_satisfied(lists: List[ListNodeType]) -> bool:

    # k == lists.length
    k = len(lists)

    # 0 <= k <= 10^4
    is_legal_lists_len = 0 <= k <= 10 ** 4
    if not is_legal_lists_len:
        return False

    return is_legal_lists_len and list_node_sublist_constraints_satisfied(lists)


# Original signature: def mergeKLists(self, lists: List[ListNode]) -> ListNode;
# Since ListNodes can be None, this is technically not correct
class Solution:
    default = True

    # precondition: various problem input constraints satisfied
    @icontract.require(lambda self, lists: constraints_satisfied(lists))
    # postcondition 1: returns a single ListNode
    @typeguard.typechecked
    # postcondition 2: various problem ouput constraints satisfied
    @icontract.ensure(lambda result: list_node_sublist_constraints_satisfied([result]))
    def mergeKLists(self, lists: List[ListNodeType]) -> ListNodeType:
        # base case 1: vacuous ListNode list
        if not lists:
            return None
        # base case 2: singleton ListNode list
        if len(lists) == 1:
            return lists[0]

        # recursive case: > |lists| > 1
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])

        # return final merged array
        return self.merge(l, r)

    def merge(self, *args):
        return self.merge_default(*args) if self.default else self.merge_alt(*args)

    def merge_default(self, l, r):
        merged_handle = merged = ListNode()
        while l and r:
            if l.val < r.val:
                merged.next = l
                l = l.next
            else:
                merged.next = r
                r = r.next
            merged = merged.next

        # either l or r (or both) is now None
        # => make merged.next point to the non-None ListNode
        merged.next = l or r
        return merged_handle.next

    def merge_alt(self, l, r):
        if not (l and r):
            # return the non-None ListNode, if one exists
            return l or r
        elif l.val < r.val:
            l.next = self.merge_default(l.next, r)
            return l
        else:
            r.next = self.merge_default(l, r.next)
            return r
