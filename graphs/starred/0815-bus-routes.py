# You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

# For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

# Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

# Example 1:

# Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# Output: 2
# Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # We count bus transfers (not individual stops) to measure distance.

        # If source equals target, return 0 (no bus needed).
        # Build a mapping from each stop to the list of bus routes that serve it.

        # Initialize BFS from the source stop, tracking visited stops and visited buses.
        # For each level of BFS (representing one bus ride):
        # For each stop at the current level, check all buses that serve this stop.
        # For each unvisited bus, add all its stops to the next BFS level.
        # Mark buses and stops as visited to avoid revisiting.
        # If we reach the target stop, return the number of bus rides taken.
        # If BFS completes without finding the target, return -1
        # each route is one bus Means:

            # Bus 0 loops forever between:
            # 1,2,7
            # Bus 1 loops forever between:
            # 3,6,7
            # What are we minimizing?

            # NOT:

            # number of stops

            # We want:

            # number of buses we enter

        #source = 1 what buses can i board here? only bus 0

        #now after entering bus 0 i can reach 1,2,7
        #for each of these what bus can i enter?

        #bus 0 and bus 1 
        #that means itransfer to anotehr bus
        #now i can go to 3,6,7
        #each layer means one more bus ride not stop

        if source == target:
            return 0
        #make what stop is what bus id
        stopToBusRoutes = defaultdict(list)
        n = len(routes)
        for bus in range(n):
            for stop in routes[bus]:
                stopToBusRoutes[stop].append(bus)
        
        seen_bus = set()
        seen_stop = set([source])
        res = 0 #this is count
        #bfs
        q = deque([source]) #start at source, these are bus STOPS
        while q:
            for _ in range(len(q)): #for all available bus stops
                stop = q.popleft()
                if stop == target: #check if target
                    return res
                #for all possible buses,
                for bus in stopToBusRoutes[stop]:
                    if bus in seen_bus: #useless work we already explored
                        continue
                        #so we treat buses as layer and each layer has all those stops from every bus
                    seen_bus.add(bus)
                    for nxtStop in routes[bus]: #for each stop in 
                        if nxtStop in seen_stop:
                            continue
                        seen_stop.add(nxtStop)
                        q.append(nxtStop)
            res += 1

        return -1