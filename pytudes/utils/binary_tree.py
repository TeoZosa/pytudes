"""

See Also:
    - pytudes/educative/grokking_the_coding_interview/tree_bfs/_1_binary_tree_level_order_traversal__easy.py
    - pytudes/leetcode/blind_75/tree/_104__maximum_depth_of_binary_tree__easy.py

"""

from typing import Optional


class TreeNode:
    def __init__(
        self, val: int = 0, left: "TreeNodeType" = None, right: "TreeNodeType" = None
    ):
        self.val = val
        self.left = left
        self.right = right


TreeNodeType = Optional[TreeNode]


def build_tree(arr: list[int], is_1_indexed=False) -> TreeNodeType:
    """Builds a TreeNode binary tree from the values in arr

    Assumes the values in arr are ordered as a binary tree

    If `arr` is 0-indexed, internally pads `arr` to be 1-indexed for easier
    math

    Args:
        arr: 0- or 1-indexed array representation of a binary-tree
        is_1_indexed: whether or not `arr` is already in the expected
        1-indexed representation

    Returns: TreeNode root of a binary tree representing arr

    Examples:
        >>> assert (
        ...     build_tree([1,2,3], is_1_indexed=False).val ==
        ...     build_tree([None,1,2,3], is_1_indexed=True).val ==
        ...     1
        ... )
        >>> root = build_tree([None,3,9,20,None,None,15,7], is_1_indexed=True)
        >>> root.val
        3
        >>> root.left.val
        9
        >>> root.right.val
        20
        >>> root.right.left.val
        15
        >>> root.right.right.val
        7

    """
    if not is_1_indexed:
        arr = [None] + arr
    return _build_tree(arr, 1)


def _build_tree(arr: list[int], root_idx: int) -> TreeNodeType:
    """Recursively builds the tree rooted at arr[root_idx]"""
    ## BASE CASE ##
    if root_idx >= len(arr) or arr[root_idx] is None:
        return None

    """ALGORITHM"""
    ## RECURSIVE CASE ##
    root = TreeNode(arr[root_idx])
    root.left = _build_tree(arr, root_idx * 2)
    root.right = _build_tree(arr, root_idx * 2 + 1)
    return root


def get_parent_idx(index: int) -> int:
    """

    Args:
        index: index of the binary tree element in an array representation

    Returns: the parent index of the binary tree element

    Examples:
        >>> arr = [None,3,9,20,None,None,15,7]
        >>> arr[get_parent_idx(2)] # 20
        3
        >>> arr[get_parent_idx(len(arr)-1)] # 7
        20

    """
    return index // 2


def get_child_idx_left(index: int) -> int:
    """

    Args:
        index: index of the binary tree element in an array representation

    Returns: the left-child index of the binary tree element

    Examples:
        >>> arr = [None,3,9,20,None,None,15,7]
        >>> arr[get_child_idx_left(1)] # 3
        9
        >>> arr[get_child_idx_left(3)] # 20
        15

    """
    return index * 2


def get_child_idx_right(index: int) -> int:
    """

    Args:
        index: index of the binary tree element in an array representation

    Returns: the right-child index of the binary tree element

    Examples:
        >>> arr = [None,3,9,20,None,None,15,7]
        >>> arr[get_child_idx_right(1)] # 3
        20
        >>> arr[get_child_idx_right(3)] # 20
        7

    """
    return (index * 2) + 1
