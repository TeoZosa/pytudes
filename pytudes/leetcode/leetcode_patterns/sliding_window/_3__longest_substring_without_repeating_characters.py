"""https://leetcode.com/problems/longest-substring-without-repeating-characters/

Constraints:
    - 0 ≤ s.length ≤ 5 * 10^4
    - s consists of English letters, digits, symbols and spaces.

Examples:
      >>> Solution().lengthOfLongestSubstring("")
      0

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return length_of_longest_substring(s)


def length_of_longest_substring(s: str) -> int:
    """Returns the length of the longest substring without repeating characters.

    Args:
        s: A string of alphanumeric characters, symbols, or whitespace.

    Examples:
        >>> length_of_longest_substring("abcabcbb") # "abc"
        3
        >>> length_of_longest_substring("bbbbb") # "b"
        1
        >>> length_of_longest_substring("pwwkew") # "wke"
        3
        >>> # Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
        >>> length_of_longest_substring("") # ""
        0
        >>> length_of_longest_substring("abcba") # "abc" "cba"
        3
        >>> length_of_longest_substring("abccba") # "abc" "cba"
        3

    """
    """ALGORITHM"""
    ## INITIALIZE VARS ##
    # DS's/res
    last_idx_of_char = {}
    longest_len = 0

    ## EXPANSION
    start_idx = 0
    for end_idx, new_char in enumerate(s):

        # HANDLE WINDOW MATCH
        # Current substring has no repeating characters

        # if new_char not in last_idx_of_char or not (start_idx <= last_idx_of_char[new_char] <= end_idx):
        if new_char not in last_idx_of_char or last_idx_of_char[new_char] < start_idx:
            curr_subtr_len = end_idx - start_idx + 1
            longest_len = max(longest_len, curr_subtr_len)
        else:
            ## CONTRACTION
            # shrink this window by excluding everything up to, and including,
            # last occurrence of current char (since we are now including the
            # same char, but at this position)
            start_idx = last_idx_of_char[new_char] + 1

        last_idx_of_char[new_char] = end_idx

    return longest_len
