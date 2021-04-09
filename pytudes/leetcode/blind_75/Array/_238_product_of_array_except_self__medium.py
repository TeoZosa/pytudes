"""https://leetcode.com/problems/product-of-array-except-self/

Examples:
    >>> Solution().productExceptSelf([])
    []

"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        return product_except_self(nums)


def product_except_self(nums: list[int]) -> list[int]:
    """Computes the product of all the elements of given array at each index excluding the value at that index.

    Note: could also take math.prod(nums) and divide out the num at each index,
    but corner cases of num_zeros > 1 and num_zeros == 1 make code inelegant.

    Args:
        nums:

    Returns:

    Examples:
        >>> product_except_self([])
        []
        >>> product_except_self([1,2,3,4])
        [24, 12, 8, 6]
        >>> product_except_self([-1,1,0,-3,3])
        [0, 0, 9, 0, 0]

    """

    """ALGORITHM"""
    ## INITIALIZE VARS ##
    nums_sz = len(nums)

    # DS's/res
    nums_products_except_i = [1] * nums_sz

    ## Multiply against product of all elements PRECEDING i
    total_product = 1
    for i in range(nums_sz):
        nums_products_except_i[i] *= total_product
        total_product *= nums[i]

    ## Multiply against product of all elements FOLLOWING i
    total_product = 1
    for i in reversed(range(nums_sz)):
        nums_products_except_i[i] *= total_product
        total_product *= nums[i]

    return nums_products_except_i
