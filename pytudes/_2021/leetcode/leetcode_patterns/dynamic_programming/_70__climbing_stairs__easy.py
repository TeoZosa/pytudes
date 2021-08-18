"""https://leetcode.com/problems/climbing-stairs/

Constraints:
    - 1 ≤ n ≤ 45

Examples:
    >>> Solution().climbStairs(-1)
    0

"""
import functools


class Solution:
    """Class-encapsulated functions

    Complexity:
        n = number of stairs to climb
        Time: O(n)
        Space: O(n)
            Note: since `memo` isn't ephemeral, it will be a *consistent* usage of
            space as opposed to being marked for de-allocation after runs
            if created as local variables in the driver functions, though in
            practice probably less since those stick around between garbage
            collection runs


    Attributes:
        memo:
            class-variable dict used as a global "cache" since entries do not
            vary between class instances. Since results will persist across
            class instantiants, using a dict (as opposed to a list) offers
            flexibility for variable values of n.

    Examples:
        >>> Solution().climbStairs(2)
        2
        >>> # There are two ways to climb to the top.
        >>> # 1. 1 step + 1 step
        >>> # 2. 2 steps
        >>> Solution().climbStairs(3)
        3
        >>> # There are three ways to climb to the top.
        >>> # 1. 1 step + 1 step + 1 step
        >>> # 2. 1 step + 2 steps
        >>> # 3. 2 steps + 1 step
        >>> Solution().climbStairs(10)
        89

    """

    _base_cases_memo = {i: i for i in range(3)}  # base case for [0,2]
    memo = _base_cases_memo.copy()

    @classmethod
    def _clear_cache(cls):
        cls.memo = cls._base_cases_memo.copy()

    def climbStairs(self, n: int) -> int:
        """Alias to `climb_stairs_memoize`"""
        return self.climb_stairs_memoize(n)

    def climb_stairs_memoize(self, n: int) -> int:
        """Returns the number of distinct paths which climb n stairs

        Context: you are climbing a staircase with n steps. Each time you can
        either climb 1 or 2 steps.

        Args:
            n: The number of stairs to climb

        """
        # EDGE CASE
        if n < 0:
            return 0

        """ALGORITHM"""
        if n not in self.memo:
            self.memo[n] = self.climb_stairs_memoize(n - 1) + self.climb_stairs_memoize(
                n - 2
            )

        # Return cached solution
        return self.memo[n]

    def climb_stairs_tabulate(self, n: int) -> int:
        """Returns the number of distinct paths which climb n stairs

        Context: you are climbing a staircase with n steps. Each time you can
        either climb 1 or 2 steps.

        Args:
            n: The number of stairs to climb
        Examples:
            >>> Solution()._clear_cache() # reset cache for valid method testing
            >>> Solution().climb_stairs_tabulate(2)
            2
            >>> Solution().climb_stairs_tabulate(3)
            3
            >>> Solution().climb_stairs_tabulate(10)
            89
            >>> Solution().climb_stairs_tabulate(-1)
            0

        """
        # EDGE CASE
        if n < 0:
            return 0

        # Generate new values in the space between the solutions currently
        # stored in `memo` and the current n. Note that values won't be
        # recomputed when the function is called again and tabulation would
        # start at the next non-existing value.
        # Assumption:
        #   len(self.memo) == max(self.memo.keys()) + 1
        for i in range(len(self.memo), n + 1):
            self.memo[i] = self.memo[i - 1] + self.memo[i - 2]

        # Return cached solution
        return self.memo[n]


@functools.lru_cache(maxsize=None)  # infinitely sized cache
def climb_stairs_cache(n: int) -> int:
    """Returns the number of distinct paths which climb n stairs

    Context: you are climbing a staircase with n steps. Each time you can
    either climb 1 or 2 steps.

    Note: memoization abstracted away by `lru_cache` function decorator

    Args:
        n: The number of stairs to climb

    Examples:
        >>> climb_stairs_cache(2)
        2
        >>> climb_stairs_cache(3)
        3
        >>> climb_stairs_cache(10)
        89
        >>> climb_stairs_cache(-1)
        0

    """
    # EDGE CASE
    if n < 0:
        return 0

    # Base Cases:
    if 0 <= n <= 2:
        return n

    return climb_stairs_cache(n - 1) + climb_stairs_cache(n - 2)
