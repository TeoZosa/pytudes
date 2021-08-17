"""https://www.educative.io/courses/grokking-the-coding-interview/7npk3V3JQNr

"""


def find_subsets(nums: list[int]) -> list[list[int]]:
    """

    Args:
        nums:

    Returns:

    Examples:
        >>> find_subsets([1, 3, 3])
        [[], [1], [3], [1, 3], [3, 3], [1, 3, 3]]
        >>> find_subsets([1, 5, 3, 3])
        [[], [1], [3], [1, 3], [3, 3], [1, 3, 3], [5], [1, 5], [3, 5], [1, 3, 5], [3, 3, 5], [1, 3, 3, 5]]

    """
    # sort the numbers to handle duplicates by making them adjacent
    nums.sort()

    subsets = [[]]  # Initialized with the empty subset
    prev_new_subsets_start_idx = 0

    for i, curr_num in enumerate(nums):
        prev_num = None if i == 0 else nums[i - 1]
        # if current and the previous elements are same,
        # create new subsets only from the subsets added in the previous step
        valid_subsets_start_idx = (
            0 if curr_num != prev_num else prev_new_subsets_start_idx
        )
        valid_subsets = subsets[valid_subsets_start_idx:]

        # create new subsets from the valid set of subsets
        # and add the current element to it
        new_subsets = [subset + [curr_num] for subset in valid_subsets]

        # Update the prev appended subsets start idx
        # since we are appending to subsets,
        # the first index of the new subsets
        # will be the size of the current subsets array
        prev_new_subsets_start_idx = len(subsets)

        subsets += new_subsets

    return subsets
