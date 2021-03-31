"""
for
K = num_closest_points
N = |points|

k-d tree: O(K log N); Space: O(K)

use when:
  lot of points (≥ 10**6)
  and only need a few neighbors


Using a kd-tree to solve this problem is an overkill.
However, it will be a nice approach for discussion
if this follow up question comes up during interview.

What if I have 10 million points now
and I have to perform the search 10000 times?
How would you optimize it?

Let's first have a review of some solutions that we have already come across:

Sorting - O(NlogN),
  since we need to sort the entire list of points

Max Heap - O(NlogK),
  since we need to maintain a priority queue of size K
  and extract the closest K points with a bunch of heap push and pop

Quick Select - O(N) *on average*,
  a modified quick-sort like algorithm (proof of complexity not shown here)

As we can see,
  if we have N=10000000
  and we have to perform the search over a large number of times,
  even O(N) solution may seem to be inefficient in this extreme case.

So, what can we do?
  We can make use of a data structure called kd-tree
  which are particularly good at searching 2D (or 3D,...,KD) points in logarithmic time.
  Since the points on the 2D planes aren't going to change
  (in most cases)
  during the query,
  we can preprocess the points
  by constructing a kd-tree to store them for later queries.

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
using the following code may not only show that you have insights of more advanced data structure,
but also demonstrate that you have practical experience implementing them with pre-existing libraries."""
from scipy import spatial


class Solution:
    def kClosest(self, points: list[list[int]], K: int) -> list[list[int]]:
        """
        >>> Solution().kClosest([[1,3],[-2,2]], 1)
        [[-2, 2]]
        >>> Solution().kClosest([[3,3],[5,-1],[-2,4]], 2)
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
