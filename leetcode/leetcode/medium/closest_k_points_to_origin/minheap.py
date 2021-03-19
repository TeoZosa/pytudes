"""
    Complexity:
        K = len(heap)
            Time: O(NlogK) N heap push/pop operations on heap with size ≤ K
            Space: O(K) priority queue of size K
"""
import heapq


class Solution:  # Space: O(K) since only ≤ K in memory at any one time
    def kClosest(self, points: list[list[int]], K: int) -> list[list[int]]:
        """
        >>> Solution().kClosest([[1,3],[-2,2]], 1)
        [[-2, 2]]
        >>> Solution().kClosest([[3,3],[5,-1],[-2,4]], 2)
        [[3, 3], [-2, 4]]
        """
        return heapq.nsmallest(
            K, points, key=lambda point: sum([coord ** 2 for coord in point])
        )


class Solution_elaborated:
    def kClosest(self, points: list[list[int]], K: int) -> list[list[int]]:
        """
        >>> Solution_elaborated().kClosest([[1,3],[-2,2]], 1)
        [[-2, 2]]
        >>> Solution_elaborated().kClosest([[3,3],[5,-1],[-2,4]], 2)
        [[-2, 4], [3, 3]]
        """

        """ALGORITHM"""
        ## INITIALIZE VARS ##
        max_heap = []

        for point in points:
            # negate to use minheap as a maxheap
            dist = -sum([coord ** 2 for coord in point])
            dist_and_point = (dist, point)

            # maintain a max_heap of size ≤ K
            if len(max_heap) < K:
                heapq.heappush(max_heap, dist_and_point)
            else:
                # if current point's distance is better
                #   pop point with worst distance
                #   and push current point
                # else
                #   noop
                _ = heapq.heappushpop(max_heap, dist_and_point)

        return [point for (dist, point) in max_heap]
