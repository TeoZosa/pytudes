"""https://leetcode.com/problems/find-smallest-letter-greater-than-target/

Constraints:
    - letters has a length in range [2, 10000].
    - letters consists of lowercase letters, and contains at least 2 unique letters.
    - target is a lowercase letter.

Examples:
    >>> Solution().nextGreatestLetter([],"")
    ''

"""


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        return next_greatest_letter(letters, target)


def next_greatest_letter(letters: list[str], target: str) -> str:
    """Returns the the smallest element in the list that is larger than the given target

    Args:
        letters:
            A list of sorted characters drawn from the lowercase latin
            alphabet that also wraps around. For example, if the target is
            target = 'z' and letters = ['a', 'b'], the answer is 'a'.
        target:
            The letter target for which we are to find the smallest
            strictly greater element.

    Examples:
        >>> next_greatest_letter(["c", "f", "j"],"a")
        'c'
        >>> next_greatest_letter(["c", "f", "j"],"c")
        'f'
        >>> next_greatest_letter(["c", "f", "j"],"d")
        'f'
        >>> next_greatest_letter(["c", "f", "j"],"g")
        'j'
        >>> next_greatest_letter(["c", "f", "j"],"j")
        'c'
        >>> next_greatest_letter(["c", "f", "j"],"k")
        'c'

    """
    if not letters:
        return ""

    start_idx, end_idx = 0, len(letters) - 1
    while start_idx <= end_idx:
        mid_idx = start_idx + (end_idx - start_idx) // 2
        if letters[mid_idx] <= target:
            start_idx = mid_idx + 1
        elif letters[mid_idx] > target:
            end_idx = mid_idx - 1

    # If start_idx pointer exceeded the array bounds, this implies that
    # letters[-1] < next_greatest_letter < letters[0] which further implies
    # that `letters[0]` is the smallest element strictly greater than `target`
    next_greatest_letter_idx = start_idx if start_idx < len(letters) else 0

    return letters[next_greatest_letter_idx]
