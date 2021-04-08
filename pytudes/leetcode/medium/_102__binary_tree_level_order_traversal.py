"""https://leetcode.com/problems/binary-tree-level-order-traversal/

Examples:
    >>> Solution().levelOrder(binary_tree.build_tree([1,None,2]))
    [[1], [2]]

See Also:
    - pytudes/educative/GrokkingTheCodingInterview/TreeBFS/_1_binary_tree_level_order_traversal__easy.py

"""
from collections import deque
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
    def levelOrder(self, root: TreeNodeType) -> list[list[int]]:
        return level_order(root)


def level_order(root: TreeNodeType) -> list[list[int]]:
    """

    Args:
        root: TreeNode root of a binary tree

    Returns: node values corresponding to the level-order traversal of the binary tree rooted at `root`

    Examples:
        >>> level_order(binary_tree.build_tree([3,9,20,None,None,15,7]))
        [[3], [9, 20], [15, 7]]
        >>> level_order(binary_tree.build_tree([1,None,2]))
        [[1], [2]]
        >>> level_order(binary_tree.build_tree([1]))
        [[1]]
        >>> level_order(binary_tree.build_tree([]))
        []

    """
    ## EDGE CASES ##
    if not root:
        return []

    """ALGORITHM"""
    ## INITIALIZE VARS ##

    # DS's/res
    level_order_traversal = []
    queue = deque()

    ## BFS @ root ##
    queue.append(root)
    while len(queue) > 0:
        curr_level_traversal = []

        level_size = len(queue)
        for _ in range(level_size):
            curr_node = queue.popleft()

            ## Visit node and add children
            curr_level_traversal.append(curr_node.val)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)

        # Append current level's traversal to traversal order
        level_order_traversal.append(curr_level_traversal)

    return level_order_traversal
