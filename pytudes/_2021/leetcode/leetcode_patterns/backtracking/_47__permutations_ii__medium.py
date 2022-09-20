"""https://leetcode.com/problems/permutations-ii/

47. Permutations II
Medium

Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.

Examples:
    >>> Solution().permuteUnique([])
    [[]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

Restrict insertion past the first occurrence of a duplicate value (if one exists)

    To prevent adding a duplicate permutation,
    we only allow insertion of a duplicate element once,
    immediately to the left of the first already-existing duplicate value in the permutation
    and break out of the loop since further iterations will create duplicate permutations.



    ---
        Very smart way to eliminate the duplicate.
    Here is my understanding about the eliminate process.

    After several times of append and other operations,
    #here I just pay attention to one element, 2's position in the inner list
    We get the current list like below:

    [2,x,x,x]
    [x,2,x,x]
    [x,x,2,x]
    [x,x,x,2]
    Of course if we replace the "x" with other elements,
    there should be several other lists in each row,
    but the position of "2" should just be same,
    [0],[1],[2],[3] for each row.

    The approach will traverse each list and insert the new element.
    If the new element is "2", the current "for loop" will break.

    Therefor,after the two loops,the "2" 's position in the list should be:
    [0,1]
    [0,2],[1,2]
    [0,3],[1,3],[2,3]
    [0,4],[1,4],[2,4],[3,4]
    It will actually cover all the situation of the two 2's distribution.

    subsets = [[]]
    for num in [1,2,1,1]:
        []              start
        [(1)]           ins(1)
        [(2),1],[1,(2)] ins(2)

           implicit break     => avoids [1,(1),2]
                        v     v
        [(1),2,1],[2,(1),1],[(1),1,2] ins(1)

       => avoids [1,(1),2,1]...     => avoids [2,1,(1),1]...   => avoids [1,(1),1,2]...
            v                        v                          v
        [(1),1,2,1],[(1),2,1,1],[2,(1),1,1],                [(1),1,1,2] ins(1)


    return [1,1,2,1],[1,2,1,1],[2,1,1,1],[1,1,1,2]

    ---

    Great solution! Here is a short (casual) proof about why break can avoid the duplication.
    Argument: Assume curr_unique_permutations is a list of unique permutations
    with each item length k,
    then new_unique_permutations is a list of unique permutation with length k+1.

    When k=0, it holds.
    Then we prove it will also holds in each iteration using proof by contradiction.

    Suppose duplicate happens when inserting num into the jth location,
        the result is [l2[:char_idx], num, l2[char_idx:]],
        and it duplicates with the item [l1[:j], num, l1[j:]]

    - Suppose char_idx < j,
        then we have l1[char_idx]==num,
        however, we will break when l1[char_idx]==num,
        and thus num will not be inserted after l1[:j] -> contradiction,
    - Suppose char_idx > j,
        then we have l2[j] == num,
        however we will break when l2[j] == num,
        and thus num will not be inserted after l2[:char_idx] -> contradiction.
    - Suppose char_idx==j,
        then we have l1==l2,
        which contradicts the assumption that curr_unique_permutations is a list of unique permutations.

    Thus the argument hold.

    ---
See Also:
    - https://leetcode.com/problems/permutations-ii/discuss/18602/9-line-python-solution-with-1-line-to-handle-duplication-beat-99-of-others-%3A-)
    - [Permutations Involving Repeated Symbols - Example 1](https://www.youtube.com/watch?v=3VBdsNCSBXM)
    - [Permutations II - Backtracking - Leetcode 47](https://www.youtube.com/watch?v=qhBVWf0YafA)
    - https://leetcode.com/problems/permutations-ii/discuss/189116/summarization-of-permutations-I-and-II-(Python)

"""


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        return permute_unique(nums)


def permute_unique(nums: list[int]) -> list[list[int]]:
    """Compute all the *unique* permutations of the elements in a given input array

    Args:
        nums: array of possibly non-distinct elements

    Returns: all *unique* permutations of elements in `nums`

    Examples:
        >>> sorted(permute_unique([1,1,2]))
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        >>> sorted(permute_unique([1,2,1,1]))
        [[1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1], [2, 1, 1, 1]]
        >>> sorted(permute_unique([1,2,3]))
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    """

    """ALGORITHM"""

    def get_last_valid_insertion_idx(perm, item):
        """Restrict insertion past the first occurrence of a duplicate value (if one exists)"""
        # equivalent to `(perm + [item]).index(item)`
        try:
            return perm.index(item)
        except ValueError:
            return len(perm)

    # DS's/res
    uniq_perms = [[]]

    # Build unique permutations
    # increasing the permutation size by 1 at each iteration
    for curr_num in nums:
        uniq_perms = [
            perm[:insertion_idx] + [curr_num] + perm[insertion_idx:]
            for perm in uniq_perms
            for insertion_idx in range(get_last_valid_insertion_idx(perm, curr_num) + 1)
        ]

    return uniq_perms


