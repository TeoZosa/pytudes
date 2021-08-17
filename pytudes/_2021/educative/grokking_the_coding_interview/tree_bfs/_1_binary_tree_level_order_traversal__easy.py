"""https://www.educative.io/courses/grokking-the-coding-interview/xV7E64m4lnz


See Also:
    - pytudes/_2021/leetcode/blind_75/tree/_102__binary_tree_level_order_traversal__medium.py

"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(
        self, val: int, left: "TreeNodeType" = None, right: "TreeNodeType" = None
    ):
        self.val = val
        self.left = left
        self.right = right


TreeNodeType = Optional[TreeNode]


def traverse(root: TreeNodeType) -> list[list[int]]:
    """BFS exploration to yield node values from binary tree rooted at the given input node

    Complexity:
        Time: O(n) (visiting each node once)
        Space: O(n) (to store n/2 nodes when visiting the last level of a FULL binary tree)

    Args:
        root: Binary tree root node

    Returns: nested list of tree node values in level-order

    Examples:
        >>> traverse(None)
        []
        >>> root = TreeNode(12)
        >>> root.left = TreeNode(7)
        >>> root.right = TreeNode(1)
        >>> root.left.left = TreeNode(9)
        >>> root.right.left = TreeNode(10)
        >>> root.right.right = TreeNode(5)
        >>> traverse(root)
        [[12], [7, 1], [9, 10, 5]]

    """
    ## EDGE CASES ##
    if root is None:
        return []

    """ALGORITHM"""
    ## INITIALIZE VARS
    # DS's/res
    traversal_order_result = []
    queue = deque()

    ## BFS: Level-order Traversal
    queue.append(root)
    while queue:
        curr_level_vals = []

        # Visit all the nodes at the current tree level
        curr_level_size = len(queue)
        for _ in range(curr_level_size):
            current_node = queue.popleft()

            # Visit node
            curr_level_vals.append(current_node.val)

            # Enqueue current node's child nodes
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        # Append current level node vals to traversal order
        traversal_order_result.append(curr_level_vals)

    return traversal_order_result
