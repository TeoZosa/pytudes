"""https://leetcode.com/problems/longest-word-in-dictionary/

Constraints:
    - 1 ≤ words.length ≤ 1000
    - 1 ≤ words[i].length ≤ 30
    - words[i] consists of lowercase English letters.

Examples:
    >>> Solution().longestWord([])
    ''

"""

from typing import Optional, Union


class TrieNode:
    """Trie Node

    Attributes:
        word:
            string word stored at node if node corresponds to the last char in
            that word
        children:
            dictionary mapping chars to children

    """

    def __init__(self, word: Optional[str] = None):
        self.word = word
        self.children: TrieDictType = {}


TrieDictType = Union[dict, dict[str, TrieNode]]


class Solution:
    def longestWord(self, words: list[str]) -> str:
        """Initializes the TrieNode object."""
        return longest_word_trie_node(words)


def longest_word_sort(words: list[str]) -> str:
    """Returns the longest word character composable from other words in input array

    Complexity:
        n = len(words), m = len(max(words))
        Time: O(nlogn) * O(m) = O((n*m)logn)
            - String comparisons are O(m) in the worst case all strings are
            the same length and must be fully compared
        Space: O(n)
            - O(n): for the timsort auxillary sort space
            - O(n): for the words set space

    Args:
        words: array of strings words representing an English Dictionary

    Returns:
        the longest word in words that can be built one character at a time by
        other words in words. If there is more than one possible answer,
        returns the longest word with the smallest lexicographical order,
        otherwise the empty string.

    Examples:
        >>> longest_word_sort(["w","wo","wor","worl","world"])
        'world'
        >>> longest_word_sort(["a","banana","app","appl","ap","apply","apple"])
        'apple'
        >>> longest_word_sort(["a","b","banana","app","appl","ap","apple","apply"])
        'apple'

    """

    """ALGORITHM"""
    words.sort()

    ## INITIALIZE VARS ##
    # DS's/res
    words_set = {""}  # The empty string is the longest proper prefix to single chars
    longest_word = ""

    for word in words:
        longest_proper_prefix = word[:-1]

        # If the longest proper prefix (all chars up to, but not including,
        # the last char) of `word` has been seen, this implies `word` is
        # buildable from prefix substrings in `words`.
        #
        # Correctness explanation:
        #   since we are iterating in sorted order,
        #   if `word` is buildable from prefix substrings in `words`,
        #   these prefix substrings are *guaranteed* to have been visited before `words`
        #   so the algorithm is, in turn, guaranteed to be correct
        if longest_proper_prefix in words_set:
            words_set.add(word)

            # since sorting lexicographically orders words,
            # this conditional branch implicitly handles the case where
            # multiple words are bigger than the current longest word and
            # have the same length since the lexicographically smaller word
            # will always be added first
            if len(word) > len(longest_word):
                longest_word = word

    return longest_word


def longest_word_trie_node(words: list[str]) -> str:
    """Returns the longest word character composable from other words in input array

    Complexity:
        n = len(words), m = len(max(words))
        Time: O(n*m)
            - O(n*m): for each word, build the subtree one char (node) at a time
            - O(n*m): DFS trie (visiting all nodes in the worst case) to find the longest word
        Space: O(n*m)
            - each word may produce distinct subtrees (i.e. no common prefix)
            => n*m nodes in the tree

    Args:
        words: array of strings words representing an English Dictionary

    Returns:
        the longest word in words that can be built one character at a time by
        other words in words. If there is more than one possible answer,
        returns the longest word with the smallest lexicographical order,
        otherwise the empty string.

    Examples:
        >>> longest_word_trie_node(["w","wo","wor","worl","world"])
        'world'
        >>> longest_word_trie_node(["a","banana","app","appl","ap","apply","apple"])
        'apple'
        >>> longest_word_trie_node(["a","b","banana","app","appl","ap","apple","apply"])
        'apple'

    """
    root_node = TrieNode(word="")  # prefixes are descendants of the empty string

    ## BUILD Trie
    for word in words:
        # Iteratively traverse/populate prefix subtree corresponding to `word`
        curr_trie_node = root_node
        for char in word:
            child_trie_node = curr_trie_node.children.setdefault(char, TrieNode())
            curr_trie_node = child_trie_node
        ## Trie word-insertion post-condition:
        # Mark node of LAST char in word as word-ending char
        # (in this case, by stored `word` at node)
        curr_trie_node.word = word

    ## SEARCH Trie for longest word
    return find_longest_word_in_trie(root_node)


