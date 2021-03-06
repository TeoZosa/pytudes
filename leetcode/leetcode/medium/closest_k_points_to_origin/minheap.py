"""
Max Heap - O(NlogK); Space: O(K)
  since we need to maintain a priority queue of size K
  and extract the closest K points with a bunch of heap push and pop
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

        heap = []

        for (x, y) in points:
            # Note:
            #   this is K-closest pair of points
            #   with a constant point of (0,0) (origin)
            dist = -(x ** 2 + y ** 2)  # negate to use minheap as a maxheap

            if (
                len(heap) == K
            ):  # maintain a heap of size ≤ K by (potentially) swapping in a new smaller dist
                """Fast version of a heappush followed by a heappop."""
                # noop if dist is farther than the current set of points
                #   (constant-time comparison against the root of the maxheap)
                # else
                #   swap dist with the root of the maxheap
                #   and re-balance the tree
                _ = heapq.heappushpop(heap, (dist, x, y))

            else:  # space left; add item
                heapq.heappush(heap, (dist, x, y))

        return [[x, y] for (dist, x, y) in heap]
