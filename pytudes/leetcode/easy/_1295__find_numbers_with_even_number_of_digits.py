"""https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

Examples:
    >>> Solution().findNumbers([])
    0

"""


class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        return find_num_even_digit_numbers_via_str_len(nums)


def find_num_even_digit_numbers_via_str_len(nums: list[int]) -> int:
    """

    Args:
        nums:

    Returns:

    Examples:
        >>> find_num_even_digit_numbers_via_str_len([12,345,2,6,7896])
        2
        >>> find_num_even_digit_numbers_via_str_len([555,901,482,1771])
        1

    """
    return len([num for num in nums if len(str(num)) % 2 == 0])


def find_num_even_digit_numbers_via_repeated_division(nums: list[int]) -> int:
    """

    Args:
        nums:

    Returns:

    Examples:
        >>> find_num_even_digit_numbers_via_repeated_division([12,345,2,6,7896])
        2
        >>> find_num_even_digit_numbers_via_repeated_division([555,901,482,1771])
        1

    """
    num_even_digit_numbers = 0

    for num in nums:
        num_digits = 1
        num = abs(num)
        while (num := num // 10) > 0:
            num_digits += 1
        if num_digits % 2 == 0:
            num_even_digit_numbers += 1
    return num_even_digit_numbers
