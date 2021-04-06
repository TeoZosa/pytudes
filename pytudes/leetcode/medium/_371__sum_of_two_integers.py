"""https://leetcode.com/problems/sum-of-two-integers/

    Examples:
        >>> Solution().getSum(1,1)
        2

    Categories:
        Binary
        Bit Manipulation
        Blind 75

"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        return get_sum(a, b)


def get_sum(num1: int, num2: int) -> int:
    """Sum of two input numbers without using + or - operators

    Note: in 2's complement arithmetic,
      summation rules work the same for positive and negative numbers
      <=> num1 - num2 is `get_sum(num1, -num2)`

    Returns: sum of input integers

    Examples:
        >>> get_sum(1,2)
        3
        >>> get_sum(2,3)
        5
        >>> get_sum(-12,-8)
        -20

    """

    _32_BIT_MASK = 0xFFFFFFFF  # (1 << NUM_BITS)-1

    ## RIPPLE CARRY ADDER (*in uint-space*)
    res, carry = num1, num2
    while carry != 0:  # bitwise add carry bits and get new carry bits
        res, carry = (
            add_carry_bits(res, carry, MASK=_32_BIT_MASK),
            get_new_carry_bits(res, carry, MASK=_32_BIT_MASK),
        )

    ## Handle binary strings which fall into the 2's complement negative range
    MAX_INT = 0x7FFFFFFF  # (1 << NUM_BITS - 1) - 1
    if res > MAX_INT:  # Map res from uint-space to 2's complement-space
        # flips bits; Note: repr now in 2's complement positive range
        res_flipped_bits = res ^ _32_BIT_MASK

        # bitwise negation: flip all the bits again, but in 2's complement-space (i.e. accounting for sign bit)
        res = ~res_flipped_bits
        # Note: *in uint-space* (i.e., if we inspected `bin(~res_flipped_bits)`): adds one AND *prepends* a sign bit

    return res


def get_new_carry_bits(res, carry, MASK=0xFFFFFFFF):
    """Get carry bits that would be produced by an add operation at each position
    01 + 01 = 10 <=> carry = 10 <=> carry 01 to next position
    01 + 00 = 01 <=> carry = 00 <=> no carry
    Examples:
        >>> res, carry = int("0101", 2), int("0011", 2)
        >>> bin(get_new_carry_bits(res, carry))
        '0b10'
    """
    # if there were 1s at the same position in both operands,
    # carry that one over to the next position
    return ((res & carry) << 1) & MASK


def add_carry_bits(res, carry, MASK=0xFFFFFFFF):
    """Adds bits at each position
    1 + 1 = 0
    1 + 0 = 1
    Examples:
        >>> res, carry = int("0101", 2), int("0011", 2)
        >>> bin(add_carry_bits(res, carry))
        '0b110'
    """
    return (res ^ carry) & MASK
