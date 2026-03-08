# You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

# The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

# You are also given two integers node1 and node2.

# Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.

# Note that edges may contain cycles.

 

# Example 1:


# Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
# Output: 2
# Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
# The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.


from collections import defaultdict, deque
from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        adj = defaultdict(list)                       
        
        for node, directedTo in enumerate(edges):      
            if directedTo != -1:                      
                adj[node].append(directedTo)           

        # BFS that records the shortest distance from 'start' to every reachable node
        # We store distances in distance_map: distance_map[x] = steps from start to x.
        def bfs(start: int, distance_map: dict) -> None:
            q = deque()                              
            q.append((start, 0))                        # push (current_node, distance_from_start)
            distance_map[start] = 0                     # mark start visited with distance 0 (prevents cycles)

            while q:                                    
                curr, dist = q.popleft()               

                for neigh in adj[curr]:                 # explore outgoing neighbor(s) from curr
                    if neigh not in distance_map:       # if we haven't visited neigh yet
                        distance_map[neigh] = dist + 1  # record shortest distance to neigh
                        q.append((neigh, dist + 1))     # push neigh to BFS queue with updated distance

        node1Dist = {}                                  # distances from node1 to reachable nodes
        node2Dist = {}                                  # distances from node2 to reachable nodes

        bfs(node1, node1Dist)                          
        bfs(node2, node2Dist)                           

        res = -1                                        # answer node index (default -1 if no meeting node)
        resDist = float("inf")                          # best (smallest) max-distance found so far

        for i in range(len(edges)):                     
            if i in node1Dist and i in node2Dist:       # candidate must be reachable from both starts
                dist = max(node1Dist[i], node2Dist[i])  # worst-case distance if they meet at i
                if dist < resDist:                      
                    resDist = dist                      # update best distance
                    res = i                             # update best node index


        return res                                     