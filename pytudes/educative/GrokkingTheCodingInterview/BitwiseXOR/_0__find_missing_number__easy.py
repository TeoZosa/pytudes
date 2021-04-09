"""https://www.educative.io/courses/grokking-the-coding-interview/RLPGq6Vx0YY

Categories:
    - Binary
    - Bit Manipulation
    - Blind 75

See Also:
    - pytudes/educative/GrokkingTheCodingInterview/CyclicSort/_1__find_the_missing_number__easy.py
    - pytudes/leetcode/blind_75/Binary/_268__missing_number__easy.py

"""


def find_missing_number(arr: list[int]) -> int:
    """

    Complexity:
        Time: O(n)
        Space: O(1)

    Args:
        arr: array containing n-1 distinct numbers
              taken from the range [1,n]
              (n possible numbers)

    Returns: the single missing number in the range [1,n] missing from `arr`

    Examples:
        >>> find_missing_number([8,6,4,2,3,5,7,1])
        9

    """
    """ALGORITHM"""
    ## INITIALIZE VARS ##
    n = len(arr) + 1

    # XOR of all values from 1 to n
    xor_of_1_to_n = 0
    for i in range(n + 1):  # REDUCE
        xor_of_1_to_n ^= i

    # XOR of all values in arr
    xor_of_arr_vals = 0
    for num in arr:  # REDUCE
        xor_of_arr_vals ^= num

    # missing number is the xor of `xor_of_1_to_n` and `xor_of_arr_vals`
    return xor_of_arr_vals ^ xor_of_1_to_n


def find_missing_number_code_golf(arr: list[int]) -> int:
    """

    Since XOR is commutative and associative,
    use a single variable to reduce XORs


    Complexity:
        Time: O(n)
        Space: O(1)

    Returns:

    Examples:
        >>> find_missing_number_code_golf([1, 5, 2, 6, 4])
        3

    """
    """ALGORITHM"""
    ## INITIALIZE VARS ##
    n = len(arr) + 1

    # XOR of all values from n to 1 & nums in arr
    missing_number = n
    # REDUCE (n-1 iterations)
    for i, num in enumerate(arr):
        missing_number ^= (i + 1) ^ num
    return missing_number
