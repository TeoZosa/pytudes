"""https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently

Bit manipulation is the act of algorithmically manipulating bits or other pieces of data shorter than a word.

Computer programming tasks that require bit manipulation include low-level device control,
error detection and correction algorithms, data compression, encryption algorithms, and optimization.

For most other tasks, modern programming languages allow the programmer
to work directly with abstractions instead of bits that represent those abstractions.

Bit manipulation, in some cases, can obviate or reduce the need to loop over a data structure
and can give many-fold speed ups, as bit manipulations are processed in parallel,
but the code can become more difficult to write and maintain.

-----

`& (and)`

Examples:
    >>> bin(uint("1111") & uint("1111"))
    '0b1111'
    >>> bin(uint("1001") & uint("0110"))
    '0b0'

`| (or)`

Examples:
    >>> bin(uint("1111") | uint("1111"))
    '0b1111'
    >>> bin(uint("1001") | uint("0110"))
    '0b1111'

`~ (not)`

Examples:
    >>> bin(~uint("0"))
    '-0b1'
    >>> bin(~uint("1"))
    '-0b10'

`^ (xor)`

Examples:
    >>> bin(uint("0000") ^ uint("0000"))
    '0b0'
    >>> bin(uint("1111") ^ uint("1111"))
    '0b0'
    >>> bin(uint("1001") ^ uint("0110"))
    '0b1111'

`a << b (left-shift; a * 2**b)`

Examples:
    >>> uint("1110") << 4
    224
    >>> assert(uint("1110") << 4 == uint("1110") * 2**4 == uint("11100000") == 224)

`a >> b (right-shift; a // 2**b)`

Examples:
    >>> uint("11100000") >> 4
    14
    >>> assert(uint("11100000") >> 4 == uint("11100000") // 2 **4 == uint("1110") == 14)
    >>> assert(uint("1110") << 4 >> 4 == uint("1110") == 14)

See Also:
    - https://wiki.python.org/moin/BitwiseOperators

"""


def uint(bin_str: str) -> int:
    """

    Args:
        bin_str:

    Returns: `bin_str` as an insigned integer

    Examples:
        >>> uint("0001")
        1
        >>> uint("1001")
        9
        >>> uint("1110")
        14

    """
    return int(bin_str, 2)


def set_union(A: int, B: int) -> int:
    """

    Args:
        A:
        B:

    Returns:

    Examples:
        >>> bin(set_union(int("0001", 2), int("1110", 2)))
        '0b1111'
        >>> bin(set_union(int("0001", 2), int("0001", 2)))
        '0b1'

    """
    return A | B


def set_intersection(A: int, B: int) -> int:
    """

    Args:
        A:
        B:

    Returns:

    Examples:
        >>> bin(set_intersection(int("0001", 2), int("1110", 2)))
        '0b0'
        >>> bin(set_intersection(int("0001", 2), int("0001", 2)))
        '0b1'

    """
    return A & B


def set_subtraction(A: int, B: int) -> int:
    """

    Args:
        A:
        B:

    Returns:

    Examples:
        >>> bin(set_subtraction(int("1001", 2), int("0111", 2)))
        '0b1000'
        >>> bin(set_subtraction(int("0001", 2), int("0001", 2)))
        '0b0'
    """
    return A & ~B


def set_negation(A: int) -> int:
    """
    Note:

        Two's Complement binary for Negative Integers:

        Negative numbers are written with a leading one instead of a leading zero.
        So if you are using only 8 bits for your twos-complement numbers,
        then you treat patterns from "00000000" to "01111111"
        as the whole numbers from 0 to 127,
        and reserve "1xxxxxxx" for writing negative numbers.

        A negative number, -x, is written using the bit pattern for (x-1)
        with all of the bits complemented (switched from 1 to 0 or 0 to 1).
        So -1 is complement(1 - 1) = complement(0) = "11111111",
        and -10 is complement(10 - 1) = complement(9) = complement("00001001") = "11110110".

        This means that negative numbers go all the way down to -128 ("10000000").

        Of course, Python doesn't use 8-bit numbers.
        It USED to use however many bits were native to your machine,
        but since that was non-portable,
        it has recently switched to using an INFINITE number of bits.
        Thus the number -5
        is treated by bitwise operators as if it were written "...1111111111111111111011".

    <=>  when getting the integer representation of a bit negation,
         the representation maps to the 2's complement circle
    <=> `bin(~A)` is the unsigned representation of A+1
         prefixed by `-` if the negation of A is negative (i.e., A was positive)
    <=>  must mask by WORD_SIZE_BITS to get the "true" binary representation

    Args:
        A:

    Returns: the complement of A <=>
        the number you get by switching each 1 for a 0 and each 0 for a 1 == (-A - 1).



    Examples:
        >>> int("0001", 2)
        1
        >>> set_negation(int("0001", 2))
        -2
        >>> assert (~1 == ~int("0001", 2) == set_negation(int("0001", 2)) == -2)

        >>> bin(set_negation(int("0001", 2))) # -(uint binary representation) # UNDERLYING REPR IS TRUE NEGATION
        '-0b10'

        # PURELY FOR VISUALIZATION, UNDERLYING REPR IS FINE
        >>> true_repr = true_bin_repr(~int("0001", 2), num_bits=4)
        >>> bin(true_repr)
        '0b1110'
        >>> assert (int("0001", 2) == ~~int("0001", 2) == true_bin_repr( ~true_repr, num_bits=4))

        # MISC.
        >>> A = int("0001", 2)
        >>> assert set_intersection(A, set_negation(A)) == A & ~A == 0

    """
    normal_neg = ~A
    XOR_neg = A ^ all_1_bits()  # ~0
    assert normal_neg == XOR_neg == -A - 1
    return normal_neg


