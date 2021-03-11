"""
https://leetcode.com/problems/minimum-number-of-refueling-stops/
See Also: leetcode/Miscellany/Interviews/minimum_number_of_refueling_stops.py
"""

###Leetcode solutions###

"""Approach 1: 1D DP, O(N^2)"""
###
def minRefuelStops_DP(
    target_distance: int, start_fuel: int, stations: list[list[int]]
) -> int:
    """
    DP_table[num_stops]
        the furthest distance (== max gas) that we can get
        with num_stops times of refueling.

    So for every station, stations[i],
        if the current distance DP_table[num_stops] >= stations[i][0], we can refuel:
            DP_table[num_stops + 1] = max(
                DP_table[num_stops + 1],
                DP_table[num_stops] + stations[i][1]
                )

    In the end, we'll return
        the first num_stops with DP_table[num_stops] >= target,
        otherwise -1.

    Args:
        target_distance:
        start_fuel:
        stations: list of [distance, gallon] pairs, in sorted order of distance

    Returns: LEAST # of stops to destination OR -1 if not possible
    Examples:
        >>> stations = [[10,60],[20,30],[30,30],[60,40]]
        >>> minRefuelStops_DP(target_distance=100, start_fuel=10, stations=stations)
        2
        >>> minRefuelStops_DP(target_distance=100, start_fuel=1, stations=stations)
        -1
        >>> minRefuelStops_DP(target_distance=1, start_fuel=1, stations=[])
        0
        >>> stations = [[10,10],[20,10],[30,30],[60,40]]
        >>> minRefuelStops_DP(target_distance=100, start_fuel=10, stations=stations)
        4
    """
    ##Initialize

    # vars
    pass

    # DS's/res
    # DP_table[num_stops]<=> furthest distance (== max gas) possible if refueling num_stops times.
    DP_table = [start_fuel] + [0] * len(stations)  # |DP_table| == len(stations) + 1

    ## POPULATE the table
    for station_i in range(len(stations)):

        # Check all stops ≤ current station_idx
        # Updates values from the worst case (all stations) to the best case (0 stations)
        for num_stops in range(station_i + 1)[::-1]:  # Backwards iteration
            station_distance, station_fuel = stations[station_i]

            curr_fuel = DP_table[num_stops]
            if curr_fuel >= station_distance:  # station is reachable
                ## VISIT station
                # update if a better option was found
                DP_table[num_stops + 1] = max(
                    DP_table[num_stops + 1], curr_fuel + station_fuel
                )

    ## FIND OPTIMAL value
    # Return the 1st min number of stops
    # where distance traveled ≥ target distance
    for num_stops, travel_distance in enumerate(DP_table):
        if travel_distance >= target_distance:
            return num_stops

    return -1


import heapq

"""Approach 2: Priority Queue, O(NlogN)"""
# Note: implicitly accounts for distance traveled since
# we can add the fuel we would have gained at a stop
# to the fuel we started with
# which expands the set of ultimately reachable stations
#
# since the condition we want to find is:
# (prev_fuel - station_distance + station_fuel) curr_fuel  ≥ curr_target (prev_target - station_distance)
#                               <==>
# (prev_fuel + station_fuel) curr_fuel  ≥ target (prev_target);
def minRefuelStops_maxheap(
    target_distance: int, start_fuel: int, stations: list[list[int]]
) -> int:
    """
    For every loop:
        We add all reachable stop to priority queue.
        We pop out the largest gas from pq and refuel once.
        If we can't refuel => we can't go forward => return -1
    Args:
        target_distance:
        start_fuel:
        stations: list of [distance, gallon] pairs, in sorted order of distance

    Returns: LEAST # of stops to destination OR -1 if not possible
    Examples:
        >>> stations = [[10,60],[20,30],[30,30],[60,40]]
        >>> minRefuelStops_maxheap(target_distance=100, start_fuel=10, stations=stations)
        2
        >>> minRefuelStops_maxheap(target_distance=100, start_fuel=1, stations=stations)
        -1
        >>> minRefuelStops_maxheap(target_distance=1, start_fuel=1, stations=[])
        0
        >>> stations = [[10,10],[20,10],[30,30],[60,40]]
        >>> minRefuelStops_maxheap(target_distance=100, start_fuel=10, stations=stations)
        4
    """
    ##Initialize

    # vars
    next_station_idx = 0
    curr_fuel = start_fuel

    # DS's/res
    priority_queue = []  # maxheap of fuel amounts from reachable station
    num_stops = 0

    while curr_fuel < target_distance:
        ## ADD currently reachable stations
        while (
            next_station_idx < len(stations)
            and stations[next_station_idx][0] <= curr_fuel
        ):
            station_fuel = stations[next_station_idx][1]
            # make a maxheap by negating value
            heapq.heappush(priority_queue, -station_fuel)
            next_station_idx += 1

        ## HANDLE EMPTY
        # no reachable stations => no gas to travel further => FAIL
        if not priority_queue:
            return -1

        ## VISIT reachable station
        # Add all fuel from the MAX(station_fuel) reachable station;
        # Remove station from priority_queue
        #   Note: adding to curr_fuel implicitly takes distance into account
        curr_fuel += -heapq.heappop(priority_queue)
        num_stops += 1  # increment visited stations count
    return num_stops
