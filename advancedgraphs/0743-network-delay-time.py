# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

# Example 1:


# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
# Example 2:

# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
# Example 3:

# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        #djisktras 

        t = 0
        minheap = [(0,k)] #store path cost and node

        
        adj = defaultdict(list)
        for u, v , cost in times:
            adj[u].append([v,cost])
        
        visited = set()

        while minheap:
            pathcost, node = heapq.heappop(minheap)
            if node in visited:
                continue
            visited.add(node)
            t = max(t, pathcost)

            for neigh, cost2 in adj[node]:
                if neigh not in visited:
                    heapq.heappush(minheap, (pathcost + cost2, neigh))
            
        return t if len(visited) == n else -1

            
