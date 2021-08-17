"""https://leetcode.com/problems/permutations/


Given an array nums of distinct integers,
return all the possible permutations.
You can return the answer in any order.


Examples:
    >>> sorted(Solution().permute([1,2,3]))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(Solution().permute([0,1]))
    [[0, 1], [1, 0]]
    >>> Solution().permute([1])
    [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return permute(nums)


def permute(nums: list[int]) -> list[list[int]]:

    """ALGORITHM"""

    # DS's/res
    uniq_perms = [[]]

    for curr_num in nums:
        uniq_perms = [
            perm[:insertion_idx] + [curr_num] + perm[insertion_idx:]
            for perm in uniq_perms
            for insertion_idx in range(len(perm) + 1)
        ]

    return uniq_perms
