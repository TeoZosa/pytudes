"""

See Also:
    https://leetcode.com/problems/median-of-two-sorted-arrays/
    https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn)))-solution-with-explanation
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        return compute_median_sort(nums1, nums2)


def compute_median_sort(nums1: list[int], nums2: list[int]) -> float:
    """
    Complexity:
        N = len(nums1) + len(nums2)
        Time: O(nlogn) for sort
        Space: O(n) for sort space
    Returns:
    Examples:
        >>> compute_median_sort([2],[1,3])
        2
        >>> compute_median_sort([3,4],[1,2])
        2.5
        >>> compute_median_sort([0,0],[0,0])
        0.0
        >>> compute_median_sort([1],[])
        1
        >>> compute_median_sort([],[2])
        2
    """
    ## EDGE CASES ##
    if not nums2 and not nums1:
        raise ValueError

    """ALGORITHM"""
    combined = sorted(nums1 + nums2)

    ## FIND MEDIAN OF COMBINED sorted array ##
    combined_size = len(combined)
    mid = (combined_size - 1) // 2
    if combined_size % 2 == 1:
        return combined[mid]
    else:
        return (combined[mid] + combined[mid + 1]) / 2


def compute_median_merge(nums1: list[int], nums2: list[int]) -> float:
    """
    Args:
        nums1:
        nums2:
    Complexity:
        N = len(smaller_arr) + len(bigger_arr)
        Time: O(n) for merge
        Space: O(n) for merged array space
    Returns:
    Examples:
        >>> compute_median_merge([2],[1,3])
        2
        >>> compute_median_merge([3,4],[1,2])
        2.5
        >>> compute_median_merge([0,0],[0,0])
        0.0
        >>> compute_median_merge([1],[])
        1
        >>> compute_median_merge([],[2])
        2
    """
    ## EDGE CASES ##
    if not nums2 and not nums1:
        raise ValueError

    """ALGORITHM"""
    ## INITIALIZE VARS##
    nums1_curr_idx = nums2_curr_idx = 0

    # res
    combined = []

    ## MERGE ##
    while nums1_curr_idx < len(nums1) and nums2_curr_idx < len(nums2):
        if nums1[nums1_curr_idx] <= nums2[nums2_curr_idx]:
            combined.append(nums1[nums1_curr_idx])
            nums1_curr_idx += 1
        else:
            combined.append(nums2[nums2_curr_idx])
            nums2_curr_idx += 1
    ## POST-CONDITION: 1 and only 1 array exhausted
    # => exhaust the remaining elements in the other

    if nums1_curr_idx == len(nums1):
        while nums2_curr_idx < len(nums2):
            combined.append(nums2[nums2_curr_idx])
            nums2_curr_idx += 1
    else:
        while nums1_curr_idx < len(nums1):
            combined.append(nums1[nums1_curr_idx])
            nums1_curr_idx += 1

    ## FIND MEDIAN OF COMBINED sorted array ##
    combined_size = len(combined)
    mid = (combined_size - 1) // 2
    if combined_size % 2 == 1:
        return combined[mid]
    else:
        return (combined[mid] + combined[mid + 1]) / 2


def compute_median_binary_search(
    smaller_arr: list[int], larger_arr: list[int]
) -> float:
    """Perform binary search on two sorted arrays to find their alignment points from which a unified median can be computed

    Given S = smaller_arr, L = larger_arr
    For S,L : |S| ≤ |L|,

    if combined = sorted(S+L) && mid_idx = len(combined)-1 // 2
    Binary search to find *ALIGNMENT POINT*:
        S[S_left_idx]  ≤  L[L_right_idx]
     && L[L_left_idx]  ≤  S[S_right_idx]

    so that
        combined[mid_idx]   == max(S[S_left_idx], L[L_left_idx])
     && combined[mid_idx+1] == min(L[L_right_idx], S[S_right_idx])

    Explanation:
        For
                         S Left Half             |                     S Right Half
            -oo  S[0], S[1], ... , S[S_left_idx] | S[S_right_idx], S[i+1], ... , S[S_size-1], +oo

                         L Left Half             |                     L Right Half
            -oo  L[0], L[1], ... , L[L_left_idx] | L[L_right_idx], L[j+1], ... , L[L_size-1], +oo

        We can also zip them such that:
                           Left Half             |                     Right Half
            -oo  S[0], S[1], ... , S[S_left_idx] | S[S_right_idx], S[i+1], ... , S[S_size-1], +oo
            -oo  L[0], L[1], ... , L[L_left_idx] | L[L_right_idx], L[j+1], ... , L[L_size-1], +oo
        =>
        ** INSIGHT **
            If we can ALIGN them such that:
                max(left_part) <= min(right_part)
                i.e.,
                    S[S_left_idx]  ≤  L[L_right_idx]
                 && L[L_left_idx]  ≤  S[S_right_idx]

        =>
                           Left Half             |                     Right Half
                 -oo  ..., S[i-2], S[S_left_idx] | S[S_right_idx], S[i+1], ... , +oo
                 -oo  ..., L[j-2], L[L_left_idx] | L[L_right_idx], L[j+1], ... , +oo
                                       ^         |        ^
                             combined[mid_idx]   | combined[mid_idx+1]
                                    ==           |          ==
                              max(S[S_left_idx], | min(L[L_right_idx],
                                  L[L_left_idx]) |     S[S_right_idx])
                                                <=>
                             WHEN S[S_left_idx]  ≤  L[L_right_idx]
                               && L[L_left_idx]  ≤  S[S_right_idx]

        e.g. For S = [2], L = [1,3] =>
                                             median = 2
                                                <=>
                                             *Alignment* =
                                                [2]+oo
                                               [1,3]
                                                <=>
                                       Left Half | Right Half
                                         -oo [(2 |+oo)]  +oo+1
                                         -oo [(1 | 3 )]  +oo
                                                <=>
                                            S_left_idx = 0 (mid)
                                            S_right_idx = 1 (+oo) (mid+1)
                                            L_left_idx = 0 (mid)
                                            L_right_idx = 1 (mid+1)
        e.g. For S = [1,2,3,4,5], L = [1,1,1,1,2,2,2,2,10,11,12] =>
                                             median = 2
                                                <=>
                                             *Alignment* =
                                              [1,2,3,4,5]
                                     [1,1,1,1,2,2,2,2,10,11,12]
                                                <=>
                                       Left Half | Right Half
                                       -oo [1,(2 | 3),4,5]  +oo
                               -oo [1,1,1,1,2,(2 | 2),2,10,11,12]  +oo
                                                <=>
                                            S_left_idx = 1 (mid -1)
                                            S_right_idx = 2 (mid)
                                            L_left_idx = 5 (mid)
                                            L_right_idx = 6 (mid+1)
        e.g. For S = [1,2,3,4,5], L = [1,1,1,1,2,2,2,2,10,11,12] =>
                                             median = 2
                                                <=>
                                             *Alignment* =
                                      [1,2,3,4,500,600,600,600,600,600,600,600,600,600]
                                      [1,2,3,4,5,6,7,8,9,10]
                                                <=>
                                       Left Half | Right Half
                                       -oo [1,(2 | 3),4,5]  +oo
                               -oo [1,1,1,1,2,(2 | 2),2,10,11,12]  +oo
                                                <=>
                                            S_left_idx = 9 (mid -1)
                                            S_right_idx = 10 (mid)
                                            L_left_idx = 47 (mid)
                                            L_right_idx = 48 (mid+1)


        If we can ensure:

        1) len(left_part) == len(right_part)
        2) max(left_part) <= min(right_part)
        then we divide all elements in {smaller_arr, larger_arr} into
            two parts with equal length,
            with one part always greater than the other.

        Then median = (max(left_part) + min(right_part))//2. #EVEN

        To ensure these 2 conditions, we just need to ensure:

        (1) S_right_idx + L_right_idx == (S_size - S_right_idx + L_size - L_right_idx)
            ( or in the odd case: S_size - S_right_idx + L_size - L_right_idx + 1)

            if |S| ≤ |L|, we just need to set:
                for ∀ S_right_idx ∈ [0, S_size]:
                    `L_right_idx = (S_size + L_size + 1)//2 - S_right_idx`

        (2) S[S_left_idx]  ≤  L[L_right_idx]
         && L[L_left_idx]  ≤  S[S_right_idx]

        ps.1 For simplicity, I presume
            smaller_arr[S_right_idx-1]
            larger_arr[L_right_idx-1]
            smaller_arr[S_right_idx]
            larger_arr[L_right_idx]
        are always valid
        even if
            S_right_idx=0
            S_right_idx=S_size
            L_right_idx=0
            L_right_idx=L_size
        I will talk about how to deal with these edge values at last.

        ps.2 Why |S| ≤ |L|?
            To ensure L_right_idx is non-negative
                since
                    1. 0 <= S_right_idx <= S_size
                    2. L_right_idx = (S_size + L_size + 1)/2 - S_right_idx.
                If |S| > |L|
                    => L_right_idx may be negative
                    => wrong results.

        So, all we need to do is:

        Searching S_right_idx in [0, S_size], to find an object `S_right_idx` that:
            larger_arr[L_right_idx-1] <= smaller_arr[S_right_idx]
            and smaller_arr[S_right_idx-1] <= larger_arr[L_right_idx],
            ( where L_right_idx = (S_size + L_size + 1)/2 - S_right_idx )

        And we can do a binary search following steps described below:





    Args:
        smaller_arr:
        larger_arr:
    Complexity:
        Time: O(log(smaller_arr))
        Space: O(1)
    Returns:
    Examples:
        >>> compute_median_binary_search([2],[1,3])
        2
        >>> compute_median_binary_search([3,4],[1,2])
        2.5
        >>> compute_median_binary_search([0,0],[0,0])
        0.0
        >>> compute_median_binary_search([1],[])
        1
        >>> compute_median_binary_search([],[2])
        2
        >>> A,B = [1,2,3,4,5], [1,1,1,1,2,2,2,2,10,11,12]
        >>> assert(compute_median_binary_search(A,B) == compute_median_sort(A,B))
        >>> A,B = [1,2,3,4,5,6,7,8,9,10], [1,2,3,4] + [i for i in range(5,700)]
        >>> assert(compute_median_binary_search(A,B) == compute_median_sort(A,B))
    """
    ## EDGE CASES ##
    if not larger_arr and not smaller_arr:
        raise ValueError

    L_size, S_size = len(larger_arr), len(smaller_arr)
    if S_size > L_size:  # ensure |S| ≤ |L| always
        return compute_median_binary_search(
            smaller_arr=larger_arr, larger_arr=smaller_arr
        )
    """ALGORITHM"""
    ## INITIALIZE VARS ##
    S_start_idx, S_end_idx = 0, S_size
    combined_mid_idx = (S_size + L_size + 1) // 2

    ## FIND ALIGNMENT points:
    #   S[S_left_idx]  ≤  L[L_right_idx]
    #   L[L_left_idx]  ≤  S[S_right_idx]
    #   (i.e. monotonically increasing)
    while S_start_idx <= S_end_idx:
        S_right_idx = (S_start_idx + S_end_idx) // 2
        S_left_idx = S_right_idx - 1

        S_left = smaller_arr[S_left_idx] if S_left_idx >= 0 else -float("inf")
        S_right = smaller_arr[S_right_idx] if S_right_idx < S_size else float("inf")

        ## Companion mid-pair indexes in L <=> reflected across L
        # (i.e. if left partition of S <=> right partition of L and vice versa)
        L_right_idx = combined_mid_idx - S_right_idx
        L_left_idx = L_right_idx - 1

        L_left = larger_arr[L_left_idx] if L_left_idx >= 0 else -float("inf")
        L_right = larger_arr[L_right_idx] if L_right_idx < L_size else float("inf")

        if S_left > L_right:  # LEFT of S => RIGHT of L
            S_end_idx = S_right_idx - 1
        elif L_left > S_right:  # RIGHT of S => LEFT of L
            S_start_idx = S_right_idx + 1
        else:  # S_left ≤ L_right && L_left ≤ S_right <=> equivalent to the midpoint of a single merged array
            max_left = max(S_left, L_left)  # <=> combined[mid]
            min_right = min(S_right, L_right)  # <=> combined[mid+1]
            if (S_size + L_size) % 2 == 1:
                return max_left
            else:
                return (max_left + min_right) / 2
