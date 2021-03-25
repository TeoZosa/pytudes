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
        return _reverse_str_to_int(x)


def _reverse_str_to_int(x: int) -> int:
    """

    Args:
        x: 32-bit signed integer
    Returns: x with digits reversed if result could be represented by 32 bits,
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
    sign = 1 if x >= 0 else -1

    ## REVERSE positive string version and reapply the original sign
    reversed_x = sign * int(str(abs(x))[::-1])

    ## Return reversed_x if it can be represented as a 32-bit signed integer
    return reversed_x if -(2 ** 31) <= reversed_x <= (2 ** 31) - 1 else 0


def _reverse(x: int) -> int:
    """

    Args:
        x: 32-bit signed integer
    Returns: x with digits reversed if result could be represented by 32 bits,
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
    """

    """ALGORITHM"""
    ## INITIALIZE VARS ##
    base, sign = 10, 1 if x >= 0 else -1

    ## MIGRATE DIGITS from x_pos to reversed_x_pos
    x_pos, reversed_x_pos = abs(x), 0

    while x_pos > 0:
        # Pretend environment can only store 32 bit integers =>
        # exit loop early if we are about to overflow the result integer
        if len(bin(sign * reversed_x_pos)) == 32:
            reversed_x_pos = 0
            break

        # Shift digits left and add new digit
        reversed_x_pos = reversed_x_pos * base + x_pos % base
        x_pos //= base  # Shift digits right, truncating off decimal

    return sign * reversed_x_pos