def permute_unique_i(nums: list[int]) -> list[list[int]]:
    """Compute all the *unique* permutations of the elements in a given input array

    Args:
        nums: array of possibly non-distinct elements

    Returns: all *unique* permutations of elements in `nums`

    Examples:
        >>> sorted(permute_unique_i([1,1,2]))
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        >>> sorted(permute_unique_i([1,2,1,1]))
        [[1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1], [2, 1, 1, 1]]
        >>> sorted(permute_unique_i([1,2,3]))
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    """
    """ALGORITHM"""

    def get_last_valid_insertion_idx(perm, item):  # nosemgrep
        """Restrict insertion past the first occurrence of a duplicate value (if one exists)"""
        # equivalent to `(perm + [item]).index(item)`
        try:
            return perm.index(item)
        except ValueError:
            return len(perm)

    # DS's/res
    uniq_perms = [[]]

    # Build unique permutations
    # increasing the permutation size by 1 at each iteration

    for curr_num in nums:
        np = []
        for perm in uniq_perms:
            for insertion_idx in range(
                get_last_valid_insertion_idx(perm, curr_num) + 1
            ):
                new_perm = perm.copy()
                new_perm.insert(insertion_idx, curr_num)
                np.append(new_perm)

        uniq_perms = np

    return uniq_perms


def permute_unique_long(nums: list[int]) -> list[list[int]]:
    """Compute all the *unique* permutations of the elements in a given
    input array

    Args:
        nums: array of possibly non-distinct elements

    Returns: all *unique* permutations of elements in `nums`

    Examples:
        >>> sorted(permute_unique_long([1,1,2]))
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        >>> sorted(permute_unique_long([1,2,1,1]))
        [[1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1], [2, 1, 1, 1]]
        >>> sorted(permute_unique_long([1,2,3]))
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    """

    """ALGORITHM"""
    uniq_perms = [[]]  # Initialized with the empty set

    # for each iteration, size of current permutations will increase by 1
    # => at the end of the algorithm, size of each permutation will be equal to len(nums)
    for curr_num in nums:
        new_uniq_perms = []

        for perm in uniq_perms:

            # Insert element at each position in existing permutation to create new permutation
            for insertion_idx in range(len(perm) + 1):

                # Bisect-left: Insert `curr_num` to the left of insertion_idx in perm
                # increases size of permutation by 1
                new_perm = perm[:insertion_idx] + [curr_num] + perm[insertion_idx:]
                new_uniq_perms.append(new_perm)

                # Prevents duplicates
                # equivalent to setting the for loop as:
                #   `for insertion_idx in range(get_last_valid_insertion_idx(perm,curr_num) + 1):`
                if insertion_idx < len(perm) and perm[insertion_idx] == curr_num:
                    break

        uniq_perms = new_uniq_perms

    return uniq_perms


def permute_unique_set(nums: list[int]) -> list[list[int]]:
    """Compute all the *unique* permutations of the elements in a given input array

    Args:
        nums: array of possibly non-distinct elements

    Returns: all *unique* permutations of elements in `nums`

    Examples:
        >>> sorted(permute_unique_set([1,1,2]))
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        >>> sorted(permute_unique_set([1,2,1,1]))
        [[1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1], [2, 1, 1, 1]]
        >>> sorted(permute_unique_set([1,2,3]))
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    """

    uniq_perms = {tuple()}  # Initialized with the empty set

    # for each iteration, size of current permutations will increase by 1
    # => at the end of the algorithm, size of each permutation will be equal to len(nums)
    for curr_num in nums:

        # Bisect-left: Insert `curr_num` to the left of insertion_idx in perm
        # (increases size of permutation by 1)
        uniq_perms = {
            # tuples for hashability
            (*perm[:insertion_idx], curr_num, *perm[insertion_idx:])
            for perm in uniq_perms
            for insertion_idx in range(len(perm) + 1)
        }

    return [list(permutation) for permutation in uniq_perms]


def permute_unique_backtrack(nums: list[int]) -> list[list[int]]:
    """Compute all the *unique* permutations of the elements in a given input array

    Args:
        nums: array of possibly non-distinct elements

    Returns: all *unique* permutations of elements in `nums`

    Examples:
        >>> sorted(permute_unique_backtrack([1,1,2]))
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        >>> sorted(permute_unique_backtrack([1,2,1,1]))
        [[1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1], [2, 1, 1, 1]]
        >>> sorted(permute_unique_backtrack([1,2,3]))
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    """

    ## INITIALIZE VARS ##

    # DS's/res
    nums_counts = {}
    for num in nums:
        nums_counts[num] = nums_counts.get(num, 0) + 1

    res = []

    # Populate res
    def compute_possible_permutations(sub_permutation):
        # BASE CASE
        if len(sub_permutation) == len(nums):
            res.append(sub_permutation.copy())
        else:
            # iterate over *distinct* elements
            for curr_num in nums_counts:  # pylint: disable=consider-using-dict-items

                # If there are remaining instances of `curr_num` left to choose
                # => Select curr_num at this position
                #   and continue building permutation from remaining elements
                if nums_counts[curr_num] > 0:

                    ## BACKTRACK
                    # Save space by in-place appending/popping
                    nums_counts[curr_num] -= 1  # Select `curr_num` at current position
                    sub_permutation.append(curr_num)

                    compute_possible_permutations(sub_permutation)

                    sub_permutation.pop()
                    # Deselect `curr_num` at current position
                    nums_counts[curr_num] += 1

    compute_possible_permutations(sub_permutation=[])  # initialize with empty list

    return res


