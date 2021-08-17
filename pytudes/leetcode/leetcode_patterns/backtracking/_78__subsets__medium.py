"""https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements,
return all possible subsets (the power set).
    - The solution set must not contain duplicate subsets.
    - Return the solution in any order.

Constraints:
    - 1 ≤ nums.length ≤ 10
    - -10 ≤ nums[i] ≤ 10
    - All the numbers of nums are unique.

Examples:
    >>> Solution().subsets([])
    [[]]

"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        return find_subsets(nums)


def find_subsets(nums: list[int]) -> list[list[int]]:
    """

    https://cs.stackexchange.com/questions/121230/explanation-of-on2n-time-complexity-for-powerset-generation

    𝑇(𝑁)=2𝑇(𝑁−1)+2^(𝑁−1)
    𝑇(1)=2

        Note that the entire runtime, our algorithm only spends time generating more data. T
        herefore, our function T represents both the amount of time that the function spends running on an input of size N,
        and also the amount of data it generates from an input of size N.

    We have 2𝑇(𝑁−1) because we first make the recursive call,
    and the following line makes a copy of all that data again
    in preparation to tack on the element we left out in the recursive call.

    We tack on exactly 2𝑁−1 copies of the element we intentionally left out
    so that's where the last term comes from.

    Finally, T(1)=2 because with 1 element, we return 2 possible subsets (the entire set and the empty set).

    Unrolling this recurrence we have:

    𝑇(𝑁)=2𝑇(𝑁−1)+2^(𝑁−1)
    =2(2(𝑇(𝑁−2)+2𝑁−2)+2^(𝑁−1)
    =2(2(2(𝑇(𝑁−3)+2𝑁−3)+2𝑁−2)+2^(𝑁−1)
    ...
    =2𝑁+(𝑁−1)∗2^(𝑁−1)
    =𝑂(𝑁∗2^𝑁)

    Complexity: sum (i * 2^(i-1)) for i=>n ?
        n = len(nums)
        Time: O(n*2^n) (i.e. in the last iteration of the algorithm)
            - O(2^n) subsets: the number of subsets doubles at each step (if not a duplicate element)
                since we add each element to all the existing subsets
            - O(n) for building each subset since we must copy and append to an existing subset
        Space: O(n*2^n) (for the output list)
            - O(2^n) subsets (if no duplicates)
            - O(n) for each subset

    Args:
        nums: array of distinct elements

    Returns: The powerset of `nums`

    Examples:
        >>> find_subsets([1,2,3])
        [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        >>> find_subsets([0])
        [[], [0]]

    """

    subsets = [[]]  # Initialized with the empty subset

    for num in nums:
        # we will take all existing subsets
        # and insert the current number in them to create new subsets
        new_subsets = [subset + [num] for subset in subsets]
        subsets += new_subsets

    return subsets
