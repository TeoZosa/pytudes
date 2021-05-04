"""https://leetcode.com/problems/edit-distance/

Constraints:
    - 0 ≤ word1.length, word2.length ≤ 500
    - word1 and word2 consist of lowercase English letters.

Examples:
    >>> Solution().minDistance("fat", "cat")
    1

See Also:
    - https://trekhleb.dev/blog/2018/dynamic-programming-vs-divide-and-conquer/

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return compute_edit_distance(word1, word2)


def compute_edit_distance(word1: str, word2: str) -> int:
    """Returns the Levenshtein (edit) distance between two words

    The edit distance is the minimum number of operations required to convert
    word1 to word2.

    Based on the observation that word transformation can be achieved via three
    distinct character operations:
        1. Insertion
        2. Deletion
        3. Substitution

    Args:
        word2:
        word1:

    Examples:
        >>> compute_edit_distance('','')
        0
        >>> compute_edit_distance("a",'')
        1
        >>> compute_edit_distance('',"a")
        1
        >>> compute_edit_distance("abc",'')
        3
        >>> compute_edit_distance('',"abc")
        3
        >>> compute_edit_distance("islander","slander")
        1
        >>> compute_edit_distance("mart","karma")
        3
        >>> compute_edit_distance("kitten","sitting")
        3
        >>> compute_edit_distance("ball","football")
        4
        >>> compute_edit_distance("football","foot")
        4

        >>> compute_edit_distance("horse","ros")
        3
        >>> # horse -> rorse (replace "h" with "r")
        >>> # rorse -> rose (remove "r")
        >>> # rose -> ros (remove "e")

        >>> compute_edit_distance("intention","execution")
        5
        >>> # intention -> inention (remove "t")
        >>> # inention -> enention (replace "i" with "e")
        >>> # enention -> exention (replace "n" with "x")
        >>> # exention -> exection (replace "n" with "c")
        >>> # exection -> execution (insert "u")

    """
    ## EDGE CASES ##
    # if one or both strings are empty,
    # edit distance is the length of the longer string
    if min(len(word1), len(word2)) == 0:
        return max(len(word1), len(word2))

    # Initialize word1 x word2 matrix where `edit_distance[i][j]` will contain
    # the number of operations necessary to transform `word1[:i]` to/from
    # `word2[:j]`. Matrix is 1-indexed with the empty string being the shared
    # root entry (i.e., `edit_distance[0][0] == 0`)
    num_rows, num_cols = len(word1) + 1, len(word2) + 1
    edit_distance = []
    for _ in range(num_rows):
        edit_distance.append([-1] * num_cols)

    # The first column corresponds to the edit distance between the empty string
    # and `word1` substrings (e.g., `edit_distance[len(word1)][0] == len(word1)`)
    for word1_char_num in range(num_rows):
        edit_distance[word1_char_num][0] = word1_char_num

    # The first row corresponds to the edit distance between the empty string
    # and `word2` substrings (e.g., `edit_distance[0][len(word2)] == len(word2)`)
    for word2_char_num in range(num_cols):
        edit_distance[0][word2_char_num] = word2_char_num

    # As the edit distance between two strings is is a function of the edit
    # distance between its substrings, we use tabulation to efficiently compute
    # edit distances for all substring combinations between `word1` & `word2`
    for word1_char_num in range(1, num_rows):
        for word2_char_num in range(1, num_cols):
            insertion_distance = edit_distance[word1_char_num - 1][word2_char_num] + 1
            deletion_distance = edit_distance[word1_char_num][word2_char_num - 1] + 1

            substition_distance = edit_distance[word1_char_num - 1][word2_char_num - 1]
            if word2[word2_char_num - 1] != word1[word1_char_num - 1]:
                substition_distance += 1

            edit_distance[word1_char_num][word2_char_num] = min(
                insertion_distance, deletion_distance, substition_distance
            )

    return edit_distance[len(word1)][len(word2)]
