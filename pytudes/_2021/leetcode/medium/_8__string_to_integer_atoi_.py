"""https://leetcode.com/problems/string-to-integer-atoi/

Constraints:
    - 0 ≤ s.length ≤ 200
    - s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

Examples:
    >>> Solution().myAtoi("   +1  ")
    1

"""
import re

INT_MIN_VAL, INT_MAX_VAL = -(2 ** 31), (2 ** 31) - 1


class Solution:
    def myAtoi(self, s: str) -> int:
        return my_atoi(s)


def my_atoi(num_str: str) -> int:
    """Returns the first number in a string as a 32-bit integer

    Args:
        num_str:
            Valid strings contain 0 or more whitespace characters at the beginning of the string
             immediately followed by a contiguous sequence of digits number,
             with an optional + or - symbol prefix .
             Only this first number is read in, if it exists.

    Examples:
        >>> my_atoi("42")
        42
        >>> my_atoi("+42")
        42
        >>> my_atoi("-42")
        -42
        >>> my_atoi("   -42")
        -42
        >>> my_atoi("4193 with words")
        4193
        >>> my_atoi("words and 987")
        0
        >>> my_atoi("")
        0
        >>> my_atoi("   ")
        0
        >>> my_atoi("-91283472332")
        -2147483648
        >>> my_atoi("91283472332")
        2147483647

    """
    # Regex explanation:
    # 1. Ignore leading whitespace
    # 2. Read in optional sign
    # 3. Read in contiguous digits, ignoring remainder of the string

    num_cap = re.search(r"^\s*([-+]?\d+)", num_str)
    num = int(num_cap.group(1)) if num_cap else 0
    return max(INT_MIN_VAL, min(num, INT_MAX_VAL))


def my_atoi_no_re(num_str: str) -> int:
    """Returns the first number in a string as a 32-bit integer

    Args:
        num_str:
            Valid strings contain 0 or more whitespace characters at the beginning of the string
             immediately followed by a contiguous sequence of digits number,
             with an optional + or - symbol prefix .
             Only this first number is read in, if it exists.

    Examples:
        >>> my_atoi_no_re("42")
        42
        >>> my_atoi_no_re("+42")
        42
        >>> my_atoi_no_re("-42")
        -42
        >>> my_atoi_no_re("4193 with words")
        4193
        >>> my_atoi_no_re("words and 987")
        0
        >>> my_atoi_no_re("")
        0
        >>> my_atoi_no_re("   ")
        0
        >>> my_atoi_no_re("-91283472332")
        -2147483648
        >>> my_atoi_no_re("91283472332")
        2147483647

    """

    num_str = num_str.lstrip()
    if not num_str:
        return 0

    signs = {"-", "+"}
    num_components = []
    if num_str[0] in signs:
        num_components.append(num_str[0])
        num_str = num_str[1:]

    for char in num_str:
        if not char.isdigit():
            break
        num_components.append(char)

    if len(num_components) > 0 and num_components[-1].isdigit():
        num = int("".join(num_components))
    else:  # no digits were read in
        num = 0

    if num < 0:
        return max(INT_MIN_VAL, num)
    else:
        return min(num, INT_MAX_VAL)
