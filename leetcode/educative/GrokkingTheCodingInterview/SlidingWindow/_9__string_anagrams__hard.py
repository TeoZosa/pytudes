"""https://www.educative.io/courses/grokking-the-coding-interview/xl2g3vxrMq3"""


def find_string_anagrams(input_str: str, pattern: str) -> list[str]:
    """Find all anagrams of a specified pattern in the given string.

    Anagram is actually a Permutation of a string.
    For example, “abc” has the following six anagrams:
        abc
        acb
        bac
        bca
        cab
        cba

    Complexity:
        N = len(input_str)
        M = len(pattern)
            Time: O(N+M)
            Space: O(N+M)
                O(M) (for HashMap if `pattern` has ALL DISTINCT CHARACTERS)
              + O(N) (for result list if M==1 & `input_str` contains ONLY that char)
    Returns:
        Anagrams of `pattern` in `input_str`.
    Examples:
        >>> find_string_anagrams("ppqp", "pq")
        ['pq', 'qp']
        >>> find_string_anagrams("abbcabc", "abc")
        ['bca', 'cab', 'abc']
        >>> find_string_anagrams("aaaa", "a")
        ['a', 'a', 'a', 'a']
    """

    def validate_input():
        for input_var, input_var_name, expected_type in [
            [input_str, "input_str", str],
            [pattern, "pattern", str],
        ]:
            if not isinstance(input_var, expected_type):
                raise ValueError(
                    f"Invalid input type for `{input_var_name}`\n"
                    f"Expected: {expected_type}\t"
                    f"Got: {type(input_var)}"
                )

    ## INPUT VALIDATION ##
    validate_input()

    ## EDGE CASES ##
    if not pattern or not input_str or len(pattern) > len(input_str):
        return []

    """ALGORITHM"""
    get_curr_win_size = lambda: window_end - window_start + 1
    ## INITIALIZE VARS ##
    window_start, num_fully_matched_chars = 0, 0

    # DS's/res
    anagrams = []
    pattern_char_count = {}
    for c in pattern:
        pattern_char_count[c] = pattern_char_count.get(c, 0) + 1

    ## SLIDING ##
    for window_end in range(len(input_str)):

        ## EXPANSION ##
        if (right_char := input_str[window_end]) in pattern_char_count:
            pattern_char_count[right_char] -= 1  # Decrement the character count
            if pattern_char_count[right_char] == 0:
                num_fully_matched_chars += 1  # Increment the matched count

        ## WINDOW MATCH ##
        if num_fully_matched_chars == len(pattern_char_count):  # Anagram!
            window_substr = input_str[window_start : window_end + 1]
            anagrams.append(window_substr)

        ## CONTRACTION ##
        if get_curr_win_size() == len(pattern):
            if (left_char := input_str[window_start]) in pattern_char_count:
                if pattern_char_count[left_char] == 0:
                    num_fully_matched_chars -= 1  # Decrement the matched count
                pattern_char_count[left_char] += 1  # Re-increment the character count
            window_start += 1

    return anagrams
