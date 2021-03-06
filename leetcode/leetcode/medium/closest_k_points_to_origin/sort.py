"""
Sorting - O(NlogN); Space: O(N)
  since we need to sort the entire list of points


"""


class Solution:
    def kClosest(self, points: list[list[int]], K: int) -> list[list[int]]:
        """
        >>> Solution().kClosest([[1,3],[-2,2]], 1)
        [[-2, 2]]
        >>> Solution().kClosest([[3,3],[5,-1],[-2,4]], 2)
        [[3, 3], [-2, 4]]
        """
        distance_fn = lambda point: sum([coord ** 2 for coord in point])
        points.sort(key=distance_fn)
        return points[:K]
