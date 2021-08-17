"""https://www.educative.io/courses/grokking-the-coding-interview/B8R83jyN3KY

"""
from collections import deque


def find_permutations(nums: list[int]) -> list[list[int]]:
    """

    Args:
        nums:

    Returns:

    Examples:
        >>> find_permutations([1, 3, 5])
        [[5, 3, 1], [3, 5, 1], [3, 1, 5], [5, 1, 3], [1, 5, 3], [1, 3, 5]]

    """

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


def find_permutations_orig(nums: list[int]) -> list[list[int]]:
    """

    Args:
        nums:

    Returns:

    Examples:
        >>> find_permutations_orig([1, 3, 5])
        [[5, 3, 1], [3, 5, 1], [3, 1, 5], [5, 1, 3], [1, 5, 3], [1, 3, 5]]

    """

    """ALGORITHM"""

    # DS's/res
    result = []
    curr_permutations = deque([[]])  # Initialized with the empty subset

    for curr_num in nums:

        # For all existing permutations:
        #   add the current number to create new permutations
        for _ in range(len(curr_permutations)):

            perm = curr_permutations.popleft()
            # create a new permutation by adding the current number at every position
            for insertion_idx in range(len(perm) + 1):
                new_perm = perm[:insertion_idx] + [curr_num] + perm[insertion_idx:]

                if len(new_perm) == len(nums):
                    result.append(new_perm)
                else:
                    curr_permutations.append(new_perm)

    return result