def find_longest_word_in_trie(node: TrieNode) -> str:
    ## BASE CASE ##
    # Terminate search if the root node is not part of a valid prefix
    # (i.e., char belonging to root node is not the end of an inserted string;
    # no prefix `links` to children)
    if node.word is None:
        return ""

    longest_word = node.word
    for child_node in node.children.values():
        longest_child_word = find_longest_word_in_trie(child_node)
        longest_word = get_longer_word(longest_child_word, longest_word)
    return longest_word


def get_longer_word(word1: str, word2: str) -> str:
    """Returns the "longer" of word1, word2

    Complexity:
        c = min(len(word1),len(word2))
        Time: O(c)
            - Since lexicographical string comparisons are
            character-by-character
        Space: O(1)

    Args:
        word1:
        word2:

    Returns:
        the "longer" of word1, word2 if they are not of equal lengths,
        otherwise the lexicographically smaller word.

    """
    # For equal length strings, return the lexicographically smaller one
    if len(word1) == len(word2):
        return min(word1, word2)
    else:  # Otherwise return the string with the larger length
        return max(word1, word2, key=len)  # O(1) since len is O(1)


class Trie:
    """Tree data structure used to efficiently store and retrieve keys in a dataset of strings

    A trie (pronounced as "try") or prefix tree is a tree data structure used
    to efficiently store and retrieve keys in a dataset of strings.

    There are various applications of this data structure, such as autocomplete
    and spellchecker.

    Attributes:
        root: root TrieNode() of this data structure

    """

    def __init__(self):
        """Initializes the Trie object."""
        self.root = TrieNode(word="")

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.word = word  # Add word to furthest depth (bottom-most) char node

    def get_longest(self, prefix_chars: list[str]) -> str:
        longest_word = ""
        prefix_char_children = [
            self.root.children[prefix_char] for prefix_char in prefix_chars
        ]
        for child_node in prefix_char_children:
            child_longest_word = _get_longest_word_at_root(child_node)
            longest_word = get_longer_word(longest_word, child_longest_word)
        return longest_word


def _get_longest_word_at_root(node: TrieNode) -> str:
    if not node.word:
        return ""

    longest_word = node.word
    for child_node in node.children.values():
        child_longest_word = _get_longest_word_at_root(child_node)
        longest_word = get_longer_word(longest_word, child_longest_word)

    return longest_word


def get_longest_word_trie_ds(words: list[str]) -> str:
    """Returns the longest word character composable from other words in input array

    Args:
        words: array of strings words representing an English Dictionary


    Returns:
        the longest word in words that can be built one character at a time by
        other words in words. If there is more than one possible answer,
        returns the longest word with the smallest lexicographical order,
        otherwise the empty string.

    Examples:
        >>> get_longest_word_trie_ds(["w","wo","wor","worl","world"])
        'world'
        >>> get_longest_word_trie_ds(["a","banana","app","appl","ap","apply","apple"])
        'apple'
        >>> get_longest_word_trie_ds(["a","b","banana","app","appl","ap","apple","apply"])
        'apple'

    """
    trie = Trie()
    prefix_chars = []  # root chars; all longest words will start from these root chars
    for word in words:
        if len(word) == 1:
            prefix_chars.append(word)
        trie.insert(word)
    return trie.get_longest(prefix_chars)
