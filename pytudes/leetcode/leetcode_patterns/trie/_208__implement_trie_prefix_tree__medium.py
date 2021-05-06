"""https://leetcode.com/problems/implement-trie-prefix-tree/

Constraints:
    - 1 ≤ word.length, prefix.length ≤ 2000
    - word and prefix consist only of lowercase English letters.
    - At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

Examples"
    >>> trie = Trie()
    >>> trie.startsWith("app")
    False
    >>> trie.insert("apple")
    >>> trie.search("apple")
    True
    >>> trie.startsWith("app")
    True
    >>> trie.search("app")
    False
    >>> trie.insert("app")
    >>> trie.search("app")
    True

"""
from typing import Optional


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
        """Initializes the TrieNode object."""
        self.word = word  # alternatively: is_end = False
        self.children = {}


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
        self.root = TrieNode(word="")  # Root node word is the empty string

    def insert(self, word: str) -> None:
        """Inserts the given word into the trie

        Args:
            word:

        """
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.word = word  # cache word at end-node # note: could also build after coming back from nodes with is_end == True

    def search(self, word: str) -> bool:
        """Returns True if word is in the trie, False otherwise.

        Args:
            word:

        """
        last_char_node = self.get_tail_node(word)
        was_word_found = last_char_node is not None and last_char_node.word is not None
        return was_word_found

    def startsWith(self, prefix: str) -> bool:
        """Returns True if there is any word in the trie that starts with the given prefix, otherwise False

        Args:
            prefix:

        """
        return self.get_tail_node(prefix) is not None

    def get_tail_node(self, string: str) -> Optional[TrieNode]:
        """Returns the node corresponding to the final char in a given string, if one exists

        Args:
            string:

        """
        node = self.root
        for char in string:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        else:
            return node
