"""https://www.educative.io/courses/grokking-the-coding-interview/JPnp17NYXE9

    Categories:
        Binary
        Bit Manipulation
        Blind 75

    See Also:
        pytudes/educative/GrokkingTheCodingInterview/BitwiseXOR/_0__find_missing_number__easy.py
        pytudes/leetcode/easy/_268__missing_number.py

"""


def find_missing_number(nums: list[int]) -> int:
    """
    Args:
        nums: array containing n distinct numbers
              taken from the range [0,n]
              (n+1 possible numbers)
    Complexity:
        N = len(nums)
            Time: O(N) (iterate the entire array)
            Space: O(1) (in-place computations)
    Returns: the missing number in the range [0,n]
    Examples:
        >>> find_missing_number([])
        0
        >>> find_missing_number([0])
        1
        >>> find_missing_number([1])
        0
        >>> find_missing_number([4, 0, 3, 1])
        2
        >>> find_missing_number([8, 3, 5, 2, 4, 6, 0, 1])
        7
    """
    """ALGORITHM"""

    def swap_elements(i, j):
        nums[i], nums[j] = nums[j], nums[i]

    ## INITIALIZE VARS ##
    curr_idx, n = 0, len(nums)

    ## CYCLIC SORT ## O(n)
    while curr_idx < n:
        target_idx = nums[curr_idx]
        if curr_idx != target_idx and target_idx < n:
            swap_elements(curr_idx, target_idx)
        else:
            curr_idx += 1

    ## FIND item ## O(n)
    for curr_idx in range(n):
        target_idx = nums[curr_idx]
        if curr_idx != target_idx:
            return curr_idx
    else:
        return n


def find_missing_number_via_closed_form_equation(nums: list[int]) -> int:
    """
    https://en.wikipedia.org/wiki/Triangular_number
       n          n
      ___        ___
      ╲         ╲        n(n+1)    (n+1
      ╱    i =  ╱    i = ------ =    2 ) = "n plus 1 choose 2"
      ‾‾‾        ‾‾‾         2
     i = 0      i = 1
    Args:
        nums: array containing n distinct numbers
              taken from the range [0,n]
              (n+1 possible numbers)
    Complexity:
        N = len(nums)
            Time: O(N) (iterate the entire array)
            Space: O(1) (in-place computations)
    Returns: the missing number in the range [0,n]
    Examples:
        >>> find_missing_number_via_closed_form_equation([])
        0
        >>> find_missing_number_via_closed_form_equation([0])
        1
        >>> find_missing_number_via_closed_form_equation([1])
        0
        >>> find_missing_number_via_closed_form_equation([4, 0, 3, 1])
        2
        >>> find_missing_number_via_closed_form_equation([8, 3, 5, 2, 4, 6, 0, 1])
        7
    """
    """ALGORITHM"""
    ## INITIALIZE VARS ##
    n = len(nums)

    sum_of_i_for_0_to_n_formula = (n * (n + 1)) // 2
    return sum_of_i_for_0_to_n_formula - sum(nums)


def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()
