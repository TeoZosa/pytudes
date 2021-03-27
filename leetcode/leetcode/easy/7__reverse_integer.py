"""
Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value to go outside the
    signed 32-bit integer range [-2^31, 2^31 - 1],
    then return 0.

Assume the environment does not allow you to store 64-bit integers
(signed or unsigned).
See Also:
    https://leetcode.com/problems/reverse-integer/
"""


class Solution:
    def reverse(self, x: int) -> int:
        return _reverse(x)


def _reverse(x: int) -> int:
    """

    Args:
        x: 32-bit signed integer
    Returns: x with digits reversed if it would fit in a 32-bit signed integer,
             0 otherwise
    Examples:
        >>> _reverse(123)
        321
        >>> _reverse(-123)
        -321
        >>> _reverse(120)
        21
        >>> _reverse(0)
        0
        >>> _reverse(1534236469)
        0
        >>> _reverse(7463847412)
        2147483647
        >>> _reverse(-8463847412)
        -2147483648
        >>> _reverse(8463847412)
        0
    """

    """ALGORITHM"""
    ## INITIALIZE VARS ##
    number_base, max_and_min_val_prefix = 10, 214748364
    is_negative = x < 0

    ## MIGRATE DIGITS from x_pos to reversed_x_pos
    x_pos, reversed_x_pos = abs(x), 0

    while x_pos > 0:
        digit = x_pos % number_base
        x_pos //= number_base  # Shift digits right, truncating off decimal

        # Exit early if 32-bit min/max bounds are about to be exceeded
        if (
            reversed_x_pos > max_and_min_val_prefix
            or reversed_x_pos == max_and_min_val_prefix
            and ((is_negative and digit > 8) or (not is_negative and digit > 7))
        ):
            return 0

        # Shift digits left and add new digit
        reversed_x_pos = reversed_x_pos * number_base + digit

    sign = -1 if is_negative else 1
    return sign * reversed_x_pos


def _reverse_str_to_int(x: int) -> int:
    """

    Args:
        x: 32-bit signed integer
    Returns: x with digits reversed if it would fit in a 32-bit signed integer,
             0 otherwise
    Examples:
        >>> _reverse_str_to_int(123)
        321
        >>> _reverse_str_to_int(-123)
        -321
        >>> _reverse_str_to_int(120)
        21
        >>> _reverse_str_to_int(0)
        0
        >>> _reverse_str_to_int(1534236469)
        0
    """

    """ALGORITHM"""
    ## INITIALIZE VARS ##
    sign = -1 if x < 0 else 1

    ## REVERSE positive string version and reapply the original sign
    reversed_x = sign * int(str(abs(x))[::-1])

    ## Return reversed_x if it can be represented as a 32-bit signed integer
    return reversed_x if -(2 ** 31) <= reversed_x <= (2 ** 31) - 1 else 0