def permute_unique_backtrack_stack(nums: list[int]) -> list[list[int]]:
    """Compute all the *unique* permutations of the elements in a given input array

    Args:
        nums: array of possibly non-distinct elements

    Returns: all *unique* permutations of elements in `nums`

    Examples:
        # >>> sorted(permute_unique_backtrack_stack([1,1,2]))
        # [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        >>> sorted(permute_unique_backtrack_stack([1,2,1,1]))
        [[1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1], [2, 1, 1, 1]]
        >>> sorted(permute_unique_backtrack_stack([1,2,3]))
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    """
    # (STALE) TODO(teo): stack-based backtracking
    #  2. Your implementation is allowed to use a Stack, a Queue
    #  Hint: Use the stack to store the elements
    #  yet to be used to generate the permutations,
    #  and use the queue to store the (partial) collection of permutations
    #  generated so far.

    ## INITIALIZE VARS ##

    # DS's/res
    nums_counts = {}
    for num in nums:
        nums_counts[num] = nums_counts.get(num, 0) + 1

    res = []
    stack = [[]]  # empty set on stack
    # stack2 = [[[]]]  # empty set on stack
    while stack:
        sub_permutation = stack.pop()
        # sub_perms = stack2.pop()
        # track state?

        # BASE CASE
        if len(sub_permutation) == len(nums):
            res.append(sub_permutation)
        else:

            # (STALE) TODO(teo): find a way to avoid nums_count updates every time
            # without passing in a a dict
            for used_num in sub_permutation:
                nums_counts[used_num] -= 1  # Select `curr_num` at current position

            children = [
                sub_permutation + [curr_num]
                for curr_num, curr_num_count in nums_counts.items()
                if curr_num_count > 0
            ]

            stack.extend(children)
            # stack2.append(children)
            # cats = 2

            # for curr_num in nums_counts:
            #
            #     # If there are remaining instances of `curr_num` left to choose
            #     # => Select curr_num at this position
            #     #   and continue building permutation from remaining elements
            #     if nums_counts[curr_num] > 0:
            #         stack.append(sub_permutation + [curr_num])

            for used_num in sub_permutation:
                nums_counts[used_num] += 1  # Deselect `curr_num` at current position

    return res


def permute_unique_matt(nums: list[int]) -> list[list[int]]:
    """Compute all the *unique* permutations of the elements in a given input array

    Args:
        nums: array of possibly non-distinct elements

    Returns: all *unique* permutations of elements in `nums`

    Examples:
        >>> sorted(permute_unique_matt([1,1,2]))
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        >>> sorted(permute_unique_matt([1,2,1,1]))
        [[1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1], [2, 1, 1, 1]]
        >>> sorted(permute_unique_matt([1,2,3]))
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    """

    if len(nums) == 1:
        return [nums]

    uniq_perms = []
    already_used_set_of_elements_at_curr_pos = set()

    for curr_num in nums:

        # Since we are selecting elements at the current pos,
        # skip repeated elements we had already explored once before
        if curr_num not in already_used_set_of_elements_at_curr_pos:
            nums_tmp = nums.copy()
            nums_tmp.remove(curr_num)

            uniq_perms.extend(
                [
                    [curr_num] + sub_permutation
                    for sub_permutation in permute_unique_matt(nums_tmp)
                ]
            )

            already_used_set_of_elements_at_curr_pos.add(curr_num)

    return uniq_perms


def permute_unique_matt_teo(nums: list[int]) -> list[list[int]]:
    """Compute all the *unique* permutations of the elements in a given input array

    Args:
        nums: array of possibly non-distinct elements

    Returns: all *unique* permutations of elements in `nums`

    Examples:
        >>> sorted(permute_unique_matt_teo([1,1,2]))
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        >>> sorted(permute_unique_matt_teo([1,2,1,1]))
        [[1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1], [2, 1, 1, 1]]
        >>> sorted(permute_unique_matt_teo([1,2,3]))
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    """

    if len(nums) == 1:
        return [nums]

    distinct_nums = set(nums)

    uniq_perms = []
    for curr_num in distinct_nums:
        nums_tmp = nums.copy()
        nums_tmp.remove(curr_num)

        uniq_perms.extend(
            [
                [curr_num] + sub_permutation
                for sub_permutation in permute_unique_matt_teo(nums_tmp)
            ]
        )

    return uniq_perms
