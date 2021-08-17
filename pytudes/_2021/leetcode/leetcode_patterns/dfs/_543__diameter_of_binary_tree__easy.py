"""https://leetcode.com/problems/diameter-of-binary-tree/

Constraints:
    - The number of nodes in the tree is in the range [1, 104].
    - -100 ≤ Node.val ≤ 100

Examples:
    >>> Solution().diameterOfBinaryTree(binary_tree.TreeNode())
    0

"""
# Definition for a binary tree node.
from typing import Optional

from pytudes._2021.utils import binary_tree

# # Definition for a binary tree node.
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
    def diameterOfBinaryTree(self, root: TreeNodeType) -> int:
        diameter, _ = diameter_and_depth_of_binary_tree(root)
        return diameter


def diameter_and_depth_of_binary_tree(root: TreeNodeType) -> tuple[int, int]:
    """Returns the diameter and depth of a binary tree rooted at the given node

    The diameter of a binary tree is defined as the length (number of edges)
    of the longest path between any two nodes in a tree.
    Note: the diameter may or may not pass through the root.

    Args:
        root: Binary tree root node

    Examples:
        >>> # 3 is the length of the path [4,2,1,3] or [5,2,1,3]
        >>> diameter_and_depth_of_binary_tree(binary_tree.build_tree([1,2,3,4,5]))[0]
        3
        >>> diameter_and_depth_of_binary_tree(binary_tree.build_tree([1,2]))[0]
        1

    """
    """ALGORITHM"""
    ## BASE CASE ##
    if not root:
        return 0, 0

    ## DFS
    left_diameter, left_depth = diameter_and_depth_of_binary_tree(root.left)
    right_diameter, right_depth = diameter_and_depth_of_binary_tree(root.right)

    ## LOCAL VALUES
    # Diameter: path between the deepest parts of each subtree
    # <=> length of longest path passing through root
    root_diameter = left_depth + right_depth
    depth = 1 + max(left_depth, right_depth)

    # Diameter of this subtree is the is the maximum of the:
    #   - left subtree diameter
    #   - right subtree diameter
    #   - root diameter (longest path passing through the root)
    diameter = max(left_diameter, right_diameter, root_diameter)

    return diameter, depth
