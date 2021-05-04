"""https://leetcode.com/problems/maximum-depth-of-binary-tree/

Examples:
    >>> Solution().maxDepth(None)
    0

"""

from typing import Optional

from pytudes.utils import binary_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(
#         self, val: int = 0, left: "TreeNodeType" = None, right: "TreeNodeType" = None
#     ):
#         self.val = val
#         self.left = left
#         self.right = right
#

TreeNodeType = Optional[binary_tree.TreeNode]


class Solution:
    def maxDepth(self, root: TreeNodeType) -> int:
        return max_depth(root)


def max_depth(root: TreeNodeType) -> int:
    """

    Args:
        root: TreeNode root of a binary tree

    Returns: depth of the binary tree rooted at `root`

    Examples:
        >>> max_depth(binary_tree.build_tree([3,9,20,None,None,15,7]))
        3
        >>> max_depth(binary_tree.build_tree([1,None,2]))
        2
        >>> max_depth(binary_tree.build_tree([0]))
        1
        >>> max_depth(binary_tree.build_tree([]))
        0

    """
    ## BASE CASE ##
    if not root:
        return 0

    """ALGORITHM"""
    ## RECURSIVE CASE ##
    return 1 + max(max_depth(root.left), max_depth(root.right))
