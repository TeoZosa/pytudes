"""https://leetcode.com/problems/k-closest-points-to-origin/

Complexity:
    Sorting - O(NlogN),
      since we need to sort the entire list of points

    Max Heap - O(NlogK),
      since we need to maintain a priority queue of size K
      and extract the closest K points with a bunch of heap push and pop

    Quick Select - O(N) *on average*,
      a modified quick-sort like algorithm (proof of complexity not shown here)

Examples:
    >>> Solution().kClosest([[1,3],[-2,2]], 1)
    [[-2, 2]]
    >>> Solution().kClosest([[3,3],[5,-1],[-2,4]], 2)
    [[3, 3], [-2, 4]]

"""
import heapq


class Solution:  # Space: O(K) since only ≤ K in memory at any one time
    def kClosest(self, points: list[list[int]], K: int) -> list[list[int]]:
        return k_closest_heapq_nsmallest(points, K)


def k_closest_heapq_nsmallest(points: list[list[int]], K: int) -> list[list[int]]:
    """K-closest via `heapq.nsmallest(n, items)`

    Complexity:
        K = len(heap)
            Time: O(NlogK) N heap push/pop operations on heap with size ≤ K
            Space: O(K) priority queue of size K

    Args:
        points:
        K:

    Returns: K-closest points to the origin

    Examples:
        >>> k_closest_heapq_nsmallest([[1,3],[-2,2]], 1)
        [[-2, 2]]
        >>> k_closest_heapq_nsmallest([[3,3],[5,-1],[-2,4]], 2)
        [[3, 3], [-2, 4]]

    """
    compute_distance = lambda point: sum([coord ** 2 for coord in point])
    return heapq.nsmallest(K, points, key=compute_distance)


def k_closest_elaborated(points: list[list[int]], K: int) -> list[list[int]]:
    """K-closest by maintaining a K-sized max heap

    Since a max heap allows us to fetch the furthest distance in constant-time,
    once we build up a K-sized heap, we can maintain size K by only considering
    points with distances better than the furthest known distance. If a point
    does meet this criterion, we pop off the max-distanced point in the heap and
    push the new point.

    Complexity:
        K = len(heap)
            Time: O(NlogK) N heap push/pop operations on heap with size ≤ K
            Space: O(K) priority queue of size K

    Args:
        points:
        K:

    Returns: K-closest points to the origin

    Examples:
        >>> k_closest_elaborated([[1,3],[-2,2]],1)
        [[-2, 2]]
        >>> k_closest_elaborated([[3,3],[5,-1],[-2,4]],2)
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


from scipy import spatial


def k_closest_kd_tree(points: list[list[int]], K: int) -> list[list[int]]:
    """K-closest via `scipy.spatial.KDTree(points).query(x, k, p)`

    We can make use of a data structure called kd-tree
        which are particularly good at searching 2D (or 3D,...,KD) points in logarithmic time.
        Since the points on the 2D planes aren't going to change
        (in most cases)
        during the query, we can preprocess the points
        by constructing a kd-tree to store them for later queries.

    use when:
        - lot of points (≥ 10**6)
        - and only need a few neighbors
        - multiple points for which to find nearest neighbors

    Using a kd-tree to solve this problem is an overkill.
        However, it will be a nice approach for discussion
        if this follow up question comes up during interview.

    What if I have 10 million points now
    and I have to perform the search 10000 times?
    How would you optimize it?

    kd-tree has the following complexity:

    Build the tree - O(NlogN),
      building the tree requires presorting the points
      and finding the medians (but we only need to do this once).

    Search, Insert, Delete - O(logN),
      similar to how a normal binary tree works
      (with a tree balancing mechanism)

    Greatly reduces the time complexity
      for each nearest neighbor query
      to O(logN),
    and if we need to find the K closest points,
      the total complexity will be O(KlogN).

    This is great if we have a lot of points
    and we are only interested in a few neighbors.

    Coding a kd-tree seems daunting and not feasible in a 45-min interviews.
    However, in Python, there is some data science library which allows you to build a tree
    and perform the search in just a few lines of code!

    Since interviewers typically don't expect you to code an actual kd-tree,
    using the following code may not only show
    that you have insights of more advanced data structure,
    but also demonstrate that you have practical experience implementing them
    with pre-existing libraries.


    Complexity:
        n = len(points)
            Time: O(nlogn) (build tree)
                + num_searches*(Klogn) (subsequent searches are efficient)
            Space: O(n)

    Args:
        points:
        K:

    Returns: K-closest points to the origin

    Examples:
        >>> k_closest_kd_tree([[1,3],[-2,2]], 1)
        [[-2, 2]]
        >>> k_closest_kd_tree([[3,3],[5,-1],[-2,4]], 2)
        [[3, 3], [-2, 4]]

    """

    tree = spatial.KDTree(points)
    distance, idx = tree.query(
        # point for which to find nearest neighbors
        x=[0, 0],  # origin
        k=K,  # number of nearest neighbors,
        # Minkowski p-norm
        p=2,  # l2 norm (euclidean distance);
    )
    return [points[i] for i in idx] if K > 1 else [points[idx]]


def k_closest_sorting(points: list[list[int]], K: int) -> list[list[int]]:
    """K-closest points via sorting by distance and returning the first K points

    Complexity:
        n = len(points)
            Time: O(nlogn)
            Space: O(n)

    Args:
        points:
        K:

    Returns: K-closest points to the origin

    Examples:
        >>> k_closest_sorting([[1,3],[-2,2]], 1)
        [[-2, 2]]
        >>> k_closest_sorting([[3,3],[5,-1],[-2,4]], 2)
        [[3, 3], [-2, 4]]

    """
    compute_distance = lambda point: sum([coord ** 2 for coord in point])
    points.sort(key=compute_distance)
    return points[:K]
