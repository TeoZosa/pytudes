"""https://leetcode.com/problems/missing-number/

Categories:
    - Binary
    - Bit Manipulation
    - Blind 75

Examples:
    >>> Solution().missingNumber([])
    0

See Also:
    - pytudes/educative/GrokkingTheCodingInterview/BitwiseXOR/_0__find_missing_number__easy.py
    - pytudes/educative/GrokkingTheCodingInterview/CyclicSort/_1__find_the_missing_number__easy.py

"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return missing_number_xor(nums)


def missing_number_xor(nums: list[int]) -> int:
    """

    Complexity:
        Time: O(n)
        Space: O(1)

    Args:
        nums: array containing n distinct numbers
              taken from the range [0,n]
              (n+1 possible numbers)

    Returns: the single missing number in the range [0,n] missing from `arr`

    Examples:
        >>> missing_number_xor([])
        0
        >>> missing_number_xor([0])
        1
        >>> missing_number_xor([3,0,1])
        2
        >>> missing_number_xor([0,1])
        2
        >>> missing_number_xor([9,6,4,2,3,5,7,0,1])
        8

    """
    """ALGORITHM"""
    ## INITIALIZE VARS ##
    n = len(nums)

    # XOR of all values from 1 to n
    xor_of_1_to_n = 0
    for i in range(n + 1):  # REDUCE
        xor_of_1_to_n ^= i

    # XOR of all values in arr
    xor_of_arr_vals = 0
    for num in nums:  # REDUCE
        xor_of_arr_vals ^= num

    # missing number is the xor of `xor_of_1_to_n` and `xor_of_arr_vals`
    return xor_of_arr_vals ^ xor_of_1_to_n