def true_bin_repr(A: int, num_bits=4) -> int:
    """For negative numbers, noop for positive numbers since they're already in proper form

    Args:
        A:
        num_bits:

    Returns:

    Examples:
        >>> bin(true_bin_repr(~int("0001", 2), num_bits=4))
        '0b1110'
        >>> true_bin_repr(~int("0001", 2), num_bits=4)
        14
        >>> bin(true_bin_repr(~int("0001", 2), num_bits=32))
        '0b11111111111111111111111111111110'
    """
    BIT_MASK = (1 << num_bits) - 1
    return A & BIT_MASK


def set_bit_at_pos(A: int, pos: int) -> int:
    """0-indexed, little endian

    Args:
        A:
        pos:

    Returns:

    Examples:
        >>> bin(set_bit_at_pos(int("0000", 2), pos=0))
        '0b1'
        >>> bin(set_bit_at_pos(int("0001", 2), pos=0))
        '0b1'
        >>> bin(set_bit_at_pos(int("0001", 2), pos=1))
        '0b11'
        >>> bin(set_bit_at_pos(int("0001", 2), pos=2))
        '0b101'
        >>> bin(set_bit_at_pos(int("0001", 2), pos=3))
        '0b1001'
        >>> bin(set_bit_at_pos(int("0001", 2), pos=4))
        '0b10001'

    """
    return A | 1 << pos


def clear_bit_at_pos(A: int, pos: int) -> int:
    """0-indexed, little endian

    Args:
        A:
        pos:

    Returns:

    Examples:
        >>> bin(clear_bit_at_pos(int("1111", 2), pos=0))
        '0b1110'
        >>> bin(clear_bit_at_pos(int("1110", 2), pos=0))
        '0b1110'
        >>> bin(clear_bit_at_pos(int("1110", 2), pos=1))
        '0b1100'
        >>> bin(clear_bit_at_pos(int("1110", 2), pos=2))
        '0b1010'
        >>> bin(clear_bit_at_pos(int("1110", 2), pos=3))
        '0b110'
        >>> bin(clear_bit_at_pos(int("1110", 2), pos=4))
        '0b1110'

    """
    return A & ~(1 << pos)


def test_bit_at_pos(A: int, pos: int) -> bool:
    """0-indexed, little endian

    Args:
        A:
        pos:

    Returns:

    Examples:
        >>> test_bit_at_pos(int("1001", 2), pos=0)
        True
        >>> test_bit_at_pos(int("1001", 2), pos=1)
        False
        >>> test_bit_at_pos(int("1001", 2), pos=2)
        False
        >>> test_bit_at_pos(int("1001", 2), pos=3)
        True
        >>> test_bit_at_pos(int("1001", 2), pos=4)
        False

    """
    return (A & 1 << pos) != 0


def extract_last_bit(A: int) -> int:
    """

    Args:
        A:

    Returns:

    Examples:
        >>> bin(extract_last_bit(int("1000", 2)))
        '0b1000'
        >>> bin(extract_last_bit(int("1100", 2)))
        '0b100'
        >>> bin(extract_last_bit(int("1110", 2)))
        '0b10'
        >>> bin(extract_last_bit(int("1111", 2)))
        '0b1'

    """
    mask_with_twos_complement_negation_of_A = A & -A
    mask_with_negation_of_A_minus_1 = A & ~(A - 1)
    XOR_with_A_last_on_bit_dropped = A ^ remove_last_on_bit(A)  # A ^ (A & (A - 1))
    assert (
        mask_with_twos_complement_negation_of_A
        == mask_with_negation_of_A_minus_1
        == XOR_with_A_last_on_bit_dropped
    )
    return mask_with_twos_complement_negation_of_A


def remove_last_on_bit(A: int) -> int:
    """

    Args:
        A:

    Returns:

    Examples:
        >>> bin(remove_last_on_bit(int("1000", 2)))
        '0b0'
        >>> bin(remove_last_on_bit(int("1100", 2)))
        '0b1000'
        >>> bin(remove_last_on_bit(int("1110", 2)))
        '0b1100'
        >>> bin(remove_last_on_bit(int("1111", 2)))
        '0b1110'

    """
    return A & (A - 1)


def all_1_bits() -> int:
    """

    Returns:

    Examples:
        >>> all_1_bits()
        -1
        >>> bin(all_1_bits())
        '-0b1'

    """
    return ~0
