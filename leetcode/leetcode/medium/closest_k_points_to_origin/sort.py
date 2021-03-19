"""
https://leetcode.com/problems/k-closest-points-to-origin/
"""


class Solution:
    def kClosest(self, points: list[list[int]], K: int) -> list[list[int]]:
        """
        Complexity:
            K = len(heap)
                Time: O(NlogN) to sort entire list of points
                Space: O(N) (worst case) ; O(1) (best case)
                    Since Python sort is Timsort
        Examples:
            >>> Solution().kClosest([[1,3],[-2,2]], 1)
            [[-2, 2]]
            >>> Solution().kClosest([[3,3],[5,-1],[-2,4]], 2)
            [[3, 3], [-2, 4]]
        """
        compute_distance = lambda point: sum([coord ** 2 for coord in point])
        points.sort(key=compute_distance)
        return points[:K]
