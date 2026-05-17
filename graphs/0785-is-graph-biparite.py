# There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

# There are no self-edges (graph[u] does not contain u).
# There are no parallel edges (graph[u] does not contain duplicate values).
# If v is in graph[u], then u is in graph[v] (the graph is undirected).
# The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

# Return true if and only if it is bipartite.


from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # color[i] will store the "side" (partition) of node i
        # 0  => unvisited / uncolored
        # 1  => color A
        # -1 => color B
        color = [0] * len(graph)

        def bfs(start: int) -> bool:
            # If this node is already colored, its component was handled before
            if color[start] != 0:
                return True
            q = deque([start])

            # Assign an arbitrary color to the start node
            color[start] = 1


            while q:

                node = q.popleft()
                for nei in graph[node]:
                    # Case 1: neighbor has not been colored yet.
                    if color[nei] == 0:
                        # Give neighbor the opposite color of current node
                        color[nei] = -color[node]
                        q.append(nei)

                    # Case 2: neighbor is already colored
                    else:
                        # If neighbor has the same color as current node, not bipartite
                        if color[nei] == color[node]:
                            return False

            return True

        
        #can not be all connected so we run BFS from every node (only starts new BFS if uncolored)
        for i in range(len(graph)):
            # If any component fails bipartite check, whole graph is not bipartite
            if not bfs(i):
                return False


        return True

