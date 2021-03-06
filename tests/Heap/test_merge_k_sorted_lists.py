import pytest

from leetcode.leetcode.hard.Heap import ListNode, Solution

test_cases = [
    ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
    ([], []),
    ([[]], []),
]


def convert_to_listnode(sublist: list[int]) -> ListNode:
    """
    >>> for sublist in test_cases[0][0]: assert convert_to_listnode(sublist)
    """
    head_handle = prev = ListNode()
    for val in sublist:
        curr = ListNode(val)
        prev.next = curr
        prev = curr
    return head_handle.next


def convert_nested_lists_to_listnodes(lists: list[list[int]]) -> list[ListNode]:
    """
    >>> for test_case in test_cases: assert convert_nested_lists_to_listnodes(test_case[0]) is not None
    """
    return [convert_to_listnode(sublist) for sublist in lists]


class TestSolution:
    @staticmethod
    def _test_merge_klists(
        test_case: list[list[int]], expected: list[int], solution: Solution
    ):
        actual = solution.mergeKLists(convert_nested_lists_to_listnodes(test_case))
        expected = convert_to_listnode(expected)
        while actual is not None:
            assert actual.val == expected.val
            actual = actual.next
            expected = expected.next
        assert expected is None

    @staticmethod
    @pytest.mark.parametrize("test_case, expected", test_cases)
    def test_merge_klists_default(test_case: list[list[int]], expected: list[int]):
        solution = Solution()
        solution.default = True
        TestSolution._test_merge_klists(test_case, expected, solution)

    @staticmethod
    @pytest.mark.parametrize("test_case, expected", test_cases)
    def test_merge_klists_non_default(test_case: list[list[int]], expected: list[int]):
        solution = Solution()
        solution.default = False
        TestSolution._test_merge_klists(test_case, expected, solution)
