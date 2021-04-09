"""https://leetcode.com/problems/counting-bits/

Categories:
    - Dynamic Programming (DP)

Examples:
    >>> Solution().countBits(2)
    [0, 1, 1]
    >>> Solution().countBits(5)
    [0, 1, 1, 2, 1, 2]

See Also:
    - pytudes/leetcode/blind_75/Binary/_191__number_of_1_bits__easy.py

"""


class Solution:
    def countBits(self, num: int) -> list[int]:
        return count_bits(num)


def count_bits(num: int) -> list[int]:
    """Compute the number of 1's in the binary representation of every number in the range [0, num].

    Complexity:
        N = num + 1
        Time: O(n) (Since for each number we add 1 to it's companion entry in the DP table)
        Space: O(n) (to store the result DP table)

    Args:
        num: unsigned integer

    Returns: an array of the number of 1's in the binary representation of every number in the range [0, num]

    Examples:
        >>> count_bits(-1)
        []
        >>> count_bits(2)
        [0, 1, 1]
        >>> count_bits(5)
        [0, 1, 1, 2, 1, 2]

    """
    ## EDGE CASES ##
    if num < 0:
        return []

    """ALGORITHM"""

    ## INITIALIZE VARS ##
    # DS's/res
    # dp_table[i] = number of 1 bits in unsigned integer i
    dp_table = [0] + [None] * num  # BASE CASE: `dp_table[0]=0`

    ## POPULATE DP TABLE ##
    for curr_num in range(1, len(dp_table)):

        # Will always be strictly less than num
        # <=> since num is in the range [1, num]
        #     and we are going in sequential order
        # => this entry has already been computed
        curr_num_with_lowest_set_bit_dropped = curr_num & (curr_num - 1)

        # By definition, curr_num bits will be
        # 1 + the number of bits in the number corresponding to the
        # binary representation of curr_num with the lowest set bit dropped
        #
        # Note: true for any binary representation of `curr_num` with any on-bit dropped,
        # but this representation is computable in constant-time with the mask
        # and guaranteed to precede `curr_num`,
        # and hence already have a solution stored in `dp_table`
        dp_table[curr_num] = dp_table[curr_num_with_lowest_set_bit_dropped] + 1

    return dp_table


def count_bits_via_hamming_weight(num: int) -> list[int]:
    """Compute the number of 1's in the binary representation of every number in the range [0, num].

    Complexity:
        N = num + 1
        Time: O(n) (NUM_BITS_PER_INT * N since for each number we have to right-shift bits until the number is 0)
            note: NUM_BITS_PER_INT is assumed to be constant
        Space: O(n) (to store the result list)

    Args:
        num: unsigned integer

    Returns: an array of the number of 1's in the binary representation of every number in the range [0, num]

    Examples:
        >>> count_bits_via_hamming_weight(-1)
        []
        >>> count_bits_via_hamming_weight(2)
        [0, 1, 1]
        >>> count_bits_via_hamming_weight(5)
        [0, 1, 1, 2, 1, 2]

    """
    ## EDGE CASES ##
    if num < 0:
        return []

    """ALGORITHM"""
    ## INITIALIZE VARS ##
    # DS's/res
    num_bits_in_nums_in_range_0_to_num = []

    for num in range(num + 1):
        hamming_weight = 0
        while num != 0:
            hamming_weight += num & 1
            num >>= 1
        num_bits_in_nums_in_range_0_to_num.append(hamming_weight)

    return num_bits_in_nums_in_range_0_to_num
