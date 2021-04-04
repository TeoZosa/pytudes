"""https://www.educative.io/courses/grokking-the-coding-interview/RMlGwgpoKKY

"""

from typing import Optional


class TreeNode:
    def __init__(
        self, val: int, left: "TreeNodeType" = None, right: "TreeNodeType" = None
    ):
        self.val = val
        self.left = left
        self.right = right


TreeNodeType = Optional[TreeNode]


def has_path(root: TreeNodeType, target_sum: int) -> bool:
    """DFS exploration on a binary tree to determine if there is a root-to-leaf path where the sum of node values is equal to a given target sum

    Complexity:
        Time: O(n) (visiting each node once)
        Space: O(n) (for the recursion stack in the worst case of a degenerate linked list "tree")

    Args:
        root: Binary tree root node
        target_sum: sum which we are seeking

    Returns: True if there is a root-to-leaf path whose summed values equals `target_sum`, False otherwise.

    Examples:
        >>> has_path(None,0)
        False
        >>> root = TreeNode(12)
        >>> root.left = TreeNode(7)
        >>> root.right = TreeNode(1)
        >>> root.left.left = TreeNode(9)
        >>> root.right.left = TreeNode(10)
        >>> root.right.right = TreeNode(5)
        >>> has_path(root,23)
        True
        >>> has_path(root,16)
        False
    """
    ## EDGE CASES ##

    """ALGORITHM"""
    is_a_leaf = lambda node: node.left is None and node.right is None

    ## BASE CASE(s) ##
    if root is None:
        return False
    elif root.val == target_sum and is_a_leaf(root):
        return True

    ## DFS: RECURSIVE CASE ##
    remaining_sum = target_sum - root.val
    return has_path(root.left, remaining_sum) or has_path(root.right, remaining_sum)
