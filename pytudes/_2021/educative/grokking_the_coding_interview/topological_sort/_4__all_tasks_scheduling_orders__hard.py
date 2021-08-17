"""

"""

import collections


def print_orders(prerequisites: list[list[int]], num_tasks: int):
    """

    Args:
        num_tasks:
        prerequisites:

    Returns:

    Examples:
        >>> print_orders([[0, 1], [1, 2]], num_tasks=3)
        [0, 1, 2]
        >>> print_orders([[3, 2], [3, 0], [2, 0], [2, 1]], num_tasks=4)
        [3, 2, 0, 1]
        [3, 2, 1, 0]
        >>> print_orders([[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]], num_tasks=6)
        [0, 1, 4, 3, 2, 5]
        [0, 1, 3, 4, 2, 5]
        [0, 1, 3, 2, 4, 5]
        [0, 1, 3, 2, 5, 4]
        [1, 0, 3, 4, 2, 5]
        [1, 0, 3, 2, 4, 5]
        [1, 0, 3, 2, 5, 4]
        [1, 0, 4, 3, 2, 5]
        [1, 3, 0, 2, 4, 5]
        [1, 3, 0, 2, 5, 4]
        [1, 3, 0, 4, 2, 5]
        [1, 3, 2, 0, 5, 4]
        [1, 3, 2, 0, 4, 5]

    """
    if num_tasks <= 0:
        return False

    # a. Initialize the graph
    in_degree = {i: 0 for i in range(num_tasks)}  # count of incoming edges
    graph = {i: [] for i in range(num_tasks)}  # adjacency list graph

    # b. Build the graph
    for parent, child in prerequisites:
        graph[parent].append(child)  # put the child into it's parent's list
        in_degree[child] += 1  # increment child's in_degree

    # c. Find all sources
    # i.e., all vertices with 0 in-degrees
    sources = collections.deque(
        [
            vertex
            for vertex, num_incoming_edges in in_degree.items()
            if num_incoming_edges == 0
        ]
    )

    top_orders = compute_topological_orders(graph, in_degree, sources)
    for top_order in top_orders:
        print(top_order)


def compute_topological_orders(
    graph: dict[int, list[int]],
    in_degree: dict[int, int],
    sources: collections.deque,
    acc_topological_order: list[int] = None,
):
    if acc_topological_order is None:
        acc_topological_order = []

    ## BASE CASE
    # if acc_topological_order doesn't contain all tasks,
    # either we've a cyclic dependency between tasks, or
    # we have not processed all the tasks in this recursive call
    if len(acc_topological_order) == len(graph):
        return [acc_topological_order.copy()]

    ## Find the topological orderings if we chose this source vertex as the
    # next node in the sorted order
    topological_orders = []
    for _ in range(len(sources)):
        ## SETUP
        # only remove the current source,
        # all other sources should remain in the queue for the next call
        curr_source_vertex = sources.popleft()  # 1
        new_sources = sources.copy()  # make a copy of sources
        # get the node's children to decrement their in-degrees
        for child in graph[curr_source_vertex]:  # 3
            in_degree[child] -= 1
            if in_degree[child] == 0:
                new_sources.append(child)

        ## RECURSIVE CALL:
        # get topological orders obtained by choosing current source vertex
        acc_topological_order.append(curr_source_vertex)  # 2
        topological_orders += compute_topological_orders(
            graph, in_degree, new_sources, acc_topological_order
        )

        ## BACKTRACK
        # pop the last explored vertex from the topological order,
        # re-add it to `sources`, and put all of its children back
        # to consider the next source instead of the current vertex
        for child in graph[curr_source_vertex]:  # 3
            in_degree[child] += 1
        unpop = acc_topological_order.pop()  # 2
        assert unpop == curr_source_vertex
        sources.append(curr_source_vertex)  # 1

    return topological_orders
