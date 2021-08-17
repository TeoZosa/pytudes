"""https://coderbyte.com/information/Tree%20Constructor%20Two

Description:
    - For this challenge you will determine if an array of integer pairs can
      form a binary tree properly.

Array Challenge:
Have the function ArrayChallenge(strArr) take the array of strings stored in strArr,
which will contain pairs of integers in the following format: (i1,i2), where i1
represents a child node in a tree and the second integer i2 signifies that it is the
parent of i1.

For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"], then this forms the following
tree:

which you can see forms a proper binary tree. Your program should, in this case, return
the string true because a valid binary tree can be formed. If a proper binary tree
cannot be formed with the integer pairs, then return the string false. All of the
integers within the tree will be unique, which means there can only be one node in the
tree with the given integer value.
"""
import ast


def ArrayChallenge(strArr: list[str]) -> str:
    """Determines whether the given input represents a proper binary tree

    A proper binary tree is a graph where:
      1. All nodes have ≤ 2 children
      2. All nodes other than root node have 1 and only 1 parent node
      3. The graph (if not empty) has 1 and only 1 root node

    Args:
      strArr:
        A list of (child, parent) tuples in string representation that
        form a graph.

    Returns:
      "true" if the graph formed from the entries in strArr is a proper
      binary tree, otherwise "false".

    Examples:
      >>> ArrayChallenge(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"])
      'true'
      >>> ArrayChallenge(["(1,2)", "(2,4)", "(7,2)"])
      'true'
      >>> ArrayChallenge(["(1,2)", "(1,2)"]) # Duplicate tuples are ignored
      'true'
      >>> ArrayChallenge([]) # Vacuous binary tree
      'true'
      >>> ArrayChallenge(["(1,2)", "(1,3)"]) # 1 has >1 parent
      'false'
      >>> ArrayChallenge(["(1,2)", "(2,4)", "(7,2)", "(8,8)"]) # 8 has a Self-edge
      'false'
      >>> ArrayChallenge(["(1,2)", "(4,2)", "(7,2)"]) # 2 has >2 children
      'false'
      >>> ArrayChallenge(["(1,2)", "(4,2)", "(7,9)"]) # Graph has >1 root node
      'false'

    """
    # Edge Case
    if not strArr:  # Vacuous binary tree
        return "true"

    strArr = set(strArr)  # Remove duplicate tuples

    nodes = set()
    child_nodes, parent_node = {}, {}
    for child_parent_tuple_str in strArr:
        child, parent = ast.literal_eval(child_parent_tuple_str)

        if child == parent:  # Explicit self-edges not allowed
            return "false"

        # Assign child to parent and check if we still have a proper binary tree.
        child_nodes.setdefault(parent, []).append(child)
        if len(child_nodes[parent]) > 2:  # Parent has too many children (>2)
            return "false"

        # Assign parent to child after checking that doing so would yield a proper
        # binary tree.
        if child in parent_node:  # Child has too many parents (>1)
            return "false"
        parent_node[child] = parent

        # Add nodes to graph
        nodes.update([child, parent])

    if len(nodes) - len(parent_node) != 1:  # Tree does not have exactly one root
        return "false"

    return "true"


# # keep this function call here
# print(ArrayChallenge(input()))
