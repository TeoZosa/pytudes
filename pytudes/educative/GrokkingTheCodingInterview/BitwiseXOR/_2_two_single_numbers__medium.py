"""https://www.educative.io/courses/grokking-the-coding-interview/gk20xz4VwpG

"""


def find_single_numbers(nums: list[int]) -> list[int]:
    """Finds the two numbers in a non-empty array of integers where every number appears exactly twice, except for two which appear exactly once.

    Complexity:
        Time: O(n)
        Space: O(1)

    Args:
        nums: array of numbers with all but TWO elements appearing exactly twice,
        the TWO element that do not appear two times appear exactly once

    Returns: the TWO elements that appear exactly once

    Examples:
        >>> find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])
        [6, 4]
        >>> find_single_numbers([2, 1, 3, 2])
        [3, 1]
    """
    """ALGORITHM"""
    # XOR of all values in `nums`:
    num1_xor_num2 = 0
    for num in nums:
        num1_xor_num2 ^= num

    # Find the rightmost `1` (on) bit in `num1_xor_num2`
    #
    # Since num1 and num2 are different numbers
    # <=> there is at least a single bit different between `num1` and `num2`
    # <=> there is at least a single `1` (on) bit in `num1_xor_num2`
    rightmost_on_bit = 1
    while (rightmost_on_bit & num1_xor_num2) == 0:
        rightmost_on_bit <<= 1

    # Since `rightmost_on_bit` came from exactly one of `num1` or `num2`
    # => Partition numbers into sets based on whether they have an
    #    on bit in the same position as `rightmost_on_bit`.
    # => This ensures num1 and num2 land in separate partitions.
    #
    # Since all other numbers in those partitions will have duplicates,
    # => XORing elements within a partition together
    #    will yield num1 and num2, respectively.
    num1, num2 = 0, 0
    for num in nums:
        if (num & rightmost_on_bit) != 0:  # the bit is set
            # <=> either this is `num1`
            #     or some other number that cancels/will be canceled out
            #     leaving `num1 ^ 0` = `num1`
            num1 ^= num
        else:  # the bit is not set
            # <=> either this is `num2`
            #     or some other number that cancels/will be canceled out
            #     leaving `num2 ^ 0` = `num2`
            num2 ^= num

    return [num1, num2]
