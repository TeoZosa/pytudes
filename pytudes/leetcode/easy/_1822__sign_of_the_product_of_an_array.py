"""https://leetcode.com/problems/sign-of-the-product-of-an-array/

Constraints:
    - 1 ≤ nums.length ≤ 1000
    - -100 ≤ nums[i] ≤ 100

Examples:
    >>> Solution().arraySign([0])
    0

"""


class Solution:
    def arraySign(self, nums: list[int]) -> int:
        return array_sign(nums)


def array_sign(nums: list[int]) -> int:
    """Computes the sign of the product of a given array of numbers

    Args:
        nums:

    Returns:
        1 if the product of nums is positive.
        -1 if the product of nums is negative.
        0 if the product of nums is equal to 0.

    Examples:
        >>> array_sign([-1,-2,-3,-4,3,2,1])
        1
        >>> array_sign([1,5,0,2,-3])
        0
        >>> array_sign([-1,1,-1,1,-1])
        -1

    """
    sign = 1
    for num in nums:
        if num == 0:
            return 0  # `product` will be 0 since 0 is a factor
        elif num < 0:
            sign *= -1
    else:
        return sign


def array_sign_xor(nums: list[int]) -> int:
    """Computes the sign of the product of a given array of numbers

    Args:
        nums:

    Returns:
        1 if the product of nums is positive.
        -1 if the product of nums is negative.
        0 if the product of nums is equal to 0.

    Examples:
        >>> array_sign_xor([-1,-2,-3,-4,3,2,1])
        1
        >>> array_sign_xor([1,5,0,2,-3])
        0
        >>> array_sign_xor([-1,1,-1,1,-1])
        -1

    """
    prod_sign_bit = 0
    for num in nums:
        if num == 0:
            return 0  # `product` will be 0 since 0 is a factor
        prod_sign_bit ^= get_sign_bit(num)
    else:
        return -1 if prod_sign_bit == 1 else 1


def get_sign_bit(num: int) -> int:
    """Returns the sign bit of a number (MSB of an unsigned int)

    Args:
        num:

    >>> get_sign_bit(128)
    0
    >>> get_sign_bit(-128)
    1

    """
    return -(num >> num.bit_length())
