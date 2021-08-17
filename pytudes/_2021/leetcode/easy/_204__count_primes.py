"""https://leetcode.com/problems/count-primes/

Examples:
    >>> Solution().countPrimes(0)
    0

"""


class Solution:
    def countPrimes(self, n: int) -> int:
        return count_primes(n)


def count_primes(n: int) -> int:
    """Returns the number of primes between [2, n)

    Complexity:
        Time: O(nlog(logn))
        Space: (n) (for the boolean array)
            - This becomes the bottleneck for large values of n (e.g., ≥ 10^9).
            In those cases, a segmented sieve algorithm (either Eratosthenes
            or Sorenson) or incremental sieve would be more appropriate.

            See Also:
                - https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Segmented_sieve


    Args:
        n: the limit to which we are to count primes

    Examples:
        >>> count_primes(7)
        3
        >>> count_primes(10)
        4
        >>> count_primes(0)
        0
        >>> count_primes(1)
        0

    """
    ## EDGE CASES ##
    if n <= 2:
        return 0

    """ALGORITHM"""
    ## INITIALIZE VARS
    # DS's/res

    is_prime = [True] * n  # Primality table for the integers from [0,n-1]

    # 0 & 1 are edge cases which cannot be computed with the algorithm
    # and so are manually initialized in advance

    is_prime[0] = is_prime[1] = False

    ## SIEVE OF ERATOSTHENES ##
    # since multiple_of_num filtering filters numbers in the range
    # [num^2, n), we only need to check numbers in the range [2, √n]
    # (since (√n)^2 = n ≤ n), so we terminate the outer loop when num > √n

    for num in range(2, int(n ** 0.5) + 1):
        if is_prime[num]:
            # Mark all multiples of `num` as non-prime,
            # starting from num^2 (since the other multiples of `num`
            # will have already been marked as non-prime in previous iterations)

            step_size = 2 * num if num > 2 else num  # minor optimization
            for multiple_of_num in range(num ** 2, n, step_size):
                is_prime[multiple_of_num] = False

    primes = [i for i in range(len(is_prime)) if is_prime[i]]

    return len(primes)


def count_primes_separate_loop_for_2(n: int) -> int:
    """Returns the number of primes between [2, n)

    Complexity:
        Time: O(nlog(logn))
        Space: (n) (for the boolean array)
            - This becomes the bottleneck for large values of n (e.g., ≥ 10^9).
            In those cases, a segmented sieve algorithm (either Eratosthenes
            or Sorenson) or incremental sieve would be more appropriate.

            See Also:
                - https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Segmented_sieve


    Args:
        n: the limit to which we are to count primes

    Examples:
        >>> count_primes_separate_loop_for_2(7)
        3
        >>> count_primes_separate_loop_for_2(10)
        4
        >>> count_primes_separate_loop_for_2(0)
        0
        >>> count_primes_separate_loop_for_2(1)
        0

    """
    ## EDGE CASES ##
    if n <= 2:
        return 0

    """ALGORITHM"""
    ## INITIALIZE VARS
    # DS's/res

    is_prime = [True] * n  # Primality table for the integers from [0,n-1]

    # 0 & 1 are edge cases which are known in advance
    # as they cannot be computed with the algorithm

    is_prime[0] = is_prime[1] = False

    ## SIEVE OF ERATOSTHENES ##

    # minor optimization:
    #   sieve for num==2 has step size == num
    #   sieve for num>2 has step size == 2 * num

    for multiple_of_num in range(2 ** 2, n, 2):
        is_prime[multiple_of_num] = False

    for num in range(3, int(n ** 0.5) + 1):
        if is_prime[num]:

            for multiple_of_num in range(num ** 2, len(is_prime), 2 * num):
                is_prime[multiple_of_num] = False

    return sum(is_prime)
