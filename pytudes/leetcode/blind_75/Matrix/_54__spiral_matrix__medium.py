"""https://leetcode.com/problems/spiral-matrix/

Examples:
    >>> Solution().spiralOrder([
    ... [1,2,3],
    ... [4,5,6],
    ... [7,8,9]])
    [1, 2, 3, 6, 9, 8, 7, 4, 5]

"""


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        return spiral_order(matrix)


def spiral_order(matrix: list[list[int]]) -> list[int]:
    """Recursively concatenate first row with solution of 90º left-rotated matrix of remaining elements

    Spiral order:
        left to right, top to bottom, right to left, bottom to top
        until all nodes are visited, visiting each node at most once.

    Args:
        matrix:

    Returns: the spiral order traversal of a matrix

    Examples:
        [1,2,3],
        [4,5,6],
        [7,8,9]
        >>> spiral_order([[1,2,3],[4,5,6],[7,8,9]])
        [1, 2, 3, 6, 9, 8, 7, 4, 5]

        [1,2, 3, 4],
        [5,6, 7, 8],
        [9,10,11,12]

        [5,6, 7, 8],
        [9,10,11,12]
        >>> spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    """
    ## BASE CASE ##
    if not matrix:  # Degenerate (empty) matrix
        return []

    """ALGORITHM"""
    ## INITIALIZE VARS ##
    first_row, rest_matrix = list(matrix[0]), matrix[1:]
    # if matrix[0] is a singleton => put singleton into list,
    # else matrix[0] is a list => noop

    ## RECURSIVE CASE ##
    return first_row + spiral_order(left_rot_90(rest_matrix))


def left_rot_90(matrix: list[list[int]]) -> list[list[int]]:
    """Reversing the row-order (i.e. horizontal flip) of the matrix's transposition gives us a 90º left-rotation

    Args:
        matrix:

    Returns:

    Examples:
        [4,5,6]
        [7,8,9]
        >>> left_rot_90([[4,5,6],[7,8,9]])
        [[6, 9], [5, 8], [4, 7]]

        <=>
        [6, 9]
        [5, 8]
        [4, 7]

    """
    return transpose(matrix)[::-1]  # Note: right_rot_90 =transpose(matrix[::-1])


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """Zipping matrix rows gives us the matrix's transposition

    Since zipping groups column elements in sequential order,
    zipping is equivalent to swapping rows & columns

    Args:
        matrix:

    Returns:

    Examples:
        [1,2,3]
        [4,5,6]
        [7,8,9]
        >>> transpose([[1,2,3],[4,5,6],[7,8,9]])
        [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

        <=>
        [1,4,7]
        [2,5,8]
        [3,6,9]

        [4,5,6]
        [7,8,9]
        >>> transpose([[4,5,6],[7,8,9]])
        [[4, 7], [5, 8], [6, 9]]

        <=>
        [4, 7]
        [5, 8]
        [6, 9]

    """
    return [list(i) for i in zip(*matrix)]
