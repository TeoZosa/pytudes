"""https://leetcode.com/problems/number-of-1-bits/

Constraints:
    The input must be a binary string of length 32.

Follow up: If this function is called many times, how would you optimize it?
    Answer: DP table as cache (see below)

Examples:
    >>> Solution().hammingWeight(0)
    0
    >>> Solution().hammingWeight(int("00000000000000000000000010000000", 2))
    1
    >>> Solution().hammingWeight(int("00000000000000000000000000001011", 2))
    3
    >>> Solution().hammingWeight(int("11111111111111111111111111111101", 2))
    31

See Also:
    - pytudes/leetcode/medium/_338__counting_bits__medium.py

"""


class Solution:
    # Use a class variable since entries will not vary between class instances
    # and this can therefore be used as a global "cache"
    DP_table = {0: 0}

    def hammingWeight(self, n: int) -> int:
        if self.DP_table.get(n) is None:
            self.DP_table[n] = self.hammingWeight(n & (n - 1)) + 1
        return self.DP_table[n]


def compute_hamming_weight(n: int) -> int:
    """Computes the Hamming weight of an unsigned integer

    Note that in some languages, such as Java, there is no unsigned integer
    type.
    In this case, the input will be given as a signed integer type.
    It should not affect your implementation,
    as the integer's internal binary representation is the same,
    whether it is signed or unsigned.

    In Java, the compiler represents the signed integers using 2's
    complement notation.
    Therefore, in Example 3, the input represents the signed integer. -3.

    Args:
        n: unsigned integer

    Returns:the number of '1' bits `n` has (also known as the Hamming weight).

    Examples:
        >>> compute_hamming_weight(int("00000000000000000000000000001011", 2))
        3
        >>> compute_hamming_weight(int("00000000000000000000000010000000", 2))
        1
        >>> compute_hamming_weight(int("11111111111111111111111111111101", 2))
        31
    """
    hamming_weight = 0
    while n:
        hamming_weight += n & 1
        n >>= 1
    return hamming_weight
